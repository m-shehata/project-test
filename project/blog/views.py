from django.shortcuts import render
from models import Posts



# Create your views here.
def view_all_post(request):
	all_posts= Posts.objects.all()
	context ={'all_posts':all_posts}
	return render(request,'blog/posts.html',context)

def view_post(request,slug):
	post= Posts.objects.get(slug=slug)
	context = {'post':post}
	return render(request,'blog/posts.html',context)




