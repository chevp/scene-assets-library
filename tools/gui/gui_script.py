import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def convert_file(input_file, output_file, conversion_type):
    # Dummy conversion logic
    print(f"Converting {input_file} to {output_file} as {conversion_type}")
    messagebox.showinfo("Success", f"File converted and saved as {output_file}")

def open_file_dialog(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def save_file_dialog(entry):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv")
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def start_conversion():
    input_file = input_entry.get()
    output_file = output_entry.get()
    conversion_type = conversion_type_var.get()
    if not input_file or not output_file or not conversion_type:
        messagebox.showerror("Error", "Please complete all fields.")
        return
    convert_file(input_file, output_file, conversion_type)

# Setting up the tkinter window
root = tk.Tk()
root.title("File Conversion Tool")

# Input file selection
tk.Label(root, text="Input File:").grid(row=0, column=0)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=lambda: open_file_dialog(input_entry)).grid(row=0, column=2)

# Output file selection
tk.Label(root, text="Output File:").grid(row=1, column=0)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1)
tk.Button(root, text="Save As", command=lambda: save_file_dialog(output_entry)).grid(row=1, column=2)

# Conversion type dropdown
tk.Label(root, text="Conversion Type:").grid(row=2, column=0)
conversion_type_var = tk.StringVar()
conversion_options = ["json_to_csv", "jpeg_to_png"]
conversion_type_menu = tk.OptionMenu(root, conversion_type_var, *conversion_options)
conversion_type_menu.grid(row=2, column=1)

# Start conversion button
tk.Button(root, text="Convert", command=start_conversion).grid(row=3, column=1, pady=10)

root.mainloop()