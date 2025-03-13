# Example: File Backup Context Manager
import os
import shutil

class FileBackupContextManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.backup_file_path = f'{file_path}_backup.txt'
    

    def __enter__(self):
        # if the file path exists, the make a copy in backup file
        if os.path.exists(self.file_path):
            shutil.copy2(self.file_path, self.backup_file_path)
        return self
    

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An error occured: {exc_value}. Restore the original file")
            if os.path.exists(self.backup_file_path):
                shutil.copy2(self.backup_file_path, self.file_path)
        else:
            # no exception, delete backup file
            if os.path.exists(self.backup_file_path):
                os.remove(self.backup_file_path)


file_path = 'sample.txt'

with open(file_path, 'w') as file:
    file.write("Some more context")

def class_context_manager_example():

    try:
        with FileBackupContextManager(file_path=file_path) as backup_manager:
            with open(file_path, 'w') as file:
                file.write("This is new content")

                # mock error
                raise ValueError("Something went wrong")
    except Exception as ex:
        print(f'Error: {ex}')


class_context_manager_example()

# read file content
with open(file_path, 'r') as file:
    print(f"File content after changes: {file.read()}")