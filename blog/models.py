from django.db import models
from django.urls import reverse
from django.utils import safestring
from taggit.managers import TaggableManager

# Create your models here.
"""Models are how Django accesses, manages, 
and stores data through Python objects. (Django)
Models are classes you build that represent
database tables (RealPython)
they all extend the models.Model class"""

#tables: posts, categories, date, tags, comments

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField(max_length=400)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='images/', default="")
    categories = models.ManyToManyField("Category", related_name="posts")
    tags = TaggableManager()
    slug = models.SlugField(null=True, max_length=200, unique=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    @property 
    def img_preview(self):
        if self.image:
            return safestring.mark_safe(f'<img src= "{self.image.url}" width = "200"/>')
        return ""

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    image_alt_text = models.CharField(default="img", max_length=350)

    @property 
    def img_preview(self):
        if self.image:
            return safestring.mark_safe(f'<img src= "{self.image.url}" width = "100"/>')
        return ""

    def __str__(self):
        return self.image_alt_text


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

class TagIndexPage(models.Model):
    def get_context(self, request):
        tag = request.GET.get("tag")
        blogposts = Post.objects.filter(tags__name=tag).order_by('-created_on')
        context = super().get_context(request)
        context["blogposts"] = blogposts
        return context 