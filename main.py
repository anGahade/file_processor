"""
Напишіть програму, яка читає вміст текстового файлу
та виводить кількість слів у ньому.
"""


def read_line():
    file = open("test.txt", "r")
    content = file.read()
    words = content.split()
    count = len(words)
    file.close()
    return (
        f"Вміст файлу: \n{content}"
        f"\nФайл містить {count} слів"
    )


print(read_line())
