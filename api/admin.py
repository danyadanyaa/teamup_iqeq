from django.contrib import admin

from api.models import Test


@admin.register(Test)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'login']

