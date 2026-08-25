from django.contrib import admin
from django.urls import path
from documents import views

urlpatterns=[
 path("admin/",admin.site.urls), path("",views.home,name="home"),
 path("upload/",views.upload_document,name="upload"),
 path("document/<int:document_id>/",views.document_detail,name="document_detail"),
 path("document/<int:document_id>/ask/",views.ask_question,name="ask_question"),
]
