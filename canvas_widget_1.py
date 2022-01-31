import tkinter as tk
from turtle import width

class main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")

        self.canvas1 = tk.Canvas(self, width=300, height=300, bg="white")
        self.canvas1.pack(side=tk.RIGHT,expand=1, padx=(20, 10), pady=(10, 10))

        self.canvas2 = tk.Canvas(self, width=300, height=300, bg="red")
        self.canvas2.pack(side=tk.LEFT, expand=1, padx=(10, 20), pady=(10, 10))


if __name__=="__main__":
    window = main_window()
    window.mainloop()