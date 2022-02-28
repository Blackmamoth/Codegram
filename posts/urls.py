from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='posts/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/<int:id>/', views.post, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<int:id>/', views.update_post, name='update_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
]
