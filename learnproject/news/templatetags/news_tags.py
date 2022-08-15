from django import template
from news.models import Category
from django.contrib.auth.models import Group
register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(list_name="Список категорий⠀⠀"):
    categories = Category.objects.all()
    return {"categories": categories, 'list_name': list_name}


@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group =Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False

    return group in user.groups.all()
