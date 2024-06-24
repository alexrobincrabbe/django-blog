from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class Postlist(generic.ListView):
    queryset = Post.objects.filter(author=4)
    template_name = "post_list.html "