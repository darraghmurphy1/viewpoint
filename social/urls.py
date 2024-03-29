from . import views
from django.urls import path

urlpatterns = [

    # url for homepage
    path('', views.PostList.as_view(), name='home'),
    # url for a more detailed view of a post
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # url to post form
    path('user_post', views.UserPostView.as_view(), name='user_post'),
    # url for edit form
    path('edit_post/<int:id>/', views.PostEditView.as_view(), name='edit_post'),
    # url for delete form
    path('delete_post/<int:id>/', views.PostDeleteView.as_view(), name='delete_post'),


]
