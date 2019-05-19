from django.conf import settings
from django.db import models
from django.utils import timezone


#this is umported in views.py 
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Address(models.Model):
    addressline = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    description = models.TextField()

class Provider(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    PVaddress = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    


class Friend(models.Model):
    providers = models.ManyToManyField(Provider)
    EMPLOYMENT = 'EM'
    REFERRAL = 'RE'
    FRIENDSHIP_CHOICES = (
        (EMPLOYMENT, 'Employment'),
        (REFERRAL, 'Referral'),
    )
    friendship = models.CharField(
        max_length=2,
        choices=FRIENDSHIP_CHOICES,
        default=EMPLOYMENT,
    )






