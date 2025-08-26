"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from posts.views import first_view, html_view, post_list_view, home_view, post_detail_view, post_create_view, post_update_view
from users.views import register_view, login_view, logout_view, profile_view
from django.conf.urls.static import static
from django.conf import settings

users_patterns = [
    path("register/", register_view, name = "register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
]


posts_patterns = [
    path("admin/", admin.site.urls),
    path("first/", first_view),
    path("html/", html_view),
    path("posts/", post_list_view),
    path("", home_view, name="home"),
    path("posts/<int:post_id>/", post_detail_view, name="post_detail"),
    path("posts/create/", post_create_view),
    path("posts/<int:post_id>/update/", post_update_view),
] 

urlpatterns = users_patterns + posts_patterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
