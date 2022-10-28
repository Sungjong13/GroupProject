from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomAdmin(admin.ModelAdmin):
    list_display = ["email", "nickname"]
    search_fields = ["email"]
    search_help_text = "찾으려는 이메일을 검색해주세요"


# Register your models here.
admin.site.register(User, CustomAdmin)
