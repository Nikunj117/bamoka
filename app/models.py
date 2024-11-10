from django.db import models
from django.contrib.auth.models import User
from .mail import SendWelcomMail
from django.utils.text import slugify

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Gettouch(TimeStampModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField(null=True)

class contactus(TimeStampModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True)
    comments = models.TextField(null=True)
    privacy_policy_accepted = models.BooleanField(default=False)  

class UserMail(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email
    
    # def save(self, args, *kwargs):
    #     SendWelcomMail(self.email)
    #     super(UserMail, self).save(*args, **kwargs)
