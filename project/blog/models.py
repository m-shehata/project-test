from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

# Create your models here.

class Categories(models.Model):
	cat_name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	cat_date_pub = models.DateTimeField('date_pub')
	
	def __str__(self):
		return self.cat_name

	@permalink
	def get_absolute_url(self):
		return ('view_blog_categories', None, { 'slug': self.slug })


class Subscribe(models.Model):
	category= models.ForeignKey(Categories)
	curr_user = models.ForeignKey('auth.User')

class Posts(models.Model):
	post_title =models.CharField(max_length=200)
	slug=models.SlugField(max_length=200)
	post_body =models.TextField()
	image =models.ImageField()
	publish_date =models.DateTimeField('reg_date')
	approve =models.BooleanField()
	category=models.ForeignKey(Categories)


	def __str__(self):
		return self.post_title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, { 'slug': self.slug })

