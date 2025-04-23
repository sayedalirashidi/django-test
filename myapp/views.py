from django.shortcuts import render
from .models import blog

def myapp(request):
    myapp_blog = blog.objects.all()
    return render(request, 'myapp/index.html', {'myapp_blog':myapp_blog} )
