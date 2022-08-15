from django.urls import path
from .views import *
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('cat/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('add_news/', CreateNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('exit/', authViews.LogoutView.as_view(next_page='/'), name='exit'),
    path('for_jour/', for_journalists, name='for_jour'),
]


