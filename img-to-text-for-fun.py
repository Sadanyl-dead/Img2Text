import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageOps
import pytesseract
import pyperclip
import subprocess
import os


class ImageToTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title('ImgTxt')
        self.root.geometry("200x150")

        self.language_label = tk.Label(root, text='Select Language:')
        self.language_label.pack()

        self.languages = pytesseract.get_languages()
        self.language_combobox = ttk.Combobox(root, state='readonly')
        self.language_combobox['values'] = self.languages
        self.language_combobox.current(0)
        self.language_combobox.pack()

        self.convert_button = tk.Button(root, text='Convert', command=self.convert_image)
        self.convert_button.pack()

        self.text_box = tk.Text(root, height=5, width=30)  # Уменьшаем начальный размер текстового поля
        self.text_box.pack(fill=tk.BOTH, expand=True)  # Расширяем текстовое поле при увеличении объема текста

        # Создаем собственную панель инструментов с кнопкой "Copy" и размещаем рядом с кнопками управления окном
        self.toolbar_frame = ttk.Frame(root)
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X)

        self.copy_button = ttk.Button(self.toolbar_frame, text='Copy', command=self.copy_to_clipboard)
        self.copy_button.pack(side=tk.RIGHT)

    def convert_image(self):
        selected_language = self.language_combobox.get()
        if selected_language:
            filename = filedialog.askopenfilename(filetypes=[('Images', '*.png;*.jpg;*.jpeg;*.bmp')])
            if filename:
                image = Image.open(filename)
                # Преобразование изображения в черно-белый формат
                image = ImageOps.grayscale(image)
                text = pytesseract.image_to_string(image, lang=selected_language)
                self.text_box.delete('1.0', tk.END)
                self.text_box.insert(tk.END, text)

    def copy_to_clipboard(self):
        text = self.text_box.get('1.0', tk.END)
        pyperclip.copy(text)

def main():
    root = tk.Tk()
    app = ImageToTextConverter(root)
    root.mainloop()

if __name__ == '__main__':
    main()


#setx /M PATH "%PATH:;C:/Program Files/Tesseract-OCR\bin=%" delete path tesseract