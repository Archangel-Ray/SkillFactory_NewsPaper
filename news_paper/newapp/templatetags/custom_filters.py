from django import template

register = template.Library()

LIST_OF_PROHIBITED_WORDS = [
    'ментор',
    'автор',
    'быть',
    'перв',
]


@register.filter()
def censor(value):
    if isinstance(value, str):
        for word in LIST_OF_PROHIBITED_WORDS:
            while word in value.lower():
                index = value.lower().find(word)
                value = f"{value[:index + 1]}{'*' * (len(word) - 1)}{value[index + len(word):]}"
        return value
    else:
        raise TypeError('Неверный тип данных')
