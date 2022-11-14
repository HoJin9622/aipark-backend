from django.db import models
from common.models import CommonModel


class Project(CommonModel):
    index = models.PositiveIntegerField(verbose_name="순서")
    project_id = models.PositiveIntegerField(verbose_name="프로젝트 ID")
    project_title = models.CharField(max_length=80, verbose_name="프로젝트명")

    class Meta:
        verbose_name = "프로젝트"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.project_title
