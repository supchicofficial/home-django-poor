from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html')

def blog_view(request):
    return render(request, 'blog.html')

def contacts_view(request):
    return render(request, 'contacts.html')