from django.contrib import admin
from .models import (Blog,BlogComment,BlogTag)

admin.site.register((Blog,BlogTag,BlogComment))