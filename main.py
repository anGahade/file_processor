"""
Створіть функцію, яка приймає рядок від користувача та записує його у файл.
"""


def add_line():
    with open("test.txt", "r+") as file:
        file.write(input("Введіть нові дані: "))
        file.seek(0)
        content = file.read()

    return f"Новий вміст файлу:\n{content}"


print(add_line())

