from datetime import date
TEXT={"vi":{"title":"Sổ học tập","save":"Lưu"},"en":{"title":"Study book","save":"Save"}}
def tr(lang,key):
    return TEXT.get(lang,{}).get(key,TEXT["en"].get(key,key))
def format_date(iso,lang):
    value=date.fromisoformat(iso)
    return value.strftime("%d/%m/%Y" if lang=="vi" else "%m/%d/%Y")
def format_number(value,lang):
    text=f"{value:,.2f}"
    return text.translate(str.maketrans({",":".",".":","})) if lang=="vi" else text
def apply_language(root,button,lang):
    root.title(tr(lang,"title")); button.configure(text=tr(lang,"save"))
