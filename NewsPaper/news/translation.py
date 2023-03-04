from .models import Post
from modeltranslation.translator import register, TranslationOptions


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('category', 'time_in', 'head_news', 'text_news', )
