from django.contrib import admin
from .models import img
# Register your models here.
@admin.register(img)
class admis(admin.ModelAdmin):
    list_display=['id','photo','date']
