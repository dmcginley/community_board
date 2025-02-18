from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import (
    DetailView, ListView,
    CreateView, DeleteView,
    UpdateView,
)

from django.db.models import Count
from .models import Post, Comment
from cms_app.models import HeroSettings
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, 'community_board_app/index.html')


class PostFeedView(ListView):
    model = Post
    template_name = 'community_board_app/post_feed.html'
    context_object_name = 'posts'  # Ensures we use `posts` in the template
    ordering = ['-created_at']  # Orders posts by latest first

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count('comments'))  # Annotate each post with comment count

    def get_context_data(self, **kwargs):
        # Get the context from the parent class
        context = super().get_context_data(**kwargs)

        # Get the HeroSettings instance
        hero_settings = HeroSettings.objects.get(pk=1)

        # Add `hero_settings` to the context
        context['hero_settings'] = hero_settings

        return context


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'community_board_app/post_form.html'  # Template for the form
    success_url = reverse_lazy('community_board_app:post_feed')  # Redirect after success

    def form_valid(self, form):
        form.instance.author = self.request.user  # Assign the logged-in user
        self.object = form.save()
        return redirect('community_board_app:post_detail', slug=self.object.slug)  # Redirect to post detail
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'community_board_app/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['form'] = CommentForm()
        context['comments'] = post.comments.all()  # Retrieve all comments related to the post
        return context

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count('comments'))

    def post(self, request, *args, **kwargs):
        post = self.get_object()  # Get the current post
        form = CommentForm(request.POST)
        if form.is_valid():
            # Save the comment, but don't commit it to the DB yet
            comment = form.save(commit=False)
            comment.post = post  # Link the comment to the current post
            comment.author = request.user  # Set the comment author to the current user
            comment.save()  # Now save the comment
            return redirect('community_board_app:post_detail', slug=post.slug)  # Redirect to the post's detail page

        # If the form is not valid, render the same template with errors
        return self.get(request, *args, **kwargs)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'community_board_app/edit_post.html'
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    # def form_valid(self, form):
    #     messages.success(self.request, 'Post updated successfully')
    #     return super().form_valid(form)




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    template_name = 'community_board_app/delete_post.html'
    success_url = reverse_lazy('community_board_app:post_feed')

    def test_func(self):
        post = self.get_object()
        # if self.request.user == post.author:
        if self.request.user == post.author or self.request.user.is_superuser:

            return True
        return False
    
    def post(self, request, *args, **kwargs):
        # Get the post object
        post = self.get_object()
        # Delete the post
        post.delete()
        # Redirect to the success URL
        return redirect(self.success_url)
    

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'community_board_app/delete_comment.html'
    
    def get_success_url(self):
        return reverse_lazy('community_board_app:post_detail', kwargs={'slug': self.object.post.slug})
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_staff
