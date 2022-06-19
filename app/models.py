from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django import forms
from django.forms import ModelForm
import datetime


# Create your models here.
#------------------------------product page models space---------------------------------------------#
class product_code(models.Model):
    product_code = models.TextField()

    def __str__(self) -> str:
        return self.product_code

class product_type(models.Model):
    product_code = models.ForeignKey(product_code, on_delete=models.CASCADE, default=False)
    product_type = models.TextField()

    def __str__(self) -> str:
        return 'the type of ' + self.product_code.product_code + 'is ' + self.product_type

class product_images_album(models.Model):
    product_code = models.ForeignKey(product_code, on_delete=models.CASCADE, default=False)
    def default(self):
        return self.images_filter(default=True).first()

    def __str__(self) -> str:
        return self.product_code.product_code

class product_image(models.Model):
    product_code = models.ForeignKey(product_code, on_delete=models.CASCADE, default=False)
    DIR = 'Product_images'
    main_image = models.BooleanField()
    Product_image = models.ImageField(upload_to = DIR)
    album = models.ForeignKey(product_images_album, related_name='images', on_delete=models.CASCADE, default=False)

    def __str__(self) -> str:
        return self.product_code.product_code

class discuss_borad(models.Model):#which is being to write command on the product page
    username = models.CharField(default=' ', max_length=20)
    product_code = models.ForeignKey(product_code, on_delete=models.CASCADE, default=False)
    post_date = models.DateTimeField(default=datetime.datetime.now(), help_text='create date: ')
    command = models.TextField(default=' ')

    def __str__(self) -> str:
        return self.username + ' ' + self.command

class product_borad(models.Model):#Whole product's big picture
    product_name = models.TextField()
    product_code = models.ForeignKey(product_code, on_delete=models.CASCADE, default=False)
    Create_Date = models.DateTimeField(default=datetime.datetime.now(), help_text='create date: ')
    Product_delta = models.TextField()
    Product_image = models.ForeignKey(product_images_album, related_name='image', on_delete=models.CASCADE, default=False)
    User_command = models.ForeignKey(discuss_borad, related_name='user', on_delete=models.CASCADE, default=False)

    def get_all_data(self) -> dict:
        dict = {
            'product_name': self.product_name,
            'Create_Date': self.Create_Date,
            'Product_delta': self.Product_delta,
            'Product_image': self.Product_image,
            'User_command': self.User_command,
        }
        return dict

    def __str__(self) -> str:
        return self.User_command.username + ': ' + self.User_command.command

    class Meta:
        permissions = (
            ('can_add', 'add'),
        )

#------------------------------models forms space---------------------------------------------------#
class add_product_form(forms.Form):
    product_name = forms.CharField()
    Product_delta = forms.CharField(widget=forms.Textarea())
    Product_image = forms.FileField()

#------------------------------product page models space---------------------------------------------#

class image_album(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

class Image_import(models.Model):
    Process_type = models.TextField()
    Image = models.ImageField(upload_to = 'Pre-Image')
    album = models.ForeignKey(image_album, related_name='images', on_delete=models.CASCADE, default=False)

    def __str__(self) -> str:
        str = 'import image path: '
        return str + self.Process_type
        

        
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
        dict = [{
            'username': self.username,
            'Save_code': self.Save_code,
            'line': self.line,
            'circle': self.circle,
            'rectangle': self.rectangle,
            'offset': self.offset,}]
        return dict[0]
    
    def __str__(self) -> str:
        return 'username: ' + self.username + ' Save_code: ' + self.Save_code