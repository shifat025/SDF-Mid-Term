from django.db import models
from car_brand.models import Brand_Model
from django.contrib.auth.models import User

# Create your models here.
class Car_Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand_Model, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='', blank = True, null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
         return self.name

class Phurses(models.Model):
     buy  = models.ForeignKey(User, on_delete=models.CASCADE)
     buy_date = models.DateField(auto_now_add=True)
     cars = models.ForeignKey(Car_Model, on_delete=models.CASCADE)

class Comment(models.Model):
    car = models.ForeignKey(Car_Model, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    

    def __str__(self):
         return f"Comments by {self.car.name}" 

