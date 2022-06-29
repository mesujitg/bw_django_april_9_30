from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Information(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    details = models.TextField()
    status = models.BooleanField(default='True')

    def __str__(self):
        return self.title
