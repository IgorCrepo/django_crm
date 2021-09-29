from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True,on_delete = models.CASCADE)
    name = models.CharField("imię", max_length = 200, null = True)
    phone = models.CharField("telefon", max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(default ="profile1.png", null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
            ('Systemy ochrony', 'Systemy ochrony'),
            ('Biuro', 'Biuro'),
            )

    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
    description = models.CharField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
            ('Oczekujące', 'Oczekujące'),
            ('Wysłane', 'Wysłane'),
            ('Dostarczone', 'Dostarczone'),
            )

    customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL) #customer to rodzić ordera, SET_NULL - gdy skasujemy rodzica, to order nadal będzie w DB
    product = models.ForeignKey(Product, null = True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    status = models.CharField(max_length = 200, null = True, choices = STATUS)
    note = models.CharField(max_length = 1000, null = True)

    def __str__(self):
        #return "{} zamówił {} - status: {}".format(self.customer.name, self.product.name, self.status)
        return self.product.name
