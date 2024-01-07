from django import forms
from .models import Brand_Model

class Brand_Form(forms.ModelForm):
    class Meta:
        model = Brand_Model
        fields = '__all__'