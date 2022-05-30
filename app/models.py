from django.db import models

# Create your models here.
class diagram(models.Model):
    type = models.CharField(max_length=20)
    point = models.TextField()#Save as JSON

    def __str__(self):
        return self.type