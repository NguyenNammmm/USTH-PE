from pathlib import Path
import collections,hashlib,html,json,re,textwrap
from PIL import Image
ROOT=Path(__file__).resolve().parent
FONT=Path('C:/Windows/Fonts')
def payload(_=True):
    data=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8-sig'))
    for lesson in data['lessons']:lesson['markdown']=(ROOT/lesson['path']).read_text(encoding='utf-8-sig')
    for lesson in data.get('supplementalLessons',[]):lesson['markdown']=(ROOT/lesson['path']).read_text(encoding='utf-8-sig')
    data['docs']={p.stem:p.read_text(encoding='utf-8-sig') for folder in ['docs','research'] for p in (ROOT/folder).glob('*.md')}
    return data
def build_pdf():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import BaseDocTemplate,PageTemplate,Frame,Paragraph,Spacer,PageBreak,XPreformatted,Table,TableStyle,Image as RLImage
    from reportlab.platypus.tableofcontents import TableOfContents
    for n,f in [('VI','arial.ttf'),('VIB','arialbd.ttf'),('VII','ariali.ttf'),('Code','consola.ttf'),('Math','seguisym.ttf')]:pdfmetrics.registerFont(TTFont(n,str(FONT/f)))
    pdfmetrics.registerFontFamily('VI',normal='VI',bold='VIB',italic='VII',boldItalic='VIB')
    width,height=A4;left=45;right=45;usable=width-left-right
    styles={
      'body':ParagraphStyle('body',fontName='VI',fontSize=10.5,leading=15.7,spaceAfter=8,splitLongWords=True),
      'list':ParagraphStyle('list',fontName='VI',fontSize=10.5,leading=15.7,spaceAfter=7,leftIndent=14,firstLineIndent=-14,splitLongWords=True),
      'title':ParagraphStyle('title',fontName='VIB',fontSize=30,leading=37,textColor=colors.HexColor('#173b44'),spaceAfter=18),
      'group':ParagraphStyle('group',fontName='VIB',fontSize=25,leading=31,textColor=colors.HexColor('#17675b'),spaceAfter=18,keepWithNext=True),
      'lesson':ParagraphStyle('lesson',fontName='VIB',fontSize=21,leading=27,textColor=colors.HexColor('#173b44'),spaceAfter=16,keepWithNext=True),
      'h2':ParagraphStyle('h2',fontName='VIB',fontSize=14,leading=19,textColor=colors.HexColor('#17675b'),spaceBefore=13,spaceAfter=9,keepWithNext=True),
      'h3':ParagraphStyle('h3',fontName='VIB',fontSize=11.5,leading=16,spaceBefore=10,spaceAfter=7,keepWithNext=True),
      'code':ParagraphStyle('code',fontName='Code',fontSize=8.1,leading=11.2,backColor=colors.HexColor('#eef2f2'),borderPadding=6,spaceBefore=4,spaceAfter=10),
      'cell':ParagraphStyle('cell',fontName='VI',fontSize=8.6,leading=12.5,spaceAfter=3),
      'small':ParagraphStyle('small',fontName='VI',fontSize=8,leading=11.5,textColor=colors.HexColor('#51666c'),spaceAfter=7)
    }
    primary=pdfmetrics.getFont('VI').face.charToGlyph;mathfont=pdfmetrics.getFont('Math').face.charToGlyph;codefont=pdfmetrics.getFont('Code').face.charToGlyph
    unknown=set();wrapped=[]
    def clean(t):
        return str(t).replace('\ufeff','').replace('\u2011','-').replace('\u2013','-').replace('\u2014','-').replace('\u00a0',' ')
    def rich(t):
        t=html.escape(clean(t))
        code=[]
        def protect(m):
            code.append('<font name="Code">'+m[1]+'</font>');return '@@C'+str(len(code)-1)+'@@'
        t=re.sub(r'`([^`]+)`',protect,t)
        t=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',t)
        t=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',r'<link href="\2" color="#17675b">\1</link>',t)
        t=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',t)
        for i,value in enumerate(code):t=t.replace('@@C'+str(i)+'@@',value)
        for c in set(t):
            if ord(c)>127 and ord(c) not in primary:
                if ord(c) in mathfont:t=t.replace(c,'<font name="Math">'+c+'</font>')
                else:unknown.add(c)
        return t
    def p(t,style='body'):return Paragraph(rich(t),styles[style])
    class Book(BaseDocTemplate):
        def __init__(self,path):
            super().__init__(str(path),pagesize=A4,leftMargin=left,rightMargin=right,topMargin=50,bottomMargin=46,title='Database Advanced - Chặng tiếp theo sau 85 bài PE',author='Programming Education - Nội dung và đặc tả biên soạn',allowSplitting=1)
            self.addPageTemplates(PageTemplate(id='book',frames=[Frame(left,46,usable,height-96,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=self.decorate));self.page_map={}
        def decorate(self,c,d):
            c.saveState();c.setFillColor(colors.HexColor('#50666b'));c.setFont('VI',7.7);c.drawString(left,height-25,'DATABASE ADVANCED / USTH + DSC7e');c.drawRightString(width-right,height-25,'06/11/2026');c.setStrokeColor(colors.HexColor('#ccd5d5'));c.line(left,height-33,width-right,height-33);c.drawString(left,25,'Bài giảng Advanced và đặc tả web - MySQL baseline');c.drawRightString(width-right,25,str(d.page));c.restoreState()
        def afterFlowable(self,f):
            if getattr(f,'_anchor',None):
                self.canv.bookmarkPage(f._anchor);self.canv.addOutlineEntry(f.getPlainText(),f._anchor,f._level,False);self.notify('TOCEntry',(f._level,f.getPlainText(),self.page,f._anchor));self.page_map[f._anchor]=self.page
    def heading(t,anchor,level=0,style='group'):
        q=p(t,style);q._anchor=anchor;q._level=level;return q
    def codeblock(lines,lid):
        blocks=[]
        for line in lines:
            line=clean(line).expandtabs(4)
            # Wrap for display only. The executable MD/SQL files retain original lines.
            if pdfmetrics.stringWidth(line,'Code',8.1)>usable-14:
                wrapped.append({'lesson':lid,'line':line})
                indent=min(len(line)-len(line.lstrip())+4,20)
                pieces=textwrap.wrap(line,width=99,subsequent_indent=' '*indent,replace_whitespace=False,drop_whitespace=False,break_long_words=True,break_on_hyphens=False)
                blocks.extend(pieces or [''])
            else:blocks.append(line)
        # XPreformatted itself can split at line boundaries across pages.
        markup=html.escape('\n'.join(blocks))
        for c in set(markup):
            if ord(c)>127 and ord(c) not in codefont:
                if ord(c) in mathfont:markup=markup.replace(c,'<font name="Math">'+c+'</font>')
                else:unknown.add(c)
        return XPreformatted(markup,styles['code'])
    def flow(text,lid=''):
        lines=text.splitlines();i=0;out=[]
        while i<len(lines):
            line=lines[i];i+=1
            if not line.strip():continue
            if line.startswith('```'):
                b=[]
                while i<len(lines) and not lines[i].startswith('```'):b.append(lines[i]);i+=1
                i+=1
                if b:out.append(codeblock(b,lid))
                continue
            h=re.match(r'^(#{1,6})\s+(.*)',line)
            if h:
                node=p(h[2],'h2' if len(h[1])<=2 else 'h3')
                if lid and h[2].startswith('Minh họa theo trạng thái'):node._anchor=lid+'-states';node._level=2
                out.append(node)
                board=ROOT/'assets/state-boards'/(lid+'.png')
                if lid and h[2].startswith('Minh họa theo trạng thái') and board.exists():
                    im=Image.open(board);scale=min(usable/im.width,590/im.height)
                    out.extend([RLImage(str(board),width=im.width*scale,height=im.height*scale),Spacer(1,10)])
                continue
            if line.startswith('|'):
                rows=[line]
                while i<len(lines) and lines[i].startswith('|'):rows.append(lines[i]);i+=1
                rows=[r for r in rows if not re.match(r'^\|[\s:|\-]+\|?$',r)]
                cells=[[x.strip() for x in r.strip('|').split('|')] for r in rows];n=max(map(len,cells))
                for r in cells:r.extend(['']*(n-len(r)))
                widths=[usable/n]*n
                if n==3:widths=[usable*.18,usable*.40,usable*.42]
                if n==4:widths=[usable*.12,usable*.30,usable*.30,usable*.28]
                table=Table([[p(c,'cell') for c in r] for r in cells],colWidths=widths,repeatRows=1,hAlign='LEFT',splitInRow=1)
                table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e7f1eb')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),.35,colors.HexColor('#ccd5d5')),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
                out.extend([table,Spacer(1,9)]);continue
            if line.startswith('- '):out.append(p('• '+line[2:]));continue
            if re.match(r'^\d+\.\s',line):out.append(p(line,'list'));continue
            para=[line]
            while i<len(lines) and lines[i].strip() and not re.match(r'^(#|```|\||- |\d+\.\s)',lines[i]):para.append(lines[i]);i+=1
            out.append(p(' '.join(para)))
        return out
    data=payload(True)
    story=[Spacer(1,45),p('DATABASE ADVANCED','title'),p('Chặng tiếp theo sau 85 bài Database PE','title'),p('85 bài Advanced, 24 bài trọng tâm và 11 phần bổ sung USTH. Lời giảng, ví dụ, thuật toán, lập luận, bài tập và đáp án.','h2'),p('06/11/2026 - Đã đối chiếu 947 thân mục sách và 458 trang lecture/practice với nội dung hiện hành. Xem phụ lục bằng chứng và giới hạn xác minh.','small'),p('Khóa thu phí, học và thực hành trên web. MySQL là hệ chính; PostgreSQL và hệ khác được nêu rõ khi cần.'),p('Bộ nền 85 bài được giữ nguyên trong thư mục baseline để ôn theo kỹ năng. Đây là tài liệu mới nối tiếp, không phải bản đổi tên bộ nền.'),Spacer(1,12),p('Nguồn đối chiếu: 9 lecture và 3 practice USTH; Database System Concepts 7e, 26 chương in, Appendix A và 6 chương online 27–32. Nội dung viết mới theo kiến thức; không sao chép toàn văn giáo trình.'),p('Bản bàn giao cho đội dev: nội dung và đặc tả runner web cùng mô hình tương tác. Demos tính theo mô hình; chỉ kết quả có engine artifact mới được gọi là chạy thật.'),p('PDF để tra cứu đầy đủ. Code dài có thể xuống dòng khi in; dùng bản Markdown/SQL đi kèm khi sao chép. Mục lục có liên kết theo chương, bài và phần minh họa trạng thái.','small'),PageBreak()]
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc0',fontName='VIB',fontSize=10,leading=15,spaceBefore=9),ParagraphStyle('toc1',fontName='VI',fontSize=9,leading=13,leftIndent=14),ParagraphStyle('toc2',fontName='VI',fontSize=8,leading=11.5,leftIndent=28,textColor=colors.HexColor('#17675b'))]
    story += [p('Mục lục có liên kết','group'),toc,PageBreak()]
    for name,title in [('course-design','Cách đi từ nền tảng sang Advanced'),('repo-labs','Lab đã chọn từ repo')]:
        if name in data['docs']:story += [heading(title,'front-'+name),*flow(data['docs'][name]),PageBreak()]
    by={x['id']:x for x in data['lessons']}
    for module in data['modules']:
        story += [heading(module['id']+' · '+module['title'],'module-'+module['id']),p('Các bài: '+', '.join(module['lessonIds'])),p('Điều kiện trước ở từng bài giúp mở đúng phần cần ôn. Thứ tự số mã không thay cho quan hệ tiên quyết.'),PageBreak()]
        for lid in module['lessonIds']:
            lesson=by[lid];story.append(heading(lid+' · '+lesson['title']+(' [Trọng tâm]' if lesson['key'] else ''),lid,1,'lesson'))
            content=lesson['markdown'].split('\n',1)[1]
            story += flow(content,lid)
            story.append(PageBreak())
    if data.get('supplementalLessons'):story += [heading('Các phần bổ sung từ lecture và practice USTH','supplements'),p('151 câu hỏi kèm đáp án; các kỹ năng, giả định và bài thực hành riêng của slide.'),PageBreak()]
    for lesson in data.get('supplementalLessons',[]):
        story += [heading(lesson['id']+' · '+lesson['title'],lesson['id'],1,'lesson'),*flow(lesson['markdown'].split('\n',1)[1],lesson['id']),PageBreak()]
    for name,title in [('coverage-map','Bản đồ sách và slide sang nội dung'),('semantic-coverage-status','Trạng thái đối chiếu đầy đủ từng mục nguồn'),('slide-semantic-coverage-status','Đối chiếu từng trang USTH'),('web-runner-spec','Đặc tả đầy đủ runner web'),('usth67-web-acceptance','ERD và object database: ca nghiệm thu web'),('teaching-contract','Thiết kế bài học và đánh giá'),('ad85-learning-sequence','AD85: từ tài liệu tra cứu tới các lượt luyện'),('repo-quality','Kiểm định các repo được chọn'),('verification-scope','Bằng chứng kiểm và giới hạn')]:
        if name in data['docs']:story += [heading(title,'appendix-'+name),*flow(data['docs'][name]),PageBreak()]
    for name in ['advanced_core.sql','company_advanced_overlay.sql']:
        source=ROOT/'fixtures'/name
        if source.exists():story += [heading('Fixture: '+name,'fixture-'+name),p('File phục vụ backend sandbox được chỉ định; không gửi lệnh reset vào dữ liệu production.'),codeblock(source.read_text(encoding='utf-8-sig').splitlines(),name),PageBreak()]
    doc=Book(ROOT/'Database-Advanced-PE.pdf');doc.multiBuild(story,maxPasses=4)
    result={'pages':doc.page,'bookmarks':doc.page_map,'lessons':len(data['lessons']),'supplemental_lessons':len(data.get('supplementalLessons',[])),'supplemental_questions':sum(x['practiceQuestions'] for x in data.get('supplementalLessons',[])),'key_lessons':sum(x['key'] for x in data['lessons']),'wrapped_code_lines':len(wrapped),'unsupported_characters':sorted(unknown),'font_size_body':10.5,'font_size_code':8.1}
    (ROOT/'qa/pdf-build.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='bookmarks'},ensure_ascii=False));assert not unknown,unknown
if __name__=='__main__':build_pdf()
