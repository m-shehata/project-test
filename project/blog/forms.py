from django import forms
from .models import Comment_Section

class Comment_Form(forms.ModelForm):
	class Meta:
		model=Comment_Section
		fields=('comment_descr','comment_usrname','comment_reply','comment_post',)