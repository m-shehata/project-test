from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

# Create your models here.

class Posts(models.Model):
	post_title =models.CharField(max_length=200)
	slug=models.SlugField(max_length=200)
	post_body =models.TextField()
	image =models.ImageField()
	#category_id =models.ForeignKey(Category)
	publish_date =models.DateTimeField('reg_date')
	approve =models.BooleanField()


	def __str__(self):
		return self.post_title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, { 'slug': self.slug })



