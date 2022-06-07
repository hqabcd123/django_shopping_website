from distutils.command.upload import upload
from django.db import models
import datetime


# Create your models here.

class discuss_borad:
    username = models.CharField(max_length=20)
    product_code = models.TextField()#link to save_code?
    post_date = models.DateTimeField(default=datetime.datetime.now(), help_text='create date: ')
    command = models.TextField()

    def __str__(self) -> str:
        return self.username + self.command

class Image_import(models.Model):
    Process_type = models.TextField()
    Image = models.ImageField(upload_to = 'Pre-Image')

    def __str__(self) -> str:
        str = 'import image path: '
        return str + self.Image
        

        
class diagram(models.Model):
    username = models.CharField(max_length=20)
    Save_code = models.TextField()
    create_date = models.DateTimeField(default=datetime.datetime.now(), help_text='create date: ')
    line = models.TextField()#Save as JSON
    circle = models.TextField()
    rectangle = models.TextField()
    offset = models.TextField()
    saved_image = models.ImageField(upload_to='upload/')

    def get_all_data(self) -> dict:
        #get all data but date and image because those can not converse to JSON data type
        dict = {
            'username': self.username,
            'Save_code': self.Save_code,
            'line': self.line,
            'circle': self.circle,
            'rectangle': self.rectangle,
            'offset': self.offset,}
        return dict
    
    def __str__(self) -> str:
        return 'username: ' + self.username + ' Save_code: ' + self.Save_code