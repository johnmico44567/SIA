from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add/", views.add_setting, name="add_setting"),
    path("delete/<int:setting_id>/", views.delete_setting, name="delete_setting"),
]
