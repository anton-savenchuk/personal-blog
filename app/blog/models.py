from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


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
    category = models.ForeignKey(
        to="Category",
        on_delete=models.PROTECT,
        null=True,
        db_index=True,
        verbose_name="Категория",
    )
    tag = models.ManyToManyField(
        to="Tag",
        blank=True,
        db_index=True,
        verbose_name="тег",
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

    def get_absolute_url(self):
        """Return post url."""
        return reverse("post", kwargs={"post_slug": self.slug})

    def get_time_read(self):
        """Return the read time as minutes of some plain text."""
        total_words = len(self.full_description.split())
        time_read = round(total_words / 180)

        return 1 if time_read == 0 else time_read


class Category(models.Model):
    """Category model."""

    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name="Категория",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="url category",
    )

    class Meta:
        """Sorting, model name in the admin panel, table with data."""

        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]

    def __str__(self):
        """Return the string representation of the object as the category title."""
        return self.title

    def get_absolute_url(self):
        """Return category url."""
        return reverse("category", kwargs={"category_slug": self.slug})


class Tag(models.Model):
    """Tag model."""

    title = models.CharField(
        max_length=60,
        db_index=True,
        verbose_name="тег",
    )
    slug = models.SlugField(
        max_length=60,
        unique=True,
        db_index=True,
        verbose_name="url tag",
    )

    class Meta:
        """Sorting, model name in the admin panel, table with data."""

        verbose_name = "тег"
        verbose_name_plural = "теги"
        ordering = ["title"]

    def __str__(self):
        """Return the string representation of the object as the tag title."""
        return self.title

    def get_absolute_url(self):
        """Return tag url."""
        return reverse("tag", kwargs={"tag_slug": self.slug})
