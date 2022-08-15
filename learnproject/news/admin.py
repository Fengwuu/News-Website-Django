from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):  # Creating News point in admin panel
    list_display = ('id', 'title', 'category',
                    'created_date', 'updated_at', 'is_published', 'get_photo')  # which fields would be shown
    list_display_links = ('id', 'title')  # which fields would have hyperlink
    search_fields = ('title', 'content')  # which fields would be used in search
    list_editable = ('is_published',)  # which field you can edit in admin panel menu
    list_filter = ('is_published', 'category')  # which fiends wil be used as filter parameter
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'created_date', 'updated_at', 'is_published',)
    readonly_fields = ('get_photo', 'created_date', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фотография не установлена! '

    get_photo.short_description = 'Изображение: '

class CategoryAdmin(admin.ModelAdmin):  # Create CATEGORY model visualisation in admin panel
    list_display = ('id', 'title')  # which fields would be shown
    list_display_links = ('id', 'title')  # which fields would have hyperlink
    search_fields = ('title',)  # which fields would be used in search


admin.site.register(News, NewsAdmin)  # Register News model
admin.site.register(Category, CategoryAdmin)  # Register CATEGORY model
admin.site.site_title = 'Упарвление новостями'
admin.site.site_header = admin.site.site_title
