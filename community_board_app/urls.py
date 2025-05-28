from django.urls import path
from . import views
from .views import (
    IndexListView,
    PostListView, PostDetailView,
    CreatePostView, PostDeleteView,
    PostUpdateView, CommentDeleteView,
    CategoryListView, CategoryDetailView,
    CategoryDeleteView
)
app_name = 'community_board_app'

urlpatterns = [
    # path('', index, name='index'),
    path('', IndexListView.as_view(), name='index'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='delete_post'),
    path('edit/<slug:slug>/', PostUpdateView.as_view(), name='edit_post'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('delete/category/<slug:slug>/', CategoryDeleteView.as_view(), name='delete_category'),
]