from django.db import models
from django.utils.text import slugify
from catalog.models import Product


class ProjectPost(models.Model):
    BATH = "bath"
    KITCHEN = "kitchen"

    SECTION_CHOICES = [
        (BATH, "Bath"),
        (KITCHEN, "Kitchen"),
    ]

    title = models.CharField(
        max_length=140,
    )

    slug = models.SlugField(
        max_length=160,
        unique=True,
        blank=True,
    )

    section = models.CharField(
        max_length=10,
        choices=SECTION_CHOICES
    )

    excerpt = models.CharField(
        max_length=255,
    )

    content = models.TextField(
        blank=True,
    )

    cover_image_url = models.URLField(
        blank=True,
    )

    related_products = models.ManyToManyField(
        Product,
        blank=True,
        related_name='projects',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def total_price(self):
        return sum(p.price for p in self.related_products.all())


    class Meta:
        ordering = (
            '-created_at',
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
