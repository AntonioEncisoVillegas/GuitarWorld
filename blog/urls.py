from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListviews.as_view(), name='blog-home'),
    path('post/<intpk>', PostListviews.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
] 

#