import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Entry widget to display the result
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(master, textvariable=self.result_var, font=("Helvetica", 16), justify="right")
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Buttons for numbers and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Create buttons using a loop
        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, width=5, height=2, font=("Helvetica", 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

        # Configure grid weights for resizing
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        current_text = self.result_var.get()

        if value == '=':
            try:
                result = eval(current_text)
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current_text + value)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
