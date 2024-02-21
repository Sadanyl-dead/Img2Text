import tkinter as tk
from tkinter import Canvas, Button, PhotoImage, filedialog, ttk, messagebox
from PIL import Image, ImageOps
import pytesseract
import pyperclip
from pathlib import Path

# Get the directory of the main script
MAIN_SCRIPT_DIR = Path(__file__).parent

# Define the relative path to the assets folder
ASSETS_PATH = MAIN_SCRIPT_DIR / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path

def convert_image():
    selected_language = language_combobox.get()
    if selected_language:
        filename = filedialog.askopenfilename(filetypes=[('Images', '*.png;*.jpg;*.jpeg;*.bmp')])
        if filename:
            image = Image.open(filename)
            image = ImageOps.grayscale(image)
            text = pytesseract.image_to_string(image, lang=selected_language)
            text_box.delete('1.0', tk.END)
            text_box.insert(tk.END, text)
            text_box.config(fg="#FFFFFF")

def copy_to_clipboard():
    text = text_box.get('1.0', tk.END)
    pyperclip.copy(text)

window = tk.Tk()
window.geometry("368x420")
window.configure(bg="#C20000")

canvas = Canvas(
    window,
    bg="#C20000",
    height=420,
    width=368,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    248.0,
    214.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copy_to_clipboard(),
    relief="flat"
)
button_1.place(
    x=138.0,
    y=379.0,
    width=99.0,
    height=36.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    184.0,
    238.0,
    image=entry_image_1
)

# Replaced Entry with Text
text_box = tk.Text(
    bd=0,
    bg="#1C1B1B",
    fg="#FFFFFF",
    highlightthickness=0
)
text_box.place(
    x=55.0,
    y=107.0,
    width=258.0,
    height=260.0
)

canvas.create_text(
    45.0,
    3.0,
    anchor="nw",
    text="Image to text converter",
    fill="#FFFFFF",
    font=("IrishGrover Regular", 24 * -1)
)

# Added a dropdown field for language selection
language_options = ['eng', 'rus']  # List of supported languages
language_combobox = ttk.Combobox(window, values=language_options)
language_combobox.place(x=9.0, y=55.0, width=172.0, height=42.0)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: convert_image(),
    relief="flat"
)
button_3.place(
    x=200.0,
    y=62.0,
    width=74.0,
    height=28.0
)
window.resizable(False, False)
window.mainloop()
