from django.shortcuts import render

# Create your CORE views here.

def core_index(request):
    return render(request, "core/index.html")

def core_about(request):
    return render(request, "core/about.html")

def core_inquisitor(request):
    return render(request, "core/inquisitor.html")

def core_directors(request):
    return render(request, "core/directors.html")

def core_aides(request):
    return render(request, "core/aides.html")

def core_careers(request):
    return render(request, "core/careers.html")

def core_news(request):
    return render(request, "blog/blog_list.html")

def core_faqs(request):
    return render(request, "core/faqs.html")

def core_values(request):
    return render(request, "core/values.html")

def core_friends(request):
    return render(request, "core/friends.html")

def core_work(request):
    return render(request, "core/work.html")