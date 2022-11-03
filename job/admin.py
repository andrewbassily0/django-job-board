from django.contrib import admin

# Register your models here.

from .models import Job
from .models import blog

admin.site.register(Job)
admin.site.register(blog)

