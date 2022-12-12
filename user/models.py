from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email',
                              max_length=100, unique=True)
    password = models.CharField(max_length=8)

    def __str__(self):
        return "%i %s " % (self.id, self.name)
