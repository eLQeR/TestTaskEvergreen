from django.contrib import admin
from test_task.models import Page
from image_cropping import ImageCroppingMixin


class PageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
