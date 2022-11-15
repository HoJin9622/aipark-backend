from django.contrib import admin
from django.urls import path, include
from projects.views import AudioDetail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/projects/", include("projects.urls")),
    path("api/v1/audios/<int:pk>/", AudioDetail.as_view()),
]
