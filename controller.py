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

        # Draw button for IP Scrolledtext
        self.textarea = ScrolledText(self).grid(row = 0, column = 2)

        # Creates empty list for entry boxes.
        self.entry_list = []
        labels = []
        items_str = ["IP", "Location", "Filter", "Owner", "Auto"]
        
        for num in range(len(items_str)):
            # Generates entry text boxes
            self.entry_list.insert(num, Entry(root))
            self.entry_list[num].grid(row = num, column = 3)
            
            # Generates labels.
            labels.insert(num, Label(text = items_str[num] + ": "))
            labels[num].grid(row=num, column = 0)

        # Generate button for location.
        self.ips = Button(None)
        self.location = Button(None)
        self.filter = Button(None)
        self.owner = Button(None)
        self.auto = Button(None)
        self.quit = Button(root, text="QUIT", fg='red', command=root.destroy)
        self.quit.grid(row = 5, column = 3)

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
        try:
            filename = self.entry_list[0].get() 
            print("Getting IP's...")
            for i in range(len(get_ips_from_file(filename))):
                if (i % 4 == 0):
                    print(get_ips_from_file(filename)[i])
                else:
                    pass
            print("Done!")
        except FileNotFoundError:
            print('Please enter a valid CSV file.')

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
