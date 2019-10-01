from django.contrib import admin
from .models import User, Test, Record, TestText

admin.site.register(User)
admin.site.register(Test)
admin.site.register(Record)
admin.site.register(TestText)
# Register your models here.
