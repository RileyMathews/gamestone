from django.urls import path

from . import views

urlpatterns = [
    path("temporary-user", views.TemporaryLoginView.as_view(), name="temporary-user-create")
]
