from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.

class Specialization(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)
    
    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
#one to many hole -->many part a foreigh key add kori .ekhane many part ta hlo available time

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="doctor/images/")
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)#one to many hole -->many part a foreigh key add kori
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    rating = models.CharField(max_length=20, choices = STAR_CHOICES)

    def __str__(self):
        return f"Patient : {self.reviewer.user.first_name}; Doctor : {self.doctor.user.first_name}"
    