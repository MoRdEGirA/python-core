"""
Напиши функцию чтения файла, которая:

При отсутствии файла выбрасывает своё исключение FileMissingError.

При пустом файле выбрасывает EmptyFileError.

Иначе возвращает содержимое файла.
"""

class FileMissingError(Exception):
    pass

class EmptyFileError(Exception):
    pass

def read_file(file_name: str) -> str:
    try:
        with open(file_name, mode="r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        raise FileMissingError(f"Файл не найден - {file_name}")
    
    if not content:
        raise EmptyFileError(f"{EmptyFileError} - Файл пуст - {file_name}")
    
    return content

def safe_read(file_name):
    print(f"Пробуем прочитать файл - {file_name}")
    try:
        content = read_file(file_name)
        print(f"Сожержимое файла - {content}")
    except FileMissingError as e:
        print(f"[Ошибка - FileNotFoundError] {e}")
    except EmptyFileError as e:
        print(f"[Ошибка - EmptyFileError] {e}")
    except Exception as e:
        print(f"[Неизвестаня ошибка - Exception] {e}")
    
    
    
if __name__ == "__main__":
    files = [
        "file/task_01_zero.txt",
        "file/task_01_notfound.txt",
        "file/task_01.txt",
    ]
    for file_path in files:
        safe_read(file_path)
        