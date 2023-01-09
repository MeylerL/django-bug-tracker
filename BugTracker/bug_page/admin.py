from django.contrib import admin
from .models import TrackerUser, BugDetail

# Register your models here.
admin.site.register(TrackerUser)
admin.site.register(BugDetail)
