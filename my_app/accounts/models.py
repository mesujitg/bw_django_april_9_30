from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class User(AbstractUser):
    mobile = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=20,
                            choices=[('Employer', 'Employer'),
                                     ('Recruiter', 'Recruiter'),
                                     ('Employee', 'Employee')], default='Employer')

