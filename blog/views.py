from django.shortcuts import render,render_to_response,get_object_or_404
from models import Blog,Category

# Create your views here.
def index(request):
	categories = Category.objects.all()
	posts = Blog.objects.all() #[:5] latest 5 posts on the blog
	context = {'categories': categories,
	'posts': posts
	}
	return render(request,'index.html',context)

def view_post(request, slug):
	post = get_object_or_404(Blog,slug=slug)
	context = {'post': post}
	return render_to_response('view_post.html',context)

def view_category(request,slug):
	category = get_object_or_404(Category,slug=slug)
	posts = Blog.objects.filter(category=category)[:5]
	context = {'category':category,
	'posts':posts}
	return render_to_response('view_category.html',context)