# Example: File Backup Context Manager

from contextlib import contextmanager
import os
import shutil


def take_file_back(file_path, backup_file_path):
    """
    Take file backup by coping main file to backupfile
    """
    if os.path.exists(file_path):
        shutil.copy2(file_path, backup_file_path)


def restore_backup_file(file_path, backup_file_path):
    """
    Copy backup file to main file
    """
    print(f"An error occured. Restore the original file")
    if os.path.exists(backup_file_path):
        shutil.copy2(backup_file_path, file_path)


def delete_backup_file(backup_file_path):
    """
    Delete the backup file, as it is no longer required
    """
    if os.path.exists(backup_file_path):
        os.remove(backup_file_path)


@contextmanager
def file_backup_context_manager(file_path):
    backup_file_path = f'{file_path}_backup.txt'
    
    # take file_backup
    take_file_back(file_path, backup_file_path)
    try:
        yield
        delete_backup_file(backup_file_path)
    except Exception as ex:
        restore_backup_file(file_path, backup_file_path)




file_path = 'sample.txt'

with open(file_path, 'w') as file:
    file.write("Some more context")


def function_context_manager_example():
    try:
        with file_backup_context_manager(file_path=file_path):
            with open(file_path, 'w') as file:
                file.write("This is new context for testing function context manager")

                # mock error
                raise ValueError("Something went wrong")
    
    except Exception as ex:
        print(f"Error: {ex}")


function_context_manager_example()

# read file content
with open(file_path, 'r') as file:
    print(f"File content after changes: {file.read()}")