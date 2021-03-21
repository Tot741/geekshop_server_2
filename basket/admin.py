from django.contrib import admin

from basket.models import Basket
from authapp.models import UserProfile

admin.site.register(Basket)
admin.site.register(UserProfile)
