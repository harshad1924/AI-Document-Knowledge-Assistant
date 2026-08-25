from django.db import models
class Document(models.Model):
    title=models.CharField(max_length=255)
    file=models.FileField(upload_to="documents/")
    extracted_text=models.TextField(blank=True)
    summary=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
class Conversation(models.Model):
    document=models.ForeignKey(Document,on_delete=models.CASCADE,related_name="conversations")
    question=models.TextField()
    answer=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
