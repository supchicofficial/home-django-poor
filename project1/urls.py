from django.urls import path
from .views import home_view, about_view, services_view, blog_view, contacts_view

urlpatterns = [
    path('', home_view),
    path('about/', about_view),
    path('services/', services_view),
    path('blog/', blog_view),
    path('contacts/', contacts_view),
]