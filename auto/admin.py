from django.contrib import admin

# Register your models here.

from .models import Article, ContactForm

admin.site.register(Article)
admin.site.register(ContactForm)