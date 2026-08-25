from django.shortcuts import get_object_or_404,redirect,render
from .models import Document,Conversation
from .services import extract_text,generate_summary,retrieve_context,answer_question

def home(request):
    return render(request,"home.html",{"documents":Document.objects.order_by("-created_at")})

def upload_document(request):
    if request.method!="POST": return redirect("home")
    f=request.FILES.get("document")
    if not f: return render(request,"home.html",{"error":"Please select a PDF file."})
    if not f.name.lower().endswith(".pdf"): return render(request,"home.html",{"error":"Only PDF files are supported."})
    doc=Document.objects.create(title=f.name,file=f)
    try:
        with doc.file.open("rb") as fh: doc.extracted_text=extract_text(fh)
        if not doc.extracted_text:
            doc.delete(); return render(request,"home.html",{"error":"No readable text found in this PDF."})
        doc.summary=generate_summary(doc.extracted_text); doc.save()
    except Exception as e:
        doc.delete(); return render(request,"home.html",{"error":f"Document processing failed: {e}"})
    return redirect("document_detail",document_id=doc.id)

def document_detail(request,document_id):
    doc=get_object_or_404(Document,id=document_id)
    return render(request,"document.html",{"document":doc,"conversations":doc.conversations.order_by("-created_at")})

def ask_question(request,document_id):
    doc=get_object_or_404(Document,id=document_id)
    if request.method=="POST":
        q=request.POST.get("question","").strip()
        if q:
            ctx=retrieve_context(doc.extracted_text,q)
            Conversation.objects.create(document=doc,question=q,answer=answer_question(ctx,q))
    return redirect("document_detail",document_id=doc.id)
