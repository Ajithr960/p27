import tkinter as tk
from tkinter import messagebox
import re

class FormApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Form Submission")

        # Variables for form fields
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()

        # Labels and entry widgets for form fields
        tk.Label(master, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(master, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(master, text="Email:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(master, textvariable=self.email_var).grid(row=1, column=1, padx=10, pady=5)

        # Submit button
        tk.Button(master, text="Submit", command=self.submit_form).grid(row=2, column=0, columnspan=2, pady=10)

    def submit_form(self):
        name = self.name_var.get()
        email = self.email_var.get()

        if not name or not email:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Validate email using regular expression
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not email_pattern.match(email):
            messagebox.showerror("Error", "Invalid email address.")
            return

        # Form submission successful
        messagebox.showinfo("Success", "Form submitted successfully!")

def main():
    root = tk.Tk()
    app = FormApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
