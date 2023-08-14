"""
Створіть функцію, яка видаляє вказаний рядок з текстового файлу.
"""


def remove_line_from_file(file_path, line_to_remove):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                if line.strip() != line_to_remove.strip():
                    file.write(line)

        print(f"Рядок '{line_to_remove}' був видалений з файлу '{file_path}'.")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")



remove_line_from_file('test.txt', 'такі самотні-самотні.')

