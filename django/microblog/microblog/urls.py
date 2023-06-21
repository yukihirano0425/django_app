from blog.views import homepage, post_detail
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage),
    path("<slug:slug>/", post_detail, name="post_detail"),
]
