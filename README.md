# goit-pythonweb-hw-04

**Fullstack Web Development with python. HW 4. Asynchronous programming**

Напишіть Python-скрипт, який буде читати всі файли у вказаній користувачем вихідній папці (source folder) і розподіляти їх по підпапках у директорії призначення (output folder) на основі розширення файлів. Скрипт повинен виконувати сортування асинхронно для більш ефективної обробки великої кількості файлів.

## Технічний опис завдання

- Імпортуйте необхідні асинхронні бібліотеки.
- Створіть об'єкт `ArgumentParser` для обробки аргументів командного рядка.
- Додайте необхідні аргументи для визначення вихідної та цільової папок.
- Ініціалізуйте асинхронні шляхи для вихідної та цільової папок.
- Напишіть асинхронну функцію `read_folder,` яка рекурсивно читає всі файли у вихідній папці та її підпапках.
- Напишіть асинхронну функцію `copy_file,` яка копіює кожен файл у відповідну підпапку у цільовій папці на основі його розширення.
- Налаштуйте логування помилок.
- Запустіть асинхронну функцію `read_folder` у головному блоці.

## Критерії прийняття

- Код успішно виконує асинхронне читання та копіювання файлів.
- Файли розподілено по підпапках на основі їх розширень.
- Програма коректно обробляє аргументи командного рядка.
- Усі помилки логовано.
- Код читабельний та відповідає стандартам PEP 8.
