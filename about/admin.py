from django.contrib import admin
from .models import about_page
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(about_page)
class Aboutadmin(SummernoteModelAdmin):
    list_display= ( 'title', 'content', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('updated_on',)
    summernote_fields = ('content',)
def __str__(self):
    return("title: {self.title}")