from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=10, unique=True)
    address = models.TextField(default='')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=99999999.99, max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='uploads/', default='uploads/default.jpg', blank=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_insert = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer=models.ForeignKey(Client, on_delete=models.CASCADE)
    products=models.ManyToManyField(Product) 
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    date_ordered=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order price: {self.total_price}, products: {self.products}, date: {self.date_ordered}'
    
    def get_all_products(self):
        pass
