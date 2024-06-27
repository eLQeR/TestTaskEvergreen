import os
import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from image_cropping import ImageRatioField


class Worker(AbstractUser):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)

    class Positions(models.TextChoices):
        ADMIN = "Адміністратор"
        EDITOR = "Редактор"
        SUPERUSER = "Власник"

    position = models.CharField(
        max_length=50,
        choices=Positions.choices,
    )


def create_header_image_path(instance, filename):
    _, extension = os.path.splitext(filename)
    return os.path.join(
        "uploads/images/",
        f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"
    )


class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    header = models.ImageField(
        upload_to=create_header_image_path,
        default="uploads/images/default_header.png"
    )
    created_by = models.ForeignKey(to=get_user_model(), on_delete=models.DO_NOTHING, related_name="pages")
    cropping = ImageRatioField('header', '720x360')

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.title} - {self.created}"
