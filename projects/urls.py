from django.urls import path
from . import views


urlpatterns = [
    path("", views.Projects.as_view()),
    path("<int:pk>/audios/", views.ProjectAudio.as_view()),
]
