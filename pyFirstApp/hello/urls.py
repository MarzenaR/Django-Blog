from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("about/", views.about, name="about"),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path("article/new/", views.ArticleCreateView.as_view(), name="article-new"),
    path('article/update/<int:pk>', views.ArticleUpdateView.as_view(), name='article-update'),
    path('article/delete/<int:pk>', views.ArticleDeleteView.as_view(), name='article-delete')
]