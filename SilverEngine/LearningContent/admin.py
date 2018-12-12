from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.forms import TextInput

from django.forms import BaseInlineFormSet

# Register your models here.
admin.site.register(Definition)
admin.site.register(Tag)