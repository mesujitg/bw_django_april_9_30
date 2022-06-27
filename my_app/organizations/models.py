from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    status = models.BooleanField(default=True)


class Organization(models.Model):
    name = models.CharField(max_length=255)
    estd = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    details = models.TextField()
    status = models.BooleanField(default=True)
    logo = models.ImageField()

