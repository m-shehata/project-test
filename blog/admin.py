from django.contrib import admin
from models import Blog,Category,Comment


#Custom models here
class BlogAdmin(admin.ModelAdmin):
	list_display = ['title','category']
	exclude = ['posted']
	prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment)