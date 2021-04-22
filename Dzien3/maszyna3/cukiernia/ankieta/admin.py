from django.contrib import admin

# Register your models here.
from .models import Pytanie, Wybor

admin.site.register(Pytanie)
admin.site.register(Wybor)
