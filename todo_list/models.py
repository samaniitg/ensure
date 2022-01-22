from operator import truediv
from django.db import models

class Task(models.Model):
    """ Gym Model """
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Unsaved Name"
