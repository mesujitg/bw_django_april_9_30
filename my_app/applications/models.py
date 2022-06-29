from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from jobs.models import Job


class Application(models.Model):
    apply_date = models.DateField(default=datetime.now())
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=255,
                              choices=[('applied', 'applied'),
                                       ('reviewing', 'reviewing'),
                                       ('selected', 'selected'),
                                       ('rejected', 'rejected'),
                                       ('waiting', 'waiting')])

    def __str__(self):
        return f'{ self.user_id } - { self.job_id }'
