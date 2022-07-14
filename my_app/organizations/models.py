from django.db import models
from django.utils import timezone
from accounts.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Organization(models.Model):
    name = models.CharField(max_length=255)
    estd = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    details = models.TextField()
    status = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='organizations')

    def __str__(self):
        return self.name


class OrgUser(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())
