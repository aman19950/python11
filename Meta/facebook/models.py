from django.db import models

# Create your models here.


class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Age = models.IntegerField()
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
