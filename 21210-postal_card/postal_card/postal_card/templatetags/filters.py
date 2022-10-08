from django import template

register = template.Library()

@register.filter(name='persian_numbers')
def persian_numbers(string):
    list_string = list(string)

    for i in range(len(list_string)):
        if list_string[i] == '1':
            list_string[i] = '۱'
        elif list_string[i] == '2':
            list_string[i] = '۲'
        elif list_string[i] == '3':
            list_string[i] = '۳'
        elif list_string[i] == '4':
            list_string[i] = '۴'
        elif list_string[i] == '5':
            list_string[i] = '۵'
        elif list_string[i] == '6':
            list_string[i] = '۶'
        elif list_string[i] == '7':
            list_string[i] = '۷'
        elif list_string[i] == '8':
            list_string[i] = '۸'
        elif list_string[i] == '9':
            list_string[i] = '۹'
        elif list_string[i] == '0':
            list_string[i] = '۰'
      
    sentence = ""

    for item in list_string:
        sentence += item

    return sentence
