from tkinter import *
from tkinter.scrolledtext import ScrolledText
from webreader import *

class ControlPanel(Frame):
    """A control panel is a Grapical User Interface for a user to interact with
    the rest of the project."""
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        
    def create_widgets(self):
        """Creates the GUI interface aspects.""" 
        # Generates title.
        title = "OSINTICS For 500 - 00101010"
        root.wm_title(title)
        csv_label = Label(text="Input CSV File")
        csv_label.grid(row=0,column=0)
        self.icsv = Entry(root)
        self.icsv.grid(row=1, column=0)
        blacklist_label = Label(text="Blacklist Info")
        blacklist_label.grid(row=2,column=0)
        self.blacklist = Entry(root)
        self.blacklist.grid(row=3, column=0)
        output_label = Label(text="Output CSV Filename")
        output_label.grid(row=4,column=0)
        self.output = Entry(root)
        self.output.grid(row=5, column=0)

        # Booleans for checkboxes.
        self.var1 = IntVar()
        self.var1.set(1)
        self.var2 = IntVar()
        self.var2.set(1)
        self.var3 = IntVar()
        self.var3.set(1)
        self.var4 = IntVar()
        self.var4.set(1)
        self.var5 = IntVar()
        self.var5.set(1)
        self.var6 = IntVar()
        self.var6.set(1)

        # Generate checkbox buttons for location.
        self.location = Checkbutton(root, text='Locations', variable=self.var1)
        self.name = Checkbutton(root, text='Names', variable=self.var2)
        self.email = Checkbutton(root, text='Emails', variable=self.var3)
        self.phone = Checkbutton(root, text='Phones', variable=self.var4)
        self.address = Checkbutton(root, text='Address', variable=self.var5)
        self.threat = Checkbutton(root, text='Threats', variable=self.var6)
        
        # Enable checkboxes with buttons.
        self.location["command"] = self.find_location
        self.location.grid(row = 0, column = 1)
        self.name["command"] = self.find_name
        self.name.grid(row = 1, column = 1)
        self.email["command"] = self.find_email
        self.email.grid(row = 2, column = 1)
        self.phone["command"] = self.find_phone
        self.phone.grid(row = 3,  column = 1)
        self.address["command"] = self.find_address
        self.address.grid(row = 4, column = 1)
        self.threat["command"] = self.find_threat
        self.threat.grid(row = 5,  column = 1)
        
        # Create go and quit buttons.
        self.go = Button(root, text="GO", fg='green', command=self.go_exec)
        self.go.grid(row = 2, column = 3)
        self.quit = Button(root, text="QUIT", fg='red', command=root.destroy)
        self.quit.grid(row = 4, column = 3)

    def find_location(self):
        """Adds locations."""
        if self.var1.get():
            print("Finding Location...")

    def find_name(self):
        """Adds names."""
        if self.var2.get():
            print('Name')

    def find_email(self):
        """Adds emails."""
        if self.var3.get():
            print("Finding owner...")

    def find_phone(self):
        """Adds phones."""
        if self.var4.get():
            print("Phones")

    def find_address(self):
        """Adds address."""
        if self.var5.get():
            print("Address")

    def find_threat(self):
        """Adds threats."""
        if self.var6.get():
            print("Threats")

    def go_exec(self):
        self.find_location(self)
        self.find_name(self)
        self.find_email(self)
        self.find_phone(self)
        self.find_address(self)
        self.find_threat(self)

if __name__ == "__main__":
    root = Tk()
    app = ControlPanel(master=root)
    app.mainloop()
