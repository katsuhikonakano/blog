from .models import Category, Tag
from django.db.models import Count, Q


def common(request):
    context = {
        'category_list': Category.objects.annotate(
            num_posts=Count('post')),
        'tag_list': Tag.objects.annotate(
            num_posts=Count('post')),
    }

    return context