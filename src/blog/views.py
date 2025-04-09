from django.shortcuts import render

def blog_views(request):



    ctx = {

    }
    
    return render(request, 'blog.html', ctx)
