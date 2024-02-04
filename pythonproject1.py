import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer App")

        self.is_running = False
        self.counter = 0

        self.label = tk.Label(master, text="0", font=("Helvetica", 24))
        self.label.pack(pady=10)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.counter = 0
        self.label.config(text="0")

    def update_timer(self):
        if self.is_running:
            self.counter += 1
            self.label.config(text=str(self.counter))
            self.master.after(1000, self.update_timer)

def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
