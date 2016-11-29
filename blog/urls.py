from django.conf.urls import url

from blog import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.index, name='blog_index'),
    url(r'^post/(?P<post_id>\d+)/$', blog_views.read_post, name="blog_read_post"),
    url(r'^add/$', blog_views.create_post, name="blog_create_post"),
]
