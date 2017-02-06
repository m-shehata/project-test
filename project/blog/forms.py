from django import forms
from .models import Comment_Section ,Posts

class Comment_Form(forms.ModelForm):
	class Meta:
		model=Comment_Section
		fields=('comment_descr','comment_usrname','comment_reply','comment_post',)



class Post_Form(forms.ModelForm):
	class Meta:
		model=Posts
		fields=('post_title','slug','post_body','image','approve','category',)