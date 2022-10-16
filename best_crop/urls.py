from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # API Routes
    path("find_best", views.find_best, name="find_best")
]
