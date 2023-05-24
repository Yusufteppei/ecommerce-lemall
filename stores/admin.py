from django.contrib import admin
from .models import Store, Contact, Product, Category, Image
from django.utils.html import format_html

# Register your models here.

m = [ Store, Contact, Category, ]

for i in m:
    admin.site.register(i)

@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="300px" width="300px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', ]
    list_per_page = 5


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.images.count() > 0:
            img = obj.images.first().image.url
        else:
            img = Image.objects.get(title='default').image.url
        return format_html('<img src="{}" height="200px" width="200px"/>'.format(img))

    image_tag.short_description = 'Image'

    list_display = ['title', 'image_tag', 'selling_price']
    list_per_page = 5

    search_fields = ('title', )
    list_filter = ('category',)