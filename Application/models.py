from django.db import models
from datetime import datetime
# Create your models here.


class task_manager(models.Model):
    STATUS_CHOICE = [
        ('PAN' , 'pending'),
        ('COM' , 'complete'),
        ('REJ' , 'rejected')
    ]
    name = models.CharField(null=False)
    discription = models.TextField(null=False)
    status = models.CharField(choices=STATUS_CHOICE,default='Panding')
    date_time = models.DateTimeField(default=datetime.now)
