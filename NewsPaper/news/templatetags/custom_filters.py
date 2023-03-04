from django import template
from .f_mat import list_mat
import string
from datetime import datetime

register = template.Library()


@register.filter()
def censor(word, code="*"):
    wordMat = word.lower().translate(str.maketrans('', '', string.punctuation + string.digits))
    for mat in list_mat:
        while mat in wordMat:
            word_a = wordMat.replace(mat[1:], code * (len(mat) - 1))
            print(word_a)
            wordMat = word_a
            word = wordMat
    return f'{word}'

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k]=v
    return d.urlencode()

@register.simple_tag(name="get_hour")
def current_hour():
    now = datetime.now()
    return now.strftime("%H")