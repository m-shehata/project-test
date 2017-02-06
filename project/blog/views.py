from django.shortcuts import render,redirect
from django.shortcuts import render_to_response, get_object_or_404
from models import Posts,Categories,Comment_Section,Inappropriate_words
from .forms import Comment_Form 
from .forms import Post_Form 
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# def view_categories(request):
# 	all_cat = Categories.object.all()
# 	context = {'all_categories':all_cat}
# 	return render_to_response ('blog/category.html',context)



def view_cat_post(request,slug):
	cat = get_object_or_404(Categories, cat_slug = slug)
	post = get_object_or_404(Posts, slug = slug)
	context = {'category':cat , 'post':post}
	return render_to_response ('blog/view_cat_post.html' , context)

def view_all_post(request):
	all_posts= Posts.objects.all()
	paginator=Paginator(all_posts,3)
	page =request.GET.get('page')
	try:
		context =paginator.page(page)
	except PageNotAnInteger:
		context =paginator.page(1)
	except EmptyPage:
		context =paginator.page(paginator.num_pages)
	return render(request,'blog/posts.html',{'context':context})

def view_post(request,slug):
	post= Posts.objects.get(slug=slug)
	context = {'post':post}
	return render(request,'blog/posts.html',context)


def new_Comment(request):
	form = Comment_Form()
	if request.method == "POST":
		form = Comment_Form(request.POST)
		if form.is_valid():
			obj=form.save()
			obj.check_comment()
			return HttpResponseRedirect('/blog/comments')
	context={'com_form':form}
	return render(request, 'blog/newCommentForm.html', {'com_form':form})

def view_all_comments(request):
	return render(request,'blog/all_comments.html')


def view_edit_post(request,slug):
	post=get_object_or_404(Posts,slug=slug)
	#prepopulated_fields = {'slug':('post_title',)}
	if request.method == "POST":
		form=Post_Form(request.POST,instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			#post.auther=request.user
			post.publish_date=timezone.now()
			
			post.save()
			return redirect('view_top_post')
	form=Post_Form(instance=post)
	context={'post_form':form}
	return render(request,'blog/postform.html',context)


def view_new_post(request):
	if request.method == 'POST':
		form=Post_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('view_top_post')
	form=Post_Form()
	context={'post_form':form}
	return render(request,'blog/postform.html',context)


def view_delete_post(request,slug):
	post=Posts.objects.get(slug=slug)
	Comment_Section.objects.filter(comment_post=post.id).delete()
	post.delete()
	return redirect('view_top_post')



