from django import template


register = template.Library()

STOP_LIST = [
    'дурак',
]
@register.filter(name='rude')
def clean_text(value):
    list = value.split()
    for word in list:
        if word in STOP_LIST:
            list.replace(word, '*')
    return list.join()