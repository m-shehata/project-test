from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
    	return '%s' % self.title

    @permalink
    def get_absolute_url(self):
    	return ('view_blog_category',None,{'slug':self.slug})


class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('blog.Category')
	
	def __unicode__(self):
		return '%s' % self.title
	
	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, { 'slug': self.slug })


class Comment(models.Model):
	#related name 3shan t3rf tgeb el comments bta3t ay blog beshola b=Blog.objects.get(id=1) b.comments_set.all()
	#b.comments_set is a Manager that returns QuerySets which can be filtered and manipulated.
	#check link https://docs.djangoproject.com/en/1.10/topics/db/queries/#backwards-related-objects
	blog = models.ForeignKey('blog.Blog', related_name='comments')
	author = models.CharField(max_length=100)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __unicode__(self):
		return self.text
