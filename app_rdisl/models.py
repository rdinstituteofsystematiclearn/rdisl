from datetime import datetime

from django.db import models


# Create your models here.

class Slider(models.Model):
    slider_img = models.ImageField(upload_to='images', blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tbl_slider"


class OurServices(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading

    class Meta:
        db_table = 'tbl_our_services'


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_gallery_category'


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    cat_id = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_gallery'


class Client(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tbl_client"


class Testimonial(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_feedback'
