from django import template

register = template.Library()


@register.filter()
def ampersand(value):
    return value.replace("&", "%26")


@register.filter()
def slash(value):
    return value.replace("\\", "")


@register.filter()
def dquot(value):
    return value.replace("\"", "")
