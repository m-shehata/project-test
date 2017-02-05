from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from models import Posts,Categories




# def view_categories(request):
# 	all_cat = Categories.object.all()
# 	context = {'all_categories':all_cat}
# 	return render_to_response ('blog/category.html',context)



def cat_posts(request,slug):
	cat = get_object_or_404(Categories, cat_slug = slug)
	post = get_object_or_404(Posts, slug = slug)
	context = {'category':cat , 'post':post}
	return render_to_response ('blog/view_cat_post.html' , context)

def view_all_post(request):
	all_posts= Posts.objects.all()
	context ={'all_posts':all_posts}
	return render(request,'blog/posts.html',context)

def view_post(request,slug):
	post= Posts.objects.get(slug=slug)
	context = {'post':post}
	return render(request,'blog/posts.html',context)


