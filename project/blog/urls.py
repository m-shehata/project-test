
from django.conf.urls import url
import views

urlpatterns = [
    url (r'^comments$',views.view_all_comments),
    url (r'^comments/new$',views.new_Comment),
    url(r'^category/(?P<slug>[^\.]+).html',views.view_cat_post, name='view_blog_categories'),
    url(r'^view/(?P<slug>[^\.]+).html',views.view_post,name='view_blog_post'),
    url(r'^posts.html$',views.view_all_post,name='view_top_post'),
    url(r'^post/(?P<slug>[^\.]+)/edit$',views.view_edit_post,name='view_edit_post'),
    url(r'^post/new$',views.view_new_post,name='view_new_post'),
    url(r'^post/(?P<slug>[^\.]+)/delete$',views.view_delete_post,name='view_delete_post'),

]

