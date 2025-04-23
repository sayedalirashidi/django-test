from django.shortcuts import render
from .models import blog

def blog_index(request):
    data = blog.objects.all()  # مدل های بلاگ رو برمیگردونیم
    return render(request, 'blog/blog.html', {'data': data})