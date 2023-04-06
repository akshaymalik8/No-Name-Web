from django.contrib import admin
from .models import blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ('content', 'title')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(blog, BlogAdmin)

# Register your models here.
