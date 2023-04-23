from . import views
from django.urls import path


urlpatterns = [
    path('',views.Blog, name='home'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name = 'blog_detail')
]
