from django_filters import FilterSet, DateTimeFilter
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'change_news': ['icontains'],
            'head_news': ['icontains'],
            'time_in': ['gt'],
        }
