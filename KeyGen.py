import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import random
import string
import csv
import os

def generate_license_keys(length, include_numbers, amount):
    choices = string.ascii_uppercase
    if include_numbers:
        choices += string.digits
    return [''.join(random.choice(choices) for _ in range(length)) for _ in range(amount)]

def save_keys_to_file(keys, file_path, file_type):
    try:
        if file_type == 'CSV':
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for key in keys:
                    writer.writerow([key])
        elif file_type == 'TXT':
            with open(file_path, 'w') as txtfile:
                for key in keys:
                    txtfile.write(f"{key}\n")
        messagebox.showinfo("Success", f"Keys have been successfully generated and saved to {file_path}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_file_location():
    filepath = filedialog.askdirectory()
    if filepath:
        file_location_entry.set(filepath)

def on_generate_keys():
    length = int(key_length_slider.get())
    include_numbers = include_numbers_var.get()
    amount = int(key_amount_slider.get())
    file_type = file_type_var.get().upper()
    file_path = file_location_entry.get()

    if not file_path or file_type == "Select File Type":
        messagebox.showwarning("Warning", "Please select a file location and type.")
        return

    keys = generate_license_keys(length, include_numbers, amount)
    file_extension = 'csv' if file_type == 'CSV' else 'txt'
    file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + f".{file_extension}"
    full_path = os.path.join(file_path, file_name)

    save_keys_to_file(keys, full_path, file_type)

def switch_theme():
    if theme_var.get() == "Light":
        app.set_theme("dark")
        theme_var.set("Dark")
    else:
        app.set_theme("light")
        theme_var.set("Light")

app = ctk.CTk()

ctk.CTkLabel(app, text="License Key Generator").pack(pady=10)

ctk.CTkLabel(app, text="by VHSQ").pack(pady=10)

file_type_var = tk.StringVar(value="Select File Type")
file_type_dropdown = ctk.CTkComboBox(app, values=["TXT", "CSV"], variable=file_type_var)
file_type_dropdown.pack(pady=10)

file_location_entry = tk.StringVar(value="")
file_location_widget = ctk.CTkEntry(app, textvariable=file_location_entry)
file_location_widget.pack(pady=10)

browse_button = ctk.CTkButton(app, text="Browse", command=save_file_location)
browse_button.pack(pady=10)

ctk.CTkLabel(app, text="Key Length").pack(pady=(20, 0))
key_length_slider = ctk.CTkSlider(app, from_=4, to=30)
key_length_slider.set(16)
key_length_slider.pack(pady=5)
key_length_value_label = ctk.CTkLabel(app, text=f"Current Length: {key_length_slider.get()}")
key_length_value_label.pack(pady=(0, 10))
def update_key_length_label(value):
    key_length_value_label.configure(text=f"Current Length: {int(float(value))}")
key_length_slider.configure(command=update_key_length_label)

ctk.CTkLabel(app, text="Amount of Keys").pack(pady=(10, 0))
key_amount_slider = ctk.CTkSlider(app, from_=1, to=100)
key_amount_slider.set(10)
key_amount_slider.pack(pady=5)
key_amount_value_label = ctk.CTkLabel(app, text=f"Amount: {key_amount_slider.get()}")
key_amount_value_label.pack(pady=(0, 20))
def update_key_amount_label(value):
    key_amount_value_label.configure(text=f"Amount: {int(float(value))}")
key_amount_slider.configure(command=update_key_amount_label)

include_numbers_var = tk.BooleanVar(value=True)
include_numbers_checkbox = ctk.CTkSwitch(app, text="Include Numbers", variable=include_numbers_var)
include_numbers_checkbox.pack(pady=10)

generate_button = ctk.CTkButton(app, text="Generate Keys", command=on_generate_keys)
generate_button.pack(pady=20)

theme_var = tk.StringVar(value="Light")
theme_switch = ctk.CTkSwitch(app, textvariable=theme_var, command=lambda: switch_theme())
theme_switch.pack(pady=20)

app.mainloop()
