import subprocess
import os
from tkinter import messagebox

def install_tesseract():
    installer_path = os.path.join(os.path.dirname(__file__), "tesseract-ocr-w64-setup.exe")
    language = "russian"  # Замените на нужное значение
    location = "C:\\Tesseract"  # Замените на нужное значение
    result = subprocess.run([installer_path, "/SILENT"])
    return result

def checker(result):
    if result.returncode == 0:
        messagebox.showinfo("Установка","Tesseract OCR успешно установлен.")
    else:
        messagebox.showinfo("Установка","Произошла ошибка при установке Tesseract OCR.")
    
    path = 'C:/Program Files/Tesseract-OCR'
    if os.path.exists(path):
        messagebox.showinfo("Проверка пути", f"Путь {path} существует.")
    else:
        messagebox.showerror("Проверка пути", f"Путь {path} не существует.")
    command='setx PATH "%PATH%;C:/Program Files/Tesseract-OCR"'
    subprocess.run(command,shell=True)

if __name__ == "__main__":
    result=install_tesseract()
    checker(result)