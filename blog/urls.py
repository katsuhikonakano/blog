"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings         
from django.conf.urls.static import static
from ka_kun_blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CategoryListView, TagListView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name="index"),
    path('<int:pk>', PostDetailView.as_view(), name="detail"),
    path('create', PostCreateView.as_view(), name="create"),
    path('<int:pk>/update', PostUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name="delete"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('category/<str:category>', CategoryListView.as_view(), name="category"),
    path('tag/<str:tag>', TagListView.as_view(), name="tag"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)