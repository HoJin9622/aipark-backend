from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
