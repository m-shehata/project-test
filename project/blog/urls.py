
from django.conf.urls import url
import views

urlpatterns = [
    
    url(r'^category/(?P<slug>[^\.]+).html',views.view_cat_post, name='view_blog_categories'),
    
]

