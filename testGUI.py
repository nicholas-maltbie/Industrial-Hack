import tkinter as tk

class ControPanel(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.button = Button(self, text = "send")
        self.button.grid(column = 0, row = 0)

if __name__ == "__main__":
        root = tk.Tk()
        app = ControlPanel(master=root)
        app.mainloop()
