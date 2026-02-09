import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

def convert_to_png(file_path):
    """Конвертация файла JP2 в PNG"""
    try:
        img = Image.open(file_path)
        new_file_name = f"{os.path.splitext(file_path)[0]}.png"
        img.save(new_file_name, format='PNG')
        return True
    except Exception as e:
        print(f"Ошибка при конвертации {file_path}: {e}")
        return False

def select_and_convert():
    """Выбор файлов и их конвертация"""
    files = filedialog.askopenfilenames(title="Выберите файлы JP2",
                                        filetypes=(("JPEG 2000 Files", "*.jp2"), ("All Files", "*.*")))
    successful_conversions = []
    failed_conversions = []

    for file in files:
        if file.lower().endswith('.jp2'):
            success = convert_to_png(file)
            if success:
                successful_conversions.append(file)
            else:
                failed_conversions.append(file)

    if len(successful_conversions) > 0 or len(failed_conversions) > 0:
        msg = ""
        if len(successful_conversions) > 0:
            msg += f"Успешно преобразованы:\n{successful_conversions}"
        if len(failed_conversions) > 0:
            msg += f"Произошла ошибка при обработке:{failed_conversions}"
        
        messagebox.showinfo("Результат конвертации", msg)

root = tk.Tk()
root.withdraw()  # Скрываем главное окно Tkinter

select_and_convert()