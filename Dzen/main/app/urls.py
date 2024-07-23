"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from .models import Mark
from .views import UserDetail, PostDetail, CommentDetail, MarkDetail

urlpatterns = [
    path('account/', UserDetail.as_view()),
    path('account_register/', UserDetail.reg),
    path('post/', PostDetail.as_view()),
    path('post/<int:post_id>/comment/', CommentDetail.as_view()),
    path('post_add', PostDetail.create_post),
    path('post/<int:post_id>/', PostDetail.get_id),
    path('post/<int:post_id>/comment_add/', CommentDetail.comment_add),
    path('post/<int:post_id>/mark/', MarkDetail.as_view()),
]