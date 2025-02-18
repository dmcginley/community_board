from django.urls import path
from . import views
from .views import (
    PostFeedView, PostDetailView,
    CreatePostView, PostDeleteView,
    PostUpdateView, CommentDeleteView
)
app_name = 'community_board_app'

urlpatterns = [
    # path('', index, name='index'),
    path('', PostFeedView.as_view(), name='post_feed'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='delete_post'),
    path('edit/<slug:slug>/', PostUpdateView.as_view(), name='edit_post'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

]