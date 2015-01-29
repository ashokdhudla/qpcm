from django.db import models

import os
from django.contrib import admin
# Create your models here.

class card(models.Model):
    cardid = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    class Admin:
        pass
    def __str__(self):
        return '%s' %(self.cardid)

    
