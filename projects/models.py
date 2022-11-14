from django.db import models
from common.models import CommonModel


class Audio(CommonModel):
    index = models.PositiveIntegerField(verbose_name="순서")
    text = models.CharField(max_length=80, verbose_name="오디오로 변환된 텍스트")
    speed = models.PositiveIntegerField(verbose_name="오디오의 스피드")
    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="projects",
        verbose_name="프로젝트",
    )

    class Meta:
        verbose_name = "오디오"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text


class Project(CommonModel):
    index = models.PositiveIntegerField(verbose_name="순서", unique=True)
    title = models.CharField(max_length=80, verbose_name="프로젝트명")

    class Meta:
        verbose_name = "프로젝트"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
