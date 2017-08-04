from django.contrib import admin
from .models import Post

# Register your models here.
# Allow it to show up in the admin interface
admin.site.register(Post)