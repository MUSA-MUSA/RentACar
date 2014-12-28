from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField
from django.core.urlresolvers import reverse
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    #user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    Username = models.CharField(max_length=60)
    Surname= models.CharField(max_length=60)
    Password = models.IntegerField(max_length=60)
    Date_of_Birth = models.IntegerField(max_length=30)
    Email = models.EmailField()
    Telephone = models.IntegerField(max_length=30)
    Address = models.CharField(max_length=50)
    Post_Code = models.IntegerField(blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Car(models.Model):
    Modele = models.CharField(max_length=255)
    Year = models.IntegerField(default=0)
    ADay = models.IntegerField(default=0)
    AWeek = models.IntegerField(default=0)
    AMounth = models.IntegerField(default=0)
    Company = models.CharField(max_length=255)
    Phone = models.IntegerField(default=0)
    Location = models.CharField(max_length=255)
    Notes = models.TextField(blank=True)
    #picture = models.ImageField(upload_to='profile_images', blank=True)


    def __unicode__(self):
        return self.Modele

class Question(models.Model):
        Username= models.CharField(max_length=255)
        Email = models.EmailField(default=0)
        Question = models.TextField(max_length=255)

        def __unicode__(self):
            return self.Username







