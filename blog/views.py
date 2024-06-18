from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
paginate_by = 6

def post_detail(request, slug):

 queryset = Post.objects.filter(status=1)
 post = get_object_or_404(queryset, slug=slug)

      return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "coder": "Kash Hussain"},
    )
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )    