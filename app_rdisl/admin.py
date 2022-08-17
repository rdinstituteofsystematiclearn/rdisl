from django.contrib import admin

from .models import *


# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'slider_img', 'created_at')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description', 'images', 'slug')


class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat_id', 'image', 'slug', 'created_at')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_at')


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'profile', 'description', 'created_at')


admin.site.register(Slider, SliderAdmin)
admin.site.register(OurServices, ServicesAdmin)
admin.site.register(GalleryCategory, GalleryCategoryAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
