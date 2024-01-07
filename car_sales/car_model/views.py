from django.shortcuts import render,redirect
from . import forms
from . import models
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# Create your views here.

def add_car(request):
    if request.method == 'POST':
        car_form = forms.car_model_form(request.POST)
        if car_form.is_valid():
            car_form.save()
            return redirect('add_car')
        
    else:
        car_form = forms.car_model_form()
    return render(request,'car.html',{'form': car_form})

class DetailPostView(DetailView):
    model = models.Car_Model
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.Comment_form(data=self.request.POST)
        car_model = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car_model
            new_comment.user = self.request.user 
            new_comment.save()
        return self.get(request, *args, **kwargs)
      
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_model = self.object
        comments = car_model.comment_set.all()
        comment_form = forms.Comment_form()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

def buynow(request, id):
    data = models.Car_Model.objects.get(pk=id)
    quntity = data.quantity
    if quntity > 1:
        quntity -=1
        data.quantity = quntity
        data.save()
        models.Phurses.objects.create(buy=request.user, cars =data)
        return redirect('profile')
    return render(request,'post_details.html', {'car_model': data})
