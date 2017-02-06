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

class Comment_Section (models.Model):
	comment_descr=models.CharField(max_length=1000,default='no comment')
	comment_date=models.DateTimeField(auto_now=True)
	comment_usrname=models.CharField(max_length=100)
	comment_reply=models.CharField(max_length=2000)
	comment_post=models.ForeignKey(Posts)

	def check_comment (self):
		inappr_obj=Inappropriate_words.objects.all()
		temp=""
		lst=self.comment_descr.split()
		for word in lst:
			for inappr in inappr_obj:
				if word == inappr.inappr_wrd:
					word=len(word)*"*"
					break

			temp+=word
			temp+=" "
		self.comment_descr=temp
		self.save()



class Inappropriate_words(models.Model):
	inappr_wrd=models.CharField(max_length=200)
	def __str__(self):
		return self.inappr_wrd

