from django.contrib import admin
from .models import Categories,Posts

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'cat_slug': ('cat_name',)}

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('post_title',)}

admin.site.register(Categories, CategoryAdmin)

admin.site.register(Posts,PostAdmin)