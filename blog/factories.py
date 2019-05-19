from django.test import TestCase
from faker import Faker
import factory
from .models import Provider

class providerFactory(factory.Factory):
    class Meta:
        model = models.Provider

    firstName = factory.Faker('firstName')
    lastName = factory.Faker('lastName')

    
 	