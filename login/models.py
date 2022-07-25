from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
 
    email = models.EmailField(max_length=100,unique=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images", null = True, blank=True)
    address = models.CharField(blank=True, max_length=300)
    city = models.CharField(max_length=30,blank=True)
    state = models.CharField(max_length=30,blank=True)
    pin = models.IntegerField(blank=True,default=0)
    role =(
        ('is_doctor','doctor' ),
        ('is_patient','patient')
        )
    roles = models.CharField(max_length=10, choices=role,default=is_doctor)

    USERNAME_FIELD ="email"
    REQUIRED_FIELDS = []



