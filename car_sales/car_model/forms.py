from django import forms
from .models import Car_Model, Comment

class car_model_form(forms.ModelForm):
    class Meta:
        model = Car_Model
        fields = '__all__'

class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']