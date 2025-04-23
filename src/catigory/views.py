from django.shortcuts import render, redirect
from .forms import RegionForm
from .models import Region


def region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('region')

    else:
        form = RegionForm()
    
    ctx = {
        'form': form
    }

    return render(request, 'region.html', ctx)

