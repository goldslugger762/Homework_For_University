'''# task 1
# создать файл my_functions.py с функциями greet и change_name
# change_name - принимает строку, а возвращает измененное имя, где каждая вторая буква - большая
# greet - принимает строку, ничего не возвращает, а просто принтит "Hello имя" с помощью украшений из rich print
'''

from rich import print
from rich.text import Text

def change_name(value: str) -> str:
    make_upper = value[0].isupper()  # определяем регистр первой буквы, если большая то тру
    
    changed_text = ""
    for char in value:
        if make_upper:
            changed_text += char.upper()
        else:
            changed_text += char.lower()
        make_upper = not make_upper
    
    return changed_text

def greet(name: str) -> str:
    text = Text(f"Hello {name}!", justify="center", style="bold italic")
    text.stylize("bold red3", 0, 5)
    text.stylize("bold sea_green2", 6, len(name))
    text.stylize("bold cyan", len(name), len(text))
    return print(text)