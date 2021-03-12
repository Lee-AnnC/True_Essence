from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

# def blog(request):
#    """ A view to return the blog page """

#    return render(request, 'blog/blog.html', {})


# class BlogView(ListView):
# model = Post
# template_name = 'blog/blog.html'
# ordering = ['-id']

class BlogView(View):
    def get(self, request, *args, **kwargs):
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            posts = Post.objects.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        else:
            posts = Post.objects.all()
            categories = Category.objects.all()
        context = {'posts': posts, 'categories': categories}

        return render(request, "blog/blog.html", context=context)


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


@method_decorator(login_required, name='dispatch')
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('BlogView')


class AddCategoryView(CreateView):
    model = Category
#   form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


@method_decorator(login_required, name='dispatch')
class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    context_object_name = 'post'
    # fields = ['title', 'title_tag', 'body']
    def form_valid(self, form):
        # save the form
        form.save()
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        if 'header_image' in self.request.FILES:
            #update the image if it was changed
            post.header_image = self.request.FILES['header_image']
            post.save()
        messages.success(self.request, 'Successfully updated blog!')
        return redirect(reverse("article-detail", args=[self.kwargs['pk']]))
    def get_success_url(self, **kwargs):
        return redirect(reverse("article-detail", args=[self.kwargs['pk']]))

@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('BlogView')
