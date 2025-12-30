# Минимальный рабочий код для сохранения в конкретную папку
import json
import os

# 1. Определите путь к папке и имя файла
folder = r'C:\Users\andre\Documents\Py_files'
filename = 'my_data.json'

# 2. Создайте папку (если нужно)
os.makedirs(folder, exist_ok=True)

# 3. Сформируйте полный путь
full_path = os.path.join(folder, filename)

# 4. Используйте этот путь в open() перед json.dump()
with open(full_path, 'w', encoding='utf-8') as f:
    json.dump({"ключ": "значение"}, f, ensure_ascii=False, indent=4)