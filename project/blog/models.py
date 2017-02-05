from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

# Create your models here.

class Categories(models.Model):
	cat_name = models.CharField(max_length=200)
	cat_slug = models.SlugField(max_length=200)
	cat_date_pub = models.DateTimeField('date_pub')
	
	
	def __str__(self):
		return self.cat_name


	@permalink
	def get_absolute_url(self):
		return ('view_blog_categories', None, { 'slug': self.cat_slug })


class Subscribe(models.Model):
	cat_id = models.ForeignKey(Categories)
	#user_id = models.ForeignKey('auth.User')