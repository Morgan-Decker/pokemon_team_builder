from django.contrib import admin

# Register your models here.
from builder.models import UserProfile

admin.site.register(UserProfile)
