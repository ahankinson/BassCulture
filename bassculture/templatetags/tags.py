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


@register.filter()
def asterisk(value):
    return value.replace("*:*", "")


@register.filter(is_safe=True)
def squares1(value):
    return value.replace("['", "")


@register.filter(is_safe=True)
def squares2(value):
    return value.replace("']", "")


@register.filter(is_safe=True)
def squares3(value):
    return value.replace("\"]", "")


@register.filter(is_safe=True)
def squares4(value):
    return value.replace("[\"", "")

@register.filter(is_safe=True)
def slashn(value):
    return value.replace("\\n", "")


@register.filter(is_safe=True)
def etc(value):
    return value.replace("&C", "&c")
