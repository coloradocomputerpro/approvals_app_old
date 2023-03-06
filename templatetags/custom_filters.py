from django import template

register = template.Library()


@register.filter(name='field_name_from_string')
def field_name_from_string(form, field_name):
    return getattr(form, field_name)


@register.filter(name='string')
def string(value):
    return str(value)


@register.filter(name='int')
def int(value):
    return int(value)
