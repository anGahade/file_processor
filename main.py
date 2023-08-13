"""
Реалізуйте програму, яка копіює вміст одного файлу в інший.
"""
source_file = 'test.txt'
dest_file = 'test_2.txt'


def copy_file():
    with open(source_file, 'r') as src:
        with open(dest_file, 'w') as dst:
            dst.write(src.read())


copy_file()

print('Файл успішно скопійовано!')

