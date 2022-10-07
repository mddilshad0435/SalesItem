
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.Home,name='home'),
    path('signup/', views.Signup.as_view(),name="signup"),
    path('login/', views.LoginView.as_view(),name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='home'),name='logout'),
    path('additems/', views.AddItems.as_view(),name="additems"),
    path('edititems/<int:id>/', views.EditItems.as_view(),name="edititems"),
]

