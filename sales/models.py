from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY = [
       ("BIO", "Bio et écologie"),
       ("FRUITS_ET_LEGUMES", "Fruits et légumes"),
       ("VIANDE_ET_POISSON", "Viande et poisson"),
       ("PAIN_ET_PATISSERIE", "Pain et pâtisseries"),
       ("FRAIS", "Produits frais"),
       ("SURGELE", "Surgelés"),
       ("BOISSONS", "Boissons"),
       ("EPICERIE_SALEE", "Epicerie salée"),
       ("EPICERIE_SUCREE", "Epicerie sucrée"),
       ("PRODUITS_DU_MONDE", "Produits du monde"),
   ]
   
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    price = models.FloatField()
    category = models.CharField(
       max_length=32,
       choices=CATEGORY,
       null=True
   )

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adress
    
class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    percentage = models.DecimalField(max_digits=3, decimal_places=0, validators=PERCENTAGE_VALIDATOR)



