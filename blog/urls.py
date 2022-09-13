from django.urls import path, reverse_lazy
from . import views
app_name ='blog'
urlpatterns =[
    path('', views.PostList.as_view(), name='post_list'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]