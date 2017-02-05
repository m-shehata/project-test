from django.contrib import admin
from .models import Posts

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('post_title',)}

admin.site.register(Posts,PostAdmin)





