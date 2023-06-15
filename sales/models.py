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
    
class Category(models.Model):   
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
    name = models.CharField(max_length=32, choices=CATEGORY, null=True)

    def __str__(self):
        return self.name

class Sales(models.Model):
    name = models.CharField(max_length=200, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    percentage = models.PositiveIntegerField(validators=PERCENTAGE_VALIDATOR)

    def __str__(self):
        return self.name
    
class Product(models.Model):       
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    sales = models.ForeignKey(Sales, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name    
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def discounted_price(self):
        if self.sales:
            discount = self.price * self.sales.percentage / 100
            return self.price - discount
        else:
            return self.price
    

    
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
    



