from tkinter import *
from tkinter.scrolledtext import ScrolledText

class ControlPanel(Frame):
    """A control panel is a Grapical User Interface for a user to interact with
    the rest of the project."""
    def __init__(self, master=None):
        super().__init__(master)
        #self.pack()
        self.create_widgets()
        
# ips, owner, filter, location, auto
    def create_widgets(self):
##        self.textarea = Button(None)
##        self.textarea.grid(column=0, row=0, columnspan=4)
##
##        self.test = Button(None)
##        self.test.grid(column=1, row=1, columnspan=4)
        
        self.ips = Button(None)
        self.ips["text"] = "Get IP's"
        self.ips["command"] = self.get_ips
        #self.ips.pack(side="top")
        #Label(master, text="Test").grid(row=0)
        
        labelIP = Label(text = "IP: ")
        labelIP.config(text="IP: ")
        labelIP.grid(row = 0, column=0)
        self.ips.grid(row = 0, column = 1)
        self.textarea = ScrolledText(self)
        self.textarea.grid(row = 0, column = 2)
        self.textarea.configure(state = "disabled")

        self.location = Button(None)
        self.location["text"] = "Get Location"
        self.location["command"] = self.find_location
        #self.location.pack(side="top")
        self.location.grid(row = 1, column = 1)
        labelLoc = Label(text = "Label: ")
        labelLoc.config(text = "Label: ")
        labelLoc.grid(row=1, column = 0)

        self.filter = Button(None)
        self.filter["text"] = "Filter Data"
        self.filter["command"] = self.filter_data
        #self.filter.pack(side="top")
        self.filter.grid(row = 2, column = 1)
        labelFilt = Label(text="Filter: ")
        labelFilt.config(text = "Filter: ")
        labelFilt.grid(row=2,column=0)

        self.owner = Button(None)
        self.owner["text"] = "Find Owner"
        self.owner["command"] = self.find_owner
        #self.owner.pack(side="top")
        self.owner.grid(row = 3, column = 1)
        labelOwner = Label(text = "Owner: ")
        labelOwner.config(text = "Owner: ")
        labelOwner.grid(row=3,column=0)

        self.auto = Button(None)
        self.auto["text"] = "Auto Generate"
        self.auto["command"] = self.auto
        #self.auto.pack(side="top")
        self.auto.grid(row = 4,  column = 1)
        labelAuto = Label(text = "Auto: ")
        labelAuto.config(text = "Auto: ")
        labelAuto.grid(row=4,column=0)
        
        self.quit = Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        #self.quit.pack(side="bottom")

    def get_ips(self):
        print("Getting IP's...")

        print("Done!")
    def find_location(self):
        print("Finding Location...")

        print("Done!")
    def filter_data(self):
        print("Filtering...")

        print("Done!")
    def find_owner(self):
        print("Finding owner...")

        print("Done!")
    def auto(self):
        self.get_ips(self)
        self.find_location(self)
        self.filter_data(self)
        self.find_owner(self)
        

if __name__ == "__main__":
    root = Tk()
    app = ControlPanel(master=root)
    app.mainloop()
