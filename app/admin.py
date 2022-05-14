from django.contrib import admin
from matplotlib.pyplot import cla
from .models import Graph

# Register your models here.
class appAdmin(admin.ModelAdmin):
    list_display = ('name', 'Length')

admin.site.register(Graph, appAdmin)