from django import template
register=template.Library()


@register.filter(name='replace')
def replace_char(value,arg):
    return value.replace(arg,'b')

@register.filter(name='rem')
def remove(value,arg):
    return value.replace(arg,' ')


@register.filter(name='low')
def lower(value):
    return value.lower()


def count(value,arg):
    c=0
    for i in range(len(value)):
        if arg==value[i:i+len(arg)]:
            c+=1
    return c

register.filter('char',count)


#register.filter('rep',replace_char)

