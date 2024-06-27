from django.shortcuts import render, get_object_or_404
from .models import about_page
# Create your views here.

def display_about(request):
    about = about_page.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about":about}
    )

