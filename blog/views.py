from django.shortcuts import render
from django.views.generic import View, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy

# def blog(request):
#    """ A view to return the blog page """

#    return render(request, 'blog/blog.html', {})


#class BlogView(ListView):
    #model = Post
    #template_name = 'blog/blog.html'
    #ordering = ['-id']

class BlogView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        categories = Category.objects.all()
        context = {'posts': posts, 'categories': categories}
        return render(request, "blog/blog.html", context=context)


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    fields = '__all__'

    success_url = reverse_lazy('BlogView')


class AddCategoryView(CreateView):
    model = Category
#   form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('BlogView')
