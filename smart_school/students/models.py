from django.db import models
import random

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    reg_num = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    email = models.EmailField(unique=True)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reg_num:  # Assign reg_num if not set
            while True:
                random_reg = random.randint(10000000, 99999999)  
                if not Student.objects.filter(reg_num=random_reg).exists():
                    self.reg_num = random_reg
                    break
        super().save(*args, **kwargs)

    def __str__(self): 
        return f"{self.reg_num} - {self.fname} {self.lname}"




