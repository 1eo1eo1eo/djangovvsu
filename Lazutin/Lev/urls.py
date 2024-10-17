from django.contrib import admin
from django.urls import path
from Lev import views

app_name = "Lev"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.BaseView.as_view(), name="base"),
    path("info/", views.InfoView.as_view(), name="info"),
    path("group/", views.GroupView.as_view(), name="group"),
    path("age/", views.AgeView.as_view(), name="age"),
]
