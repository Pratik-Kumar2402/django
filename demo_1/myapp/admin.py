from django.contrib import admin
from .models import Customers
from .models import *

admin.site.register(Customers)
admin.site.register(Blogpost)
admin.site.register(Section)
admin.site.register(Faculty)
admin.site.register(Signup)
admin.site.register(CookieDetails)
