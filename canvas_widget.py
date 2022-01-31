import tkinter as tk

from matplotlib.pyplot import fill

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Canvas Window")

        canvas_window = tk.Canvas(self, bg="white", width=300, height=300)
        canvas_window.pack()
        canvas_window.create_oval((0, 0, 300, 300), fill="yellow")
        canvas_window.create_arc((50, 100, 100, 150), extent=180, fill="black")
        canvas_window.create_arc((200, 100, 250, 150), extent=180, fill="black")
        canvas_window.create_line((50, 200, 110, 240), fill="red", width=5)
        canvas_window.create_line((110, 240, 190, 240), fill="red", width=5)
        canvas_window.create_line((190, 240, 250, 200), fill="red", width=5)


if __name__=="__main__":
    window = Window()
    window.mainloop()