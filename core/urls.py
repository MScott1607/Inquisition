from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.core_index, name="core_index"),
    path("about", views.core_about, name="core_about"),
    path("inquisitor", views.core_inquisitor, name="core_inquisitor"),
    path("directors", views.core_directors, name="core_directors"),
    path("aides", views.core_aides, name="core_aides"),
    path("careers", views.core_careers, name="core_careers"),
    path("faqs", views.core_faqs, name="core_faqs"),
    path("values", views.core_values, name="core_values"),
    path("friends", views.core_friends, name="core_friends"),
    path("work", views.core_work, name="core_work"),
    path("blog/", include("blog.urls")),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)