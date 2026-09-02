from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment, PostImage
from blog.forms import CommentForm
from taggit.models import Tag
# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    tags = Tag.objects.all()
    context = {"posts" : posts,
                "tags": tags}
    return render(request, "blog/index.html", context)


def blog_list(request, tag_slug=None):
    posts = Post.objects.all().order_by('-created_on')
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    # Get all tags that exist in your system to display on the page
    blog_tags_list = Tag.objects.all()

    context = {
        "posts": posts,
        "active_tag": tag,  # Keeps track of the filtered tag
        "tags": blog_tags_list  # This ensures the template actually receives the tags!
    }
    return render(request, "blog/blogmain.html", context)

def blog_categories(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
        ).order_by('-created_on')
    context = {"posts":posts,
                "category":category}
    return render(request, "blog/category.html", context)


def blog_tags(request, tag_slug=None):
    posts = Post.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    context = {
        'posts': posts,
        'tag': tag
    }
    return render(request, 'blog/tag.html', context) 


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    tags = Tag.objects.all()
    images = PostImage.objects.filter(post=post)
    form = CommentForm()
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    
    comments = Comment.objects.filter(post=post)
    context = { "post":post,
                "tags": tags,
                "images": images,
                "comments":comments,
                "form":CommentForm(),
                }
    return render(request, "blog/detail.html", context)