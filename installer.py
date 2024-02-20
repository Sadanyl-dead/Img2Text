import subprocess
import os 

def install_tesseract():
    installer_path = os.path.join(os.path.dirname(__file__), "tesseract-ocr-w64-setup.exe")
    language = "russian"  # Замените на нужное значение
    location = "C:\\Tesseract"  # Замените на нужное значение
    result = subprocess.run([installer_path, "/SILENT"])
    if result.returncode == 0:
        print("Tesseract OCR успешно установлен.")
    else:
        print("Произошла ошибка при установке Tesseract OCR.")

if __name__ == "__main__":
    install_tesseract()
