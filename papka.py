import os

# Путь к рабочему столу
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Создание 500 папок с названием "кекиш"
for i in range(1, 501):
    folder_name = f"кекиш_{i}"
    folder_path = os.path.join(desktop_path, folder_name)
    os.makedirs(folder_path)

print("Создано 500 папок с названием 'кекиш' на рабочем столе.")


def some_function():
    return None