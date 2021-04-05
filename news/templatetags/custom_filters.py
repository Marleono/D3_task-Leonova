from django import template


register = template.Library()

STOP_LIST = [
    'дурак',
]
@register.filter(name='rude')
def clean_text(value):
    for word in value.split():
        if word in STOP_LIST:
            value.replace(word,'***')
    return value
