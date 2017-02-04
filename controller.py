from tkinter import *
from tkinter.scrolledtext import ScrolledText
import webreader

class ControlPanel(Frame):
    """A control panel is a Grapical User Interface for a user to interact with
    the rest of the project."""
    def __init__(self, master=None):
        super().__init__(master)
        #self.pack()
        self.create_widgets()
        
# ips, owner, filter, location, auto
    def create_widgets(self):
        """Creates the buttons.""" 
        # Generates title.
        root.wm_title("OSINTICS for 500")

        # Draw button for IP
        self.textarea = ScrolledText(self).grid(row = 0, column = 2)

        # Creates empty list for entry boxes.
        entry_list = []
        labels = []
        items_str = ["IP", "Location", "Filter", "Owner", "Auto"]
        
        for num in range(5):
            # Generates entry text boxes
            entry_list.insert(num, Entry(root))
            entry_list[num].grid(row = num, column = 3)

            # Generates labels.
            labels.insert(num, Label(text = items_str[num] + ": "))
            labels[num].grid(row=num, column = 0)

        # Generate button for location.
        self.ips = Button(None)
        self.location = Button(None)
        self.filter = Button(None)
        self.owner = Button(None)
        self.auto = Button(None)
        self.quit = Button(self, text="QUIT", fg="red", command=root.destroy)

        self.ips["text"] = "Get IPs"
        self.location["text"] = "Get Location"
        self.filter["text"] = "Filter Data"
        self.owner["text"] = "Find Owner"
        self.auto["text"] = "Auto Generate"

        self.ips["command"] = self.get_ips
        self.ips.grid(row = 0, column = 1)
        self.location["command"] = self.find_location
        self.location.grid(row = 1, column = 1)
        self.filter["command"] = self.filter_data
        self.filter.grid(row = 2, column = 1)
        self.owner["command"] = self.find_owner
        self.owner.grid(row = 3, column = 1)
        self.auto["command"] = self.auto
        self.auto.grid(row = 4,  column = 1)
        

    def get_ips(self):
        """Grabs the IP and prints."""
        print("Getting IP's...")

        print("Done!")
    def find_location(self):
        """Grabs the location and prints."""
        print("Finding Location...")

        print("Done!")
    def filter_data(self):
        """Filters the data, printing."""
        print("Filtering...")

        print("Done!")
    def find_owner(self):
        """Finds the owner and prints."""
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
