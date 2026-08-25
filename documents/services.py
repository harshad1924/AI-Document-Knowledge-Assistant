import os,re
from PyPDF2 import PdfReader

def extract_text(file_obj):
    return "\n".join((p.extract_text() or "") for p in PdfReader(file_obj).pages).strip()

def retrieve_context(text,question,max_chars=9000):
    words=[x.lower() for x in re.findall(r"[A-Za-z]{3,}",question)]
    paragraphs=[p.strip() for p in re.split(r"\n\s*\n",text) if p.strip()]
    scored=[(sum(p.lower().count(x) for x in words),p) for p in paragraphs]
    scored=[x for x in scored if x[0]>0]
    scored.sort(key=lambda x:x[0],reverse=True)
    selected=[p for _,p in scored[:8]] or paragraphs[:5]
    return "\n\n".join(selected)[:max_chars]

def ask_gemini(prompt):
    key=os.getenv("GEMINI_API_KEY","")
    if not key: return None
    import google.generativeai as genai
    genai.configure(api_key=key)
    model=genai.GenerativeModel("gemini-3.6-flash")
    return model.generate_content(prompt).text

def generate_summary(text):
    prompt=("You are a document analysis assistant. Summarize this document professionally. "
            "Include main topic, key points, important facts and action items if present.\n\nDOCUMENT:\n"
            + text[:12000])
    result=ask_gemini(prompt)
    return result or ("DEMO MODE: GEMINI_API_KEY is not configured. The PDF was uploaded and "
                      "text extraction succeeded. Add the API key for a live AI summary.")

def answer_question(context,question):
    prompt=("You are an AI document assistant. Answer using ONLY the supplied document context. "
            "If the answer is not present, say the document does not contain enough information.\n\n"
            "DOCUMENT CONTEXT:\n"+context+"\n\nQUESTION:\n"+question)
    result=ask_gemini(prompt)
    return result or ("DEMO MODE: GEMINI_API_KEY is not configured. Relevant context was retrieved. "
                      "Add the API key for a live AI answer.")
