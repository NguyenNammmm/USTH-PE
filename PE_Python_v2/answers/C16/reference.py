from datetime import datetime,timedelta
import re
def due_date(text,days):
    return (datetime.strptime(text,"%Y-%m-%d")+timedelta(days=days)).strftime("%Y-%m-%d")
def extract_id(text):
    match=re.search(r"\bS\d{3}\b",text)
    return match.group(0) if match else None
def clean_spaces(text):
    return re.sub(r"\s+"," ",text).strip()
