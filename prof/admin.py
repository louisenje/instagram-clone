from django.contrib import admin
from PIL import Image
from .models import Profile,Image

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)