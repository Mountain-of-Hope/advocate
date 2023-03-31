from django import template

register = template.Library()

@register.filter
def get_type(value):
    testVal = type(value)
    return testVal.__name__