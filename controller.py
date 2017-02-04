import tkinter as tk

class ControlPanel(tk.Frame):
    """A control panel is a Grapical User Interface for a user to interact with
    the rest of the project."""
    def __init__(self, master=None):
        super().__init__(master)
        #self.pack()
        self.create_widgets()
        
# ips, owner, filter, location, auto
    def create_widgets(self):

        self.textarea = tk.Button(self)
        self.textarea.grid(column=0, row=0, columnspan=4)

        self.test = tk.Button(self)
        self.test.grid(column=1, row=1, columnspan=4)
##        self.ips = tk.Button(self)
##        self.ips["text"] = "Get IP's"
##        self.ips["command"] = self.get_ips
##        #self.ips.pack(side="top")
##        #Label(master, text="Test").grid(row=0)
##        self.ips.grid(row = 0, column = 0)
##
##        self.location = tk.Button(self)
##        self.location["text"] = "Get Location"
##        self.location["command"] = self.find_location
##        #self.location.pack(side="top")
##
##        self.filter = tk.Button(self)
##        self.filter["text"] = "Filter Data"
##        self.filter["command"] = self.filter_data
##        #self.filter.pack(side="top")
##
##        self.owner = tk.Button(self)
##        self.owner["text"] = "Find Owner"
##        self.owner["command"] = self.find_owner
##        #self.owner.pack(side="top")
##
##        self.auto = tk.Button(self)
##        self.auto["text"] = "Auto Generate"
##        self.auto["command"] = self.auto
##        #self.auto.pack(side="top")
##        
##        self.quit = tk.Button(self, text="QUIT", fg="red",
##                              command=root.destroy)
##        #self.quit.pack(side="bottom")

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
    root = tk.Tk()
    app = ControlPanel(master=root)
    app.mainloop()
