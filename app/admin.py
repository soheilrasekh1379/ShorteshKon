from django.contrib import admin
from .models import shortUrl,realUrl
# Register your models here.

admin.site.register(shortUrl)
admin.site.register(realUrl)
