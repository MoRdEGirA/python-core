class DataLoadException(Exception):
    pass

class Read_file:
    def __init__(self, file_path=None, mode="r"):
        self.file = None
        self.file_path = file_path
        self.backup_path = f"{file_path}_backup"
        self.mode = mode
        
    def __enter__(self):
        try:
            print(f"Пробую открыть файл - {self.file_path}.txt")
            self.file = open(f"{self.file_path}.txt", mode=self.mode)
            return self.file
        except FileNotFoundError as e:
            try:
                print(f"Произошла ошибка. Пробую открыть файл - {self.backup_path}.txt")
                self.file = open(f"{self.backup_path}.txt", mode=self.mode)
                return self.file
            except FileNotFoundError as e2:
                raise DataLoadException(f"[Ошибка при открытие файлов - {self.file_path} и {self.backup_path}.txt]")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.close()
        

        
if __name__ == "__main__":
    files = [
        "file/task_02_1",
        "file/task_02_2",
        "file/task_02_3",
    ]
    
    for file_path in files:
        try:
            with Read_file(file_path) as f:
                content = f.read()
                print(f"Файл {file_path} - содержимое - {content}")
        except DataLoadException as e:
            print(f"[DataLoadException] {e}\n")