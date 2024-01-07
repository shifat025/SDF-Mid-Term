from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_brand(request):
    if request.method == 'POST':
        brand_form = forms.Brand_Form(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            return redirect('add_brand')
        
    else:
        brand_form = forms.Brand_Form()
    return render(request,'brand.html',{'form': brand_form})


