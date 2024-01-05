# waitlist/urls.py

from django.urls import path
from .views import waitlist_signup, success_page

urlpatterns = [
    path('signup/', waitlist_signup, name='waitlist_signup'),
    path('success/', success_page, name='success_page'),
]