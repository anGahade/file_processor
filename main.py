"""
Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст,
виводячи рядки, які є у першому файлі, але відсутні у другому.
"""


def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
            lines_file1 = set(file1.readlines())
            lines_file2 = set(file2.readlines())

            missing_lines = lines_file1 - lines_file2

            print("Рядки, які є у першому файлі, але відсутні у другому:")
            for line in missing_lines:
                print(line.strip())
    except FileNotFoundError:
        print("Один з файлів не знайдено.")


compare_files('test.txt', 'test_2.txt')
