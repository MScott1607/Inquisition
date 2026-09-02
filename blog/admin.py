from django.contrib import admin
from .models import Post, Comment, Category, PostImage
# Register your models here.
#this is where you can customise the admin pages

class PostImageAdmin(admin.StackedInline):
    model = PostImage 
    readonly_fields = ['img_preview']
    def img_preview(self, obj):
        return obj.img_preview

    img_preview.short_description = 'Image Preview'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display=['title', 'intro', 'slug', 'get_tags', 'img_preview']
    search_fields = ['title', 'intro', 'body']

    class Meta:
        model=Post

    def body_trunc(self, obj):
        return obj.body[:100]
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def get_tags(self, obj):
        return", ".join(o for o in obj.tags.names())
    
    def img_preview(self, obj):
        return obj.img_preview


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['image_alt_text', 'img_preview', 'post']

    def img_preview(self, obj):
        return obj.img_preview

    img_preview.short_description = 'Image Preview'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['body']
    list_display = ['author', 'body']
    def body_trunc(self, obj):
        return obj.body[:150]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name',]
