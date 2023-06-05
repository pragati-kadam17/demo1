from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User


""" class User(AbstractBaseUser):
   
    is_lab_head = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
 """
    
    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Test(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name 

class LabTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    #price = models.DecimalField(max_digits=8, decimal_places=2)   # Add the price field
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    

    def __str__(self):
        return f"Test: {self.test.name}, Test ID: {self.test.id}, Price: {self.price}, Date: {self.date}"


class LabHeadSignup(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class PatientSignup(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username








        

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True, default='default_username')

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_lab_head = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()





