from django.contrib import admin
from .models import Mosque, User

class MosqueAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longtitude')


class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'telegram_id')


admin.site.register(User, UserAdmin)
admin.site.register(Mosque, MosqueAdmin)