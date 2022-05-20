from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryLevel = models.IntegerField()
    categoryParentID = models.IntegerField()
    
    def __str__(self):
        return self.categoryName
