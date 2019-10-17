from django.contrib import admin
from .models import User, Record, TestText

admin.site.register(User)
admin.site.register(Record)
admin.site.register(TestText)
# Register your models here.
