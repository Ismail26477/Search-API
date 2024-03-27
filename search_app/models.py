from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    reference = models.URLField()
    image = models.ImageField(upload_to='images/', null=True, blank=True) 

    def __str__(self):
        return self.question