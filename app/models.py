from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django import forms
from django.forms import ModelForm
import datetime
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# Create your models here.

#------------------------------product page models space---------------------------------------------#
class product_code(models.Model):
    product_code = models.TextField(unique=True)

    def __str__(self) -> str:
        return self.product_code

class product_type(models.Model):
    product_type = models.TextField()

    def __str__(self) -> str:
        return 'product type: ' + self.product_type

class set_of_product_type(models.Model):
    product_code = models.ForeignKey(product_code, on_delete=models.CASCADE, default=False)
    set_of_product_type = models.ForeignKey(product_type, on_delete=models.CASCADE, default=False)

    def __str__(self) -> str:
        return 'the type of ' + self.product_code.product_code + 'is ' + str(self.set_of_product_type)

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
    set_of_product_type = models.ForeignKey(set_of_product_type, on_delete=models.CASCADE, default=False)

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
        return self.product_name + ': ' + self.User_command.command

    class Meta:
        permissions = (
            ('can_add', 'add'),
        )

#------------------------------models forms space---------------------------------------------------#
class add_product_form(forms.Form):
    Type = [
        ('shoes', 'shoes'),
        ('range', 'range'),
        ('shirt', 'shirt'),
        ('pants', 'pants'),
    ]
    product_name = forms.CharField()
    Product_delta = forms.CharField(widget=forms.Textarea())
    product_type = forms.CharField(widget=forms.Select(choices=Type))
    Product_image = forms.FileField()

#------------------------------product page models space---------------------------------------------#

#------------------------------user models space---------------------------------------------#

class user_history(models.Model):
    foodprint = models.ForeignKey(product_borad, on_delete=models.CASCADE, default=False)

class user_history_set(models.Model):
    foodprint_set = models.ForeignKey(user_history, on_delete=models.CASCADE, default=False)

    def __str__(self) -> str:
        return str(self.foodprint_set.foodprint)

class User_Manager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        self.is_admin = True
        user.save(using=self._db)
        return user

def set_default_profile_image():
    return 'hio01.png'

def get_upload__profile_image_path(self, filename):
    return 'profile_images/{}/'.format(self.pk)

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    history = models.ForeignKey(user_history_set,
        on_delete=models.CASCADE,
        default=False,
        blank=True,
        null=True,
        )
    hide_email = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to=get_upload__profile_image_path, default=set_default_profile_image)

    objects = User_Manager()

    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/{}/'.format(self.pk)):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

#--------------------------------------------------------------------------------------------#



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