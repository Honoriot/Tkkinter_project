import tkinter as tk
import tkinter.messagebox as msg

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")

        self.name = tk.StringVar()
        self.label1 = tk.Label(self, text = "Enter you name to go:")
        self.label1.pack(fill=tk.BOTH, expand=1, padx=10, pady=20)
        
        self.entry1 = tk.Entry(self, textvariable=self.name, text="NAME")
        self.entry1.pack(fill=tk.BOTH, expand=1, padx=(20, 20), pady=(0, 20))

        button1 = tk.Button(self, text="Hello", command=self.fun_right)
        button1.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

        button1 = tk.Button(self, text="Quit", command=self.fun_left)
        button1.pack(side=tk.RIGHT, padx=(00, 20), pady=(0, 20))

    def fun_right(self):
        msg.showinfo("Hello", "Hello, " + self.entry1.get() + ".")

    def fun_left(self):
        if msg.askyesno("Quit Box", self.entry1.get() + ", are you really want to quit.") :
            self.after(1000, self.destroy)
        else:
            self.label1.configure(text="Next Enter:")



if __name__=="__main__":
    window = Window()
    window.mainloop()