from django.contrib import admin
from .models import userData

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')
    search_filter = ('title', 'content')
    # prepopulated_fields = {'slug':('title',)}

admin.site.register(userData, UserAdmin)


# Register your models here.
