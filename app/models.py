from django.db import models
import datetime

# Create your models here.
class diagram(models.Model):
    username = models.CharField(max_length=20)
    create_date = models.DateTimeField(default=datetime.datetime.now(), help_text='create date: ')
    line = models.TextField()#Save as JSON
    circle = models.TextField()
    rectangle = models.TextField()
    offset = models.TextField()

    def __str__(self):
        return 'username: ' + self.username