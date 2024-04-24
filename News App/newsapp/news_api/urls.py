from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import authView, home, custom_logout, bookmarks


urlpatterns = [
    path('', home, name = 'home'),
    path('signup/', authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', custom_logout, name='custom_logout'),
    path('bookmarks/', bookmarks, name='bookmarks'), 
]