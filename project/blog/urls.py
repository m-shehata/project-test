
from django.conf.urls import url
import views

urlpatterns = [
    url (r'^comments$',views.view_all_comments),
    url (r'^comments/new$',views.new_Comment),
    url(r'^category/(?P<slug>[^\.]+).html',views.view_cat_post, name='view_blog_categories'),
    url(r'^view/(?P<slug>[^\.]+).html',views.view_post,name='view_blog_post'),
    url(r'^posts.html$',views.view_all_post),

]

