from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path("blogmain", views.blog_list, name="blog_list"),
    path("category/<category>/", views.blog_categories, name="blog_categories"),
    path("tag/<slug:tag_slug>/", views.blog_tags, name="blog_tags"),
    path("post/<slug:slug>/", views.blog_detail, name="blog_detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    