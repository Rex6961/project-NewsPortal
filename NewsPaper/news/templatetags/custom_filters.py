from django import template
from .f_mat import list_mat
import string

register = template.Library()


@register.filter()
def censor(word, code="*"):
    word = word.lower().translate(str.maketrans('', '', string.punctuation))
    for mat in list_mat:
        if mat in word:
            word = word.replace(mat[1:], code * (len(mat) - 1))
    return f'{word}'

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k]=v
    return d.urlencode()