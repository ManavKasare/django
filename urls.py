from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from accounts.models import Post


urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^dashboard/$', ListView.as_view(queryset=Post.objects.all().order_by('-created_on'),
    template_name='dashboard/dashboard.html', context_object_name = "posts")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'dashboard/dashboard.html')),
]


