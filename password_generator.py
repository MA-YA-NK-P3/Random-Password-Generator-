import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Password Length:").pack(pady=5)
        self.length_var = tk.IntVar(value=12)
        self.length_scale = tk.Scale(self.root, from_=6, to=32, orient="horizontal", variable=self.length_var)
        self.length_scale.pack()

        # Checkboxes for complexity options
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=False)

        tk.Checkbutton(self.root, text="Include Uppercase (A-Z)", variable=self.uppercase_var).pack(anchor="w", padx=20)
        tk.Checkbutton(self.root, text="Include Lowercase (a-z)", variable=self.lowercase_var).pack(anchor="w", padx=20)
        tk.Checkbutton(self.root, text="Include Digits (0-9)", variable=self.digits_var).pack(anchor="w", padx=20)
        tk.Checkbutton(self.root, text="Include Symbols (!@#...)", variable=self.symbols_var).pack(anchor="w", padx=20)

        tk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=10)

        self.password_entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.password_entry.pack(pady=10, padx=20, fill="x")

        self.copy_btn = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_btn.pack()

        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.pack()

    def generate_password(self):
        length = self.length_var.get()
        char_pool = ""

        if self.uppercase_var.get():
            char_pool += string.ascii_uppercase
        if self.lowercase_var.get():
            char_pool += string.ascii_lowercase
        if self.digits_var.get():
            char_pool += string.digits
        if self.symbols_var.get():
            char_pool += string.punctuation

        if not char_pool:
            messagebox.showwarning("Selection Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(char_pool) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.status_label.config(text="")

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.status_label.config(text="Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
