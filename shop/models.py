from django.db import models
from django.utils.html import format_html
from django.utils.html import mark_safe
from PIL import Image
from io import BytesIO
import base64

class  Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    slug = models.SlugField(max_length=200, verbose_name="url наименование")
    image = models.ImageField( upload_to='categories/', blank=True, null=True, verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Редактирование")
    def __str__(self):
        return f"{self.name}"

    def get_preview(self):
        if self.image:
            return format_html(
                '<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;" />',
                self.image.url
            )
        return "—"

    get_preview.short_description = "Превью"
    get_preview.allow_tags = True  #

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    slug = models.SlugField(max_length=255, verbose_name="url наименование")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    stock = models.IntegerField(verbose_name="Кол-во")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Редактирование")
    def __str__(self):
        return f"{self.name}"

    def get_preview(self):
        if self.image:
            return format_html(
                '<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;" />',
                self.image.url
            )
        return "—"

    get_preview.short_description = "Превью"
    get_preview.allow_tags = True  #

    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"

