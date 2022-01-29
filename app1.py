import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")

        self.name = tk.StringVar()
        self.label1 = tk.Label(self, text = "Enter you name to go:")
        self.label1.pack(side=tk.TOP, expand=1, padx=10, pady=20)
        
        self.entry1 = tk.Entry(self, textvariable=self.name)
        self.entry1.pack(side=tk.TOP, expand=1, padx=(20, 20), pady=(0, 20))

        button1 = tk.Button(self, text="Press Me", command=self.print_me)
        button1.pack(side=tk.LEFT, expand=1, padx=(10, 10), pady=(10, 20))

    def print_me(self):
        print("Entered name: ", self.name)



if __name__=="__main__":
    window = Window()
    window.mainloop()