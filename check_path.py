import os

path = "catalog/templates/catalog/includes/menu.html"
full_path = os.path.abspath(path)

print(f"Проверяем путь: {full_path}")
print(f"Файл существует: {os.path.exists(full_path)}")
print(f"Это файл: {os.path.isfile(full_path)}")

# Проверим структуру папок
print("\nСодержимое папки templates:")
for root, dirs, files in os.walk("catalog/templates"):
    level = root.replace("catalog/templates", '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")