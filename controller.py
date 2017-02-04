import tkinter as tk

class ControlPanel(tk.Frame):
    """A control panel is a Grapical User Interface for a user to interact with
    the rest of the project."""
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ControlPanel(master=root)
    app.mainloop()

