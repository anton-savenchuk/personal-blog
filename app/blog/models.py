from django.core.validators import FileExtensionValidator
from django.db import models


class Post(models.Model):
    """Post model."""

    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="url post",
    )
    short_description = models.TextField(
        verbose_name="Краткое описание",
        max_length=300,
    )
    full_description = models.TextField(
        verbose_name="Описание",
    )
    thumbnail = models.ImageField(
        blank=True,
        upload_to="images/thumbnails/%Y/%m/%d/",
        verbose_name="Изображение",
        validators=[
            FileExtensionValidator(
                allowed_extensions=("png", "jpg", "webp", "jpeg", "gif"),
            ),
        ],
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации",
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования",
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
    )
    fixed = models.BooleanField(
        default=False,
        verbose_name="Закреплено",
    )

    class Meta:
        """Sorting, model name in the admin panel, table with data."""

        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-fixed", "-time_create", "title"]
        indexes = [models.Index(fields=["-fixed", "-time_create", "title"])]

    def __str__(self):
        """Return the string representation of the object as the post title."""
        return self.title