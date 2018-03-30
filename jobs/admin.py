from django.contrib import admin

# Register your models here, only if you view this app on the Admin page

from .models import Job

admin.site.register(Job)
