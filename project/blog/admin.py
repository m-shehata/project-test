from django.contrib import admin
from .models import Categories

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('cat_name',)}


admin.site.register(Categories, CategoryAdmin)