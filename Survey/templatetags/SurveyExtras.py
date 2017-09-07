from django import template

register = template.Library()

@register.filter(name='input_type')
def InputType(value):
    if value==True:
        return 'checkbox'
    else:
        return 'radio'


@register.filter(name='message')
def Message(value):
    if value==True:
        return 'Multi choice selection:'
    else:
        return 'Select one:'
