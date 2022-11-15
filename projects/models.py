import re
from django.db import models
from common.models import CommonModel


class Audio(CommonModel):
    index = models.PositiveIntegerField(unique=True, verbose_name="순서")
    text = models.CharField(max_length=80, verbose_name="오디오로 변환된 텍스트")
    speed = models.PositiveIntegerField(default=1, verbose_name="오디오의 스피드")
    path = models.CharField(max_length=80, verbose_name="파일 경로")
    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="audios",
        verbose_name="프로젝트",
    )

    class Meta:
        verbose_name = "오디오"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text

    @property
    def processed_text(self):
        separated_text = re.split("[.!?]", self.text)
        no_gap_text = []
        for text in separated_text:
            if text.isspace():
                continue
            no_gap_text.append(text.strip())
        return no_gap_text


class Project(CommonModel):
    index = models.PositiveIntegerField(verbose_name="순서", unique=True)
    title = models.CharField(max_length=80, verbose_name="프로젝트명")

    class Meta:
        verbose_name = "프로젝트"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
