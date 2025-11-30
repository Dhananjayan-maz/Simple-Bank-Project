from django.contrib import admin

from .models import UserDetails,transaction_model

admin.site.register(UserDetails)
admin.site.register(transaction_model)