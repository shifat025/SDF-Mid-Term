from django.shortcuts import render
from car_model.models import Car_Model
from car_brand.models import Brand_Model

def home(request, brand_slug = None):
    data = Car_Model.objects.all()
    if brand_slug is not None:
        brands = Brand_Model.objects.get(slug = brand_slug)
        data = Car_Model.objects.filter(brand = brands)
    brand = Brand_Model.objects.all()
    return render(request, 'home.html', {'data': data, 'brands': brand})