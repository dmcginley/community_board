from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import (
    DetailView, ListView,
    CreateView, DeleteView,
    UpdateView, 
)
from .models import Post, Comment, Category, SiteDescription

from django.shortcuts import get_object_or_404
from django.db.models import Count, Prefetch
from cms_app.models import HeroSettings
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.template.loader import render_to_string

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    return render(request, 'community_board_app/index.html')

class IndexListView(ListView):
    model = Category
    template_name = 'community_board_app/index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        # Prefetch posts related to each category with status 'PUBLISHED' and annotated with comment count
        return Category.objects.prefetch_related(
            Prefetch(
                'posts',
                queryset=Post.objects.filter(status=Post.PUBLISHED).annotate(comment_count=Count('comments'))
            )
        ).all()

    def get_context_data(self, **kwargs):
        # Get the context data, which includes categories by default
        context = super().get_context_data(**kwargs)
        
        # Optionally add hero settings if needed
        context['hero_settings'] = HeroSettings.objects.first()  # Assuming only one object exists
        context['site'] = SiteDescription.objects.first()  # Fetch the single instance
        return context

class PostListView(ListView):
    model = Post
    template_name = 'community_board_app/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count('comments'))  # Ensure queryset includes comment count

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.annotate(comment_count=Count('comments'))
        context['categories'] = Category.objects.all()
        context['hero_settings'] = get_object_or_404(HeroSettings, pk=1)
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('Hx-Request'):  # HTMX request
            posts = self.get_queryset()
            html = render_to_string("community_board_app/partials/post_partial.html", {"posts": posts})  # Pass as a list
            return HttpResponse(html)

        return super().get(request, *args, **kwargs)


class CreatePostView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'community_board_app/post_form.html'  # Template for the form
    success_url = reverse_lazy('community_board_app:post_list')  # Redirect after success

    def test_func(self):
        user = self.request.user
        return user.is_authenticated or user.is_staff or user.is_superuser  # Allow if logged in OR is staff/superuser
    
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
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    template_name = 'community_board_app/delete_post.html'
    success_url = reverse_lazy('community_board_app:post_list')

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



class CategoryListView(ListView):
    model = Category
    template_name = 'community_board_app/category_list.html'  # Specify your template
    context_object_name = 'categories'  # The variable name in the template
    ordering = ['name']  # Optional: Order categories alphabetically


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'community_board_app/category_detail.html'
    context_object_name = 'category'

    def get_object(self):
        return get_object_or_404(Category, slug=self.kwargs['slug'])




class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'community_board_app/delete_category.html'
    success_url = reverse_lazy('community_board_app:category_list')  # Redirect to the category list after deletion

    def test_func(self):
        category = self.get_object()
        # Allow only superusers or staff to delete categories
        return self.request.user.is_superuser or self.request.user.is_staff
    
    def post(self, request, *args, **kwargs):
        # Get the category object
        category = self.get_object()
        # Delete the category
        category.delete()
        # Redirect to the success URL (category list)
        return redirect(self.success_url)
