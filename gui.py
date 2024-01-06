import tkinter as tk
from tkinter import filedialog
from phone_number import Phonenumber
from phone_number import mobile_operators_counter


def check_phonenumber(phone_number: str):
    phonenumber = Phonenumber(phone_number.strip("\n"))
    phonenumber.record()


def __check_phonenumber():
    check_phonenumber(entry.get())


def __display_mobile_operator_count():
    print(mobile_operators_counter)


def select_file():
    file_paths = window.splitlist(filedialog.askopenfilenames(parent=window, title="Válaszd ki a fájlt",  initialdir=".", filetypes=[('Text files', '*.txt')]))
    for path in file_paths:
        with open(path) as f:
            for line in f:
                check_phonenumber(line)


def on_entry_click(event):
    if entry.get() == 'Telefonszám':
        entry.delete(0, "end")
        entry.insert(0, '')
        entry.config(fg = 'black')


def on_focusout(event):
    if entry.get() == '' and event.widget != entry: # Ha üres és nem az inputboxba kattint
        entry.insert(0, 'Telefonszám')
        entry.config(fg = 'grey')
        window.focus()


def open_gui():
    window.eval('tk::PlaceWindow . center') # Az ablak középre tétele
    window.mainloop()

window = tk.Tk()

window.title("Telefonszám ellenőrző") # Az ablak címének megadása

window.geometry("300x110")
window.resizable(width=0, height=0) 

# File kiválasztó gomb
button = tk.Button(window, text="Kiválasztás", command=select_file)
button.pack(padx=0, pady=10)

# Telefonszám inputbox
entry = tk.Entry(window)
entry.insert(0, 'Telefonszám')
entry.bind('<FocusIn>', on_entry_click) # Default szöveg törlése
entry.bind('<FocusOut>', on_focusout) # Default szöveg beírása
entry.config(fg = 'grey')
entry.pack(side=tk.LEFT, padx=10, pady=10)

window.bind("<Button-1>", on_focusout)
window.bind('<FocusOut>', on_focusout)

button = tk.Button(window, text='Ellenőrzés', command=__check_phonenumber)
button.pack(side=tk.LEFT, padx=10, pady=10)


button_list = tk.Button(window, text="Listázás", command=__display_mobile_operator_count)
button_list.place(x=232, y=65)