import os
import shutil
import asyncio
import argparse
from typing import List

async def read_folder(source: str) -> List[str]:
    """
    Асинхронно читає всі файли у вихідній папці та її підпапках.
    
    Args:
        source (str): Шлях до вихідної папки.
    
    Returns:
        List[str]: Список шляхів до файлів у вихідній папці.
    """
    try:
        files = []
        for root, _, filenames in os.walk(source):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        return files
    except Exception as e:
        print(f"Помилка при читанні папки {source}: {e}")
        return []

async def copy_file(source_file: str, output: str) -> None:
    """
    Асинхронно копіює файл у відповідну підпапку цільової папки на основі його розширення.
    
    Args:
        source_file (str): Шлях до вихідного файлу.
        output (str): Шлях до вихідної папки.
    """
    try:
        extension = os.path.splitext(source_file)[1].lstrip('.')
        destination_folder = os.path.join(output, extension or "no_extension")
        os.makedirs(destination_folder, exist_ok=True)
        
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, shutil.copy, source_file, destination_folder)
        print(f"Файл {source_file} успішно скопійовано в {destination_folder}")
    except Exception as e:
        print(f"Помилка при копіюванні {source_file}: {e}")

async def main(source_folder: str, output_folder: str) -> None:
    """
    Основна асинхронна функція, що читає файли у вихідній папці та сортує їх за розширеннями.
    
    Args:
        source_folder (str): Вихідна папка для читання файлів.
        output_folder (str): Цільова папка для сортування файлів.
    """
    files = await read_folder(source_folder)
    tasks = [copy_file(file, output_folder) for file in files]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Асинхронне сортування файлів за розширенням")
    parser.add_argument("--source", type=str, default="./source", help="Шлях до вихідної папки")
    parser.add_argument("--output", type=str, default="./output", help="Шлях до цільової папки")
    args = parser.parse_args()
    
    source_folder = args.source
    target_folder = args.output

    asyncio.run(main(source_folder, target_folder))
