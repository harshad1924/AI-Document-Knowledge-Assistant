from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[
      migrations.CreateModel(name="Document",fields=[
       ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
       ("title",models.CharField(max_length=255)),("file",models.FileField(upload_to="documents/")),
       ("extracted_text",models.TextField(blank=True)),("summary",models.TextField(blank=True)),
       ("created_at",models.DateTimeField(auto_now_add=True))]),
      migrations.CreateModel(name="Conversation",fields=[
       ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
       ("question",models.TextField()),("answer",models.TextField()),("created_at",models.DateTimeField(auto_now_add=True)),
       ("document",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="conversations",to="documents.document"))])
    ]
