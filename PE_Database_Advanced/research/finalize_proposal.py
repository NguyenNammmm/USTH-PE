from pathlib import Path
import json,collections
O=Path(__file__).resolve().parent
base=json.loads((O/'advanced-progression-proposal.json').read_text(encoding='utf-8'))['lessons']
for item in base:
 if item['id']=='AD29':item['bookPrefixes']=['14.5','24.5']
 if item['id']=='AD30':item['bookPrefixes']=['14.6','14.7','14.9','14.10','24.3']
 if item['id']=='AD31':item['bookPrefixes']=['14.8','24.2']
 if item['id']=='AD15':item['bookPrefixes']=['8.4','24.4']
 if item['id']=='AD59':item['bookPrefixes']=['A']
 if item['id']=='AD60':item['bookPrefixes']=[] # project integrates prior lessons; does not own wholechapters
 if item['id']=='AD03':item['bookPrefixes'].append('7.4')
 if item['id']=='AD05':item['bookPrefixes'].append('7.5')
children=[
('AD62','Raft: bầu leader, log matching và commit an toàn','AD52',['23.8.3'],'Trace hai term/ba node, conflict suffix và old-term entry; lập luận election safety/log matching; phân biệt điều kiện tiến triển.'),
('AD63','Long-duration, operation-level và real-time transactions','AD41',['18.10'],'Chọn compensation/semantic conflict thay row conflict; chỉ ra trạng thái trung gian và deadline không tương đương serializability.'),
('AD64','Distributed files, indexes và key-value stores','AD47',['21.5','21.6','21.7'],'Theo dõi block/metadata/re-replication, partitioned index routing và online resharding; tách storage placement khỏi query semantics.'),
('AD65','Distributed timestamp, locking và global snapshots','AD51',['23.3','23.5'],'Xây toàn lịch xuyên site, timestamp generation/leases/deadlock; chứng minh snapshot từng site chưa đủ global consistency.'),
('AD66','Asynchronous replication, conflict resolution và Merkle tree','AD51',['23.6'],'Trace stale/version conflict, vector-style detection theo nguồn, reconcile collections bằng Merkle tree và quy tắc resolve.'),
('AD67','Từ file đến cloud: hợp đồng DBMS và tiến hóa kiến trúc','AD01',['1'],'Dùng lịch sử trong sách như bối cảnh; nối yêu cầu, abstraction, engine và architecture bằng case so sánh có giả định, bổ sung1.9 còn thiếu ở C01.'),
('AD68','XML model, schema và XPath','AD16',['30.1','30.2','30.3'],'Định nghĩa tree/order/identity/mixed content, DTD/XMLSchema; trace XPath axes/predicates và khác vị trí predicate.'),
('AD69','IR: relevance, vector ranking và link analysis','AD17',['31.1','31.2','31.3','31.4'],'Tính score TF-IDF/cosine trên corpus nhỏ; precision/recall; PageRank một vòng và diễn giải giới hạn.'),
('AD70','Classification và regression: tính mô hình nhỏ','AD19',['11.4.2','11.4.3'],'Trace decision tree, Bayes, margin/neural network theo mức nguồn; regression/prediction kháccausalclaim, validation độc lập.'),
('AD71','Association rules và clustering','AD19',['11.4.4','11.4.5'],'Tính support/confidence/lift, tạo frequent itemsets; lặp clustering với metric/initialization rõ, ca confounding.'),
('AD72','Warehouse, star schema và OLAP','AD18',['11.1','11.2','11.3'],'Xác định grain/hierarchy và summarizability; cube/rollup/pivot, ETL vs lake, báo cáo tránh double counting.'),
('AD73','Big-data storage và kiến trúc xử lý','AD20',['10.1','10.2','10.3'],'Phân biệt physical partition/replication với logical model; storage format/metadata và failure assumptions trướcMapReduce.'),
('AD74','Ordered, sparse và multilevel indices','AD27',['14.1','14.2'],'Tìm block bằng index nhiều mức; tính I/O theo fanout/ordering và trace update dense/sparse khi first-key thay đổi.'),
('AD75','Bloom filter: bit, hash và xác suất false positive','AD31',['24.1'],'Build/test với hash cho trước, chứng minh no-false-negative theo mô hình insert-only và tính false positive giả định độc lập.'),
('AD76','Selection operators và mô hình chi phí','AD32',['15.1','15.2','15.3'],'So scan/index/binary-search trên thông số block/seek; conjunctive/disjunctive predicates, cache và estimated-cost limitations.'),
('AD77','Nested-loop join: tuple, block và index','AD33',['15.5.1','15.5.2','15.5.3'],'Pseudocode và trace đủ duplicate/null theo join predicate; cost đảo outer với buffer budget và index fanout.'),
('AD78','Decorrelation và tối ưu subquery','AD37',['16.4.4'],'Chứng minh EXISTS→semijoin, bác rewriteNOT IN/NULL và aggregatecorrelation; trace querygraph trước/sau.'),
('AD79','Cloud database architecture và multi-tenancy','AD46',['20.5','20.6','20.7'],'Tách compute/storage, resource governance, availability/failure domain; không đồng nhất autoscaling với correctness.'),
('AD80','Parallel execution plan và scheduling','AD48',['22.5','22.6','22.7'],'Pipeline/interoperator/independent parallelism, exchange/buffer, scheduling/resource model và contention.'),
('AD81','Blockchain: hash, chữ ký và validation','AD54',['26.1','26.2','26.3'],'Hash links/Merkle/signature chỉ đảm bảo dưới giả định cryptographic; validate transaction/ownership và double-spend.'),
('AD82','Smart contracts, ledger state và query','AD54',['26.5','26.6','26.7','26.8'],'Trace state transition hợp lệ, oracle/autonomous/cross-chain limitations; index/query throughput khácconsensus throughput.'),
('AD83','PostgreSQL memory contexts và execution lifetime','AD58',['32.8.4','32.8.8.1'],'Theo dõi allocation/reset theo tuple/query/transaction; chứng minh lifetime contract và lỗi giữ pointer qua reset.'),
('AD84','PostgreSQL Node, Datum và tuple','AD58',['32.8.5','32.8.6','32.8.7'],'Read code C có typedef/modeltrước; dispatch NodeTag đúng, Datum by-value/by-reference và tuple descriptor/null bitmap.'),
('AD85','Routine và trigger: chuyển trạng thái có transaction','AD12',['5.2','5.3'],'Procedure parameters/cursor/exception; row/statementtriggers, recursion/sideeffects và ca multiple-row đúnginvariant.'),
]
for ident,title,parent,refs,targets in children:
 p=next(x for x in base if x['id']==parent)
 base.append({'id':ident,'title':title,'module':p['module'],'before':p['before'],'bookPrefixes':refs,'requiredDeepening':[targets],'activityFormats':p['activityFormats'],'webEnvironment':p['webEnvironment'],'status':'proposed-child-not-authored','key':ident in {'AD62','AD65','AD75','AD77','AD83','AD84'},'splitFrom':parent})
examples={
'AD01':['Ba customer có0,1,2paid orders: ON/WHERE/filter/COUNT tạo những multiset nào.','NOT IN trả UNKNOWN khi subquery cóNULL; thêm UNIQUE/NOTNULL rồi chứng minh rewrite anti-join hợp lệ.'],
'AD02':['R(A,B)={(1,2),(2,3)},S(B)={(2)}: dịch exists và forall sang calculus/SQL.','{t | NOT R(t)} phụ thuộc miền; mở miền từ{1,2} sang{1,2,3} làm lộ truy vấn khôngsafe.'],
'AD03':['R(A,B,C,D,E),F={AB→C,C→D,D→E}: traceAB+ bằng fixpoint và chứng minh invariant.','F={AC→D},startA: thuật toán sai dùng giao thay subset tạoD; dựng hai tuple bác bỏ.'],
'AD04':['F={A→BC,B→C,AB→D,D→E}: rút canonical cover và kiểm từng bước equivalence.','R(A,B,C,D),F={A→B,B→A,C→D}: tìm đủAC,BC và bác heuristic loại mọi thuộc tínhRHS.'],
'AD05':['R(A,B,C),F={A→B}: táchAB,AC, dùnggiaoA chứng minh lossless.','R(A,B,C),F={AB→C,C→B}: BCNFtáchBC,AC làm mất bảo toànAB→C; trace projection chính xác.'],
'AD06':['R(A,B,C,D),F={A→B,B→C}: synthesisAB,BC rồi thêmAD vì cácrelation chưa chứa key.','Cover{A→B,B→A,C→D} choAB,CD: thêmAC hoặcBC, so những kết quả 3NF khác nhau nhưng cùng hợp đồng.'],
'AD07':['R(Student,Hobby,Language),Student→→Hobby: bốn tuple là tích haihobby/hai language.','Ba tuple thiếu một tổ hợp: chiếu rồi join tạo tuple mới, chứng minh instance vi phạmMVD.'],
'AD08':['R(A,B,C) với JD*(AB,BC,AC): cho relation cụ thể rồi ghép ba projection.','R(Order,Item,Qty) cóQty>0: key/domainconstraint với quy tắc liên-rowtổngkhôngvượtcredit, phân biệtDKNF.'],
'AD09':['Quan hệ supplier-part-project không thay bằng ba binaryrelationship nếu mất ràng buộc bộba.','Hai salaryperiods[Jan1,Feb1),[Feb1,Mar1) khôngoverlap nhưng đổi end-inclusive tạo boundaryconflict.'],
'AD10':['Cây1→2→3 và3→1: trace recursiveCTE UNION/UNIONALL và terminationguard.','Điểm10,10,8: RANK/DENSERANK/ROWS/RANGE cho khác frame và peer semantics.'],
'AD11':['TransferaccountA→B bằng haiUPDATE: mất kết nối saucommit tạo retrydouble-effect nếu thiếu idempotencykey.','Preparedquery email=? nhậnchuỗi dấuquote nhưng dynamicORDERBY identifierphảiwhitelist.'],
'AD12':['Hai roles reader/writer với cột nhạy cảm: ca allow/deny và viewboundary.','Invokervsdefiner function đọc bảngẩn; kiểm quyền và searchpath không lộ thôngtin.'],
'AD13':['JSON orders cómissingdiscount,null,0: trace path extraction và cast trướcaggregate.','RDF triplespeople/knows/worksAt: SPARQLpatternjoin và optionalmissing khácINNERmatch.'],
'AD14':['MộtPerson cóObjectID độc lậpname, hai references trỏ cùngobject sauupdate.','SubtypeStudent/Employee chungPersonID: ánhxạtablepertype so với nestedobject vàdanglingreference.'],
'AD15':['Bốn point vàrectangle: boundingbox giữcandidatefalsepositive trước exactcirclepredicate.','Điểm nằm đúngbiên polygon và haiSRID khác: cầnquyước boundary/coordinate trướcchấm.'],
'AD16':['XQuery fororder join customerlet/where/return tạoXMLaggregate cóschema đầy đủ.','XPath//item[1] khác(//item)[1]; trace trên haiorder mỗiorderhaitem.'],
'AD17':['Postinglists d1,d3,d7 vàd2,d3,d7: mergeintersection có duplicatepositions và skip.','Top-K thay câu hỏi: dừng sớm khi upperbound chứng minh phần còn lại khôngvượt kthscore.'],
'AD18':['Summary SUM=90,COUNT=2; insert30 rồi deletepricecựcđại: delta SUM/COUNT khácMIN/MAX.','Joinorders-lines vớikhách3dòng: mộtUPDATEparent tạo ba resultdeltas theo bagmultiplicity.'],
'AD19':['Train/test cùngcustomerID tạo leakage dù row khác; sửa split theoentity.','Corpusvăn bản4documents: tách labels,features và giữtestđộc lập khi chọnthreshold.'],
'AD20':['Wordcount3inputpartitions: trace map,shuffle,reduce;combinerSUMhợp lệ,AVGkhôngcócount thìsai.','Retrymộtmaptask: outputcommitprotocol khônggộpcảresultcũvàmới.'],
'AD21':['Events10:00,10:02,09:59 tới theo thứtự ấy; watermark/window policy quyếtđịnh lateevent.','Crashsauoutputtrướccheckpoint: replaytạoduplicate khi sinkkhôngidempotent.'],
'AD22':['Graph1→2,1→3,2→4,3→4: frontierBFS vàvisited tránhnhânđườngđi.','Cycle4→1: fixpointreachabilitydừng nhưng recursivepathkhôngguard cóthểkhôngdừng.'],
'AD23':['Diskblock4KiB,seek5ms,throughput100MiB/s: so1000randomread với sequentialscan.','RAIDmirror cócùngfailure-domain khác haiindependentcopy; recovery cầnđọccònđủblock.'],
'AD24':['Page128byte,header16,slot4byte: chènrecord20,30 rồi xóa20 và compact giữslotID.','Heaprecord mởrộng vượtfree-space: forwarding/move làm unstablephysicaladdress.'],
'AD25':['CLOCK3frames,refbits vàpin cho trước; sequenceA,B,C,A,D phải chọnvictim hợp lệ.','Tất cảframespinned: thuậttoán khôngđược evictdirtypage chỉ đểđạtcachehit mục tiêu.'],
'AD26':['Column[NY,NY,NY,LA,LA]: dictionary/RLE encodedsize so vớirowmaterialization.','Querychọn2/20columnsso vớiupdateallcolumns: localityvàwrite-amplificationđổi cost.'],
'AD27':['B+leafmax3keys: insert10,20,30,40,50,60,70 và root/leafsplit.','Duplicateuserkey=20 vớiRIDkhác: địnhnghĩatotalkey đểsearch/rangescan đúng.'],
'AD28':['B+treeleafmin2,max4: delete keygâyborrowrồi mergerootcontraction.','Leafsibling splitgiữlatchpath kháctransactionkeylock; trace reader lúcseparatorupdate.'],
'AD29':['Extendiblehash globaldepth2 với bucketlocaldepth1: splitkhôngnhânmọibucket.','Linearhashpointerp=2,level1: insertcollision,overflowrồi splitbucketp khácbucketnhậninsert.'],
'AD30':['Index(a,b) với predicatesa=2ANDb>5,b=5,a>2ANDb=5: range/covering khác nhau.','Bitmapsstatuspaid/pending trên8rows: AND/OR vàwritecost khi đổi mộtrow.'],
'AD31':['Memtablex=1,x=2,tombstonex: merge SSTables theo sequencegiữ latest đúng.','Compactionlàm rơi tombstone quá sớm trong khi lowerlevel cònx=1 khiếngiátrịhồi sinh.'],
'AD32':['B=1000pages,M=11buffers: tạo run11 rồi merge10-way, tính sốpass.','B≤M mộtpassmemorysortkhácB=M+1 cầnspill; côngthứcceil cầnxétboundary.'],
'AD33':['HashjoinR có6tupleskeyskew,S có4: partitionskhácsize và overflowstrategy.','MergejoinRkeys1,1,2,Skeys1,1,1: groupduplicates phải tạo6cặpkey1.'],
'AD34':['Scan→filter→sort→limit: iteratornext dừng ở đâu, sortblocking giữgì.','Setdifference với duplicate input: DISTINCTsemantics khácbag EXCEPTALL; lưu counts.'],
'AD35':['N=1000,V(city)=10 nhưngHanoichiếm900: independenceestimate100 lệchactual900.','JoinR(A) cóNDV10,S(A) cóNDV20: nêu containment/uniformity trước dùngN_R*N_S/maxNDV.'],
'AD36':['A,B,C với ba selectivities/costs cho trước: DPsubsetsAB,AC,BC rồiABC.','PlanABcost8 unorderedvs10 sorted: merge vớiC làm phươngánintermediateđắt hơn thắngtotal.'],
'AD37':['RefreshrevenueAVG bằngSUM/COUNT thay averageofaverages khi groupsizeskhác.','TopKORDERBYpriceDESCvớities: limitk khôngđủnếubusinessyêu cầuWITH TIES.'],
'AD38':['r1(A),r2(A),w1(A),w2(A): hai cạnh tạo cycle và khôngconflictserializable.','Acyclicschedulelập topologicalorder rồi swapadjacentnonconflictingops để dựng serialschedule.'],
'AD39':['T1readA,writeB/T2readB,writeA: 2PLthêmwait vàcóthểdeadlock dùserializable.','IntentionIXởrootvàXởleaf: compatibilitybảo vệancestor màkhôngkhóaXmọitable.'],
'AD40':['T1holdsA,T2holdsB,rồiđòiB/A: wait-forcycle và chọnvictim/retry.','TimestampT1=5,T2=9: wait-die vàwound-wait chờ/abort khác nhau theo requestolder→younger.'],
'AD41':['RTS(X)=8,WTS(X)=3,Ttimestamp5 muốnwrite: TOabort đểkhôngđọcquákhứ sai.','OCCoverlappingread/write sets củaT1,T2: kiểm3casevalidation interval theo commitorder.'],
'AD42':['Hai doctorsđềureadsnapshoton-call2rồi tắtbảnthân: disjointwrites vẫn phá invariant≥1.','ReadCommittedhairead khácvalue sauBcommit; RepeatableReadsnapshotkhôngđồngnghĩamọiDMLread giống.'],
'AD43':['T1committedX10→15,T2uncommittedY20→99; storageX10,Y99: redo/undo vềX15,Y20.','Dirtypageflushtrướclogdurable làWALviolation; crashmấtbeforeimagekhôngthể tựsuyundo.'],
'AD44':['LogLSN10updateP,20commitT1,30updateQbyT2; PageLSNP10,Q0: skip10,redo30,undoT2.','CrashsauCLR40durabletrướcpageflush: redoCLRrồitheoundoNext, khôngundoCLR.'],
'AD45':['PrimaryACKtrướcbackupdurable rồiprimaryloss: traceRPOkhôngbằng0.','SnapshotX10vàcommands+5,+7: replaydeterministicvàexternalrandomresult đượclogkhácnhau.'],
'AD46':['Sharednothing4nodes với data skew90/3/3/4: speedup bịnode90%giữ.','Shared-diskcùngstoragecontrollerchậm: thêmcompute khônggiảm bottleneckI/O.'],
'AD47':['Hashpartitionmod4 đổi5nodes làmđổirouting; consistent/rangeplacement cầnmigrationmetadata.','Hotcustomerchiếm70%orders: partitiontheokeygiữjoinlocal nhưng skew, saltingđổiqueryplan.'],
'AD48':['BroadcastS=10MiB tới4workersvsrepartitionR=1GiB/S10MiB: tínhnetworktraffic với giảđịnh.','ParallelaggregateAVG: merge(sum,count) đúng, averageofpartitionaverages sai.'],
'AD49':['SiteA:R1000rows,SiteB:S10rows: semijoinshipkeys+filteredrows so vớishipfullR.','FDWsourcekhôngsupportpredicate cast: localrecheck vànetworkcost; snapshotkhôngtựglobal.'],
'AD50':['T1hai participantsvoteYES,coordinatorcrashsauprepare: participantphảibảo toànuncertainty.','Coordinatorcommitlogdurable,ACKmất: participantrestartxin decision khôngtựabort.'],
'AD51':['N=5,W=3,R=3: mọi read/write quorum giao ít nhất1, nhưng chọnvalue cầnversionprotocol.','Multi-keyA/B read từ haireplica snapshotskhác tạo total khôngtừng tồn tại dù từngkeymới.'],
'AD52':['Paxosballot9 nhậnaccepted(5,X),(7,Y),none: chọnY vàgiảithích preservechosenvalue.','LeaderAterm4 bịpartition, Bterm5: fencingstorage phải từchốitoken4 dù A còn sống.'],
'AD53':['Indexthêmgiảmreadscansnhưng tănginsertcost: workload90/10 khác10/90 có kếtluậnkhác.','Benchmarkcoldcachevswarmcache haiquerykhácresult làso sánhkhônghợp lệ; sửaprotocol.'],
'AD54':['PoWforkhai nhánhcùngheight: confirmationpolicy vàreorganizationrisk khôngtươngđương2PCcommit.','Byzantine nodegửihai messagekhácnhau: majoritycrashfault khôngtựchịuByzantine.'],
'AD55':['HeapCTIDđổi sauupdate nhưngbusinesskeygiữ; PKindexkhôngclusterheap nhưInnoDB.','Coveringindextruyxuất đủcolumn nhưngvisibilitymapunset vẫn cầnheapfetch; đọcplanthật khi runner có.'],
'AD56':['ARepeatableReadreadsx10,Bupdate20commit,Ađọclạivẫn10; kếtthúcsnapshot.','Longsnapshotgiữoldtuplehorizon, VACUUM khôngthể thu hồi bảnphiênbản cònneeded; SQLlab2session.'],
'AD57':['Numericcustomfunctionvàexpressionindexlower(name): operator/typecontract trướcplan.','postgres_fdwjoinremote/local: projection/filterpushdown và transactionguarantee cần capability riêng.'],
'AD58':['Đọcqueryexecutionscan→projection: phânbiệtPlan node vàPlanState với callnext.','Buildextensionhàmadd_checked(a,b): ABI/version/toolchainpin vàtrườnghợpnull/overflow.'],
'AD59':['Universitysectionthamchiếucourse/timeslot/classroom; nhập ca FK/CHECK vi phạm đúng một invariant.','Enrollmenthai sections trùnggiờ: keykhôngbắtintervaloverlap, cần truyvấnnêuclash bằngfixtuređầy đủ.'],
'AD60':['Northwindcustomer0ordersvs2ordersvàunpaid: reportkhônglàm mấtzerochild, graincustomerđúng.','Companysupervisorcyclevàemployeeworkhours>limit: phânbiệtFKvới invariantgraph/aggregate.'],
'AD61':['edge={(a,b),(b,c)}: transitiveclosure iteration0,1,2 rồi nochange.','p(X):-node(X),notreach(a,X) cầnstratification; p(X):-notp(X) khôngcótínhđơnđiệu/naivefixpoint.'],
}
data=json.loads((O/'source-section-inventory.json').read_text(encoding='utf-8'))
keys={l['id']:l for l in base}
for l in base:
 l['oldPrereqs']=[x for x in l['before'] if not x.startswith('AD')];l['newPrereqs']=[x for x in l['before'] if x.startswith('AD')]
 l['focus']='; '.join(l['requiredDeepening']);l['algorithmProofTargets']=l.pop('requiredDeepening')
 l['exampleTargets']=examples.get(l['id'],[l['focus'],'Ca phản ví dụ dùng cùng mô hình, thay một giả định và nêu kết quả phải đổi.'])
 l['transferTargets']=['Tự giải một instance mới với ký hiệu/dữ liệu/ràng buộc đổi; phải nêu assumptions, intermediate states và kết luận.','Nếu hoạt động có code/query: chạy trên runner đúngengine; nếu proof/model: nộp lập luận/rubric. Output chuẩn bị không tính độc lập.']
 l['sectionIds']=[]
for u in data['bookSections']:
 sec=u['section'];matches=[]
 for n,l in enumerate(base):
  ps=[p for p in l['bookPrefixes'] if sec==p or sec.startswith(p+'.')]
  if ps:matches.append((max(p.count('.')*100+len(p) for p in ps),n,l['id']))
 if not matches:raise ValueError(sec)
 score,_,primary=max(matches)
 u['plannedAdvancedLessonIds']=[primary];u['depthVerdict']='authoring-assigned-not-semantic-complete';keys[primary]['sectionIds'].append(sec)
 u['baselineCreditAllowed']=False
 u['baselineCreditPolicy']='No blanket credit applied by this audit. Existing lesson evidence is locational only. Root may credit a specific reviewed paragraph/activity with exact line and reason.'
result={'date':'2026-11-05','scope':'Proposal after85 baseline lessons;61main lessons plus24children to prevent chapter-sized outlines. Titles/IDs need root adoption before authors edit child lessons.','lessons':base,'counts':{'lessons':len(base),'keyLessons':sum(l['key'] for l in base),'sourceUnits':len(data['bookSections']),'assignedUnits':sum(len(l['sectionIds']) for l in base)},'caution':'Every section has an authoring owner; this is NOT proof of semantic completeness. Root must match explanation/examples/exercise/answer and source algorithm/proof in final text. Some units are parent headings;744leaf units in the945 inventory.','sourceInventory':'source-section-inventory.json'}
(O/'proposed-lessons.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(O/'source-section-inventory.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result['counts']))
