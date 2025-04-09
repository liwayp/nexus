from django.shortcuts import render

def contact_views(request):



    ctx = {

    }
    
    return render(request, 'blog.html', ctx)
