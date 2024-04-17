import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length, complexity):
    if complexity == "1. Easy":
        characters = string.ascii_letters
    elif complexity == "2. Medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "3. Hard":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        messagebox.showerror("Error", "Invalid complexity level choice. Please choose from options 1, 2, or 3.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def generate_and_copy_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    
    password = generate_password(length, complexity)
    if password:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo("Password Generated", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Complexity label and dropdown
complexity_label = tk.Label(root, text="Complexity Level:")
complexity_label.grid(row=1, column=0, padx=10, pady=5)
complexity_var = tk.StringVar(root)
complexity_dropdown = tk.OptionMenu(root, complexity_var, "1. Easy", "2. Medium", "3. Hard")
complexity_dropdown.grid(row=1, column=1, padx=10, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_and_copy_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Generated password label and entry
password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=3, column=0, padx=10, pady=5)
password_entry = tk.Entry(root)
password_entry.grid(row=3, column=1, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
