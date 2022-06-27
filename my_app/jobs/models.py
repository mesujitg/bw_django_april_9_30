from django.db import models
from organizations.models import Organization, Category


class Job(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255,
                            choices=[('Full Time', 'Full Time'),
                                     ('Part Time', 'Part Time')])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.CharField(max_length=255)
    description = models.TextField()
    requirement = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    responsibilities = models.TextField()
    no_of_vacancy = models.IntegerField()
    salary = models.FloatField()
    deadline = models.DateField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
