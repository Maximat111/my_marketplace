from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=100)  # Назва товару
    description = models.TextField()  # Опис
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ціна
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)  # Відношення до моделі Category
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Фотографія товару
    created_at = models.DateTimeField(auto_now_add=True)  # Дата створення
    updated_at = models.DateTimeField(auto_now=True)  # Дата оновлення
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор оголошення
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # Номер телефону
    email = models.EmailField(null=True, blank=True)  # Email продавця

    def __str__(self):
        return self.title

