import customtkinter
from const import *

# * IMPORT YOUR FILE/CLASS HERE
from examplegui import Example
from example2gui import ExampleTwo

#! set customtkinter appearances
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


class Main:
    def __init__(self):
        #! initialize the main GUI (do not touch)
        self.main = customtkinter.CTk()
        self.main.geometry("1200x700")
        self.main.title("Top Movies by Year")
        self.main.grid_columnconfigure(1, weight=1)
        self.main.grid_rowconfigure(1, weight=1)

        #! frame that is sent to external GUI files (do not touch, unless more rows are needed)
        self.frame = customtkinter.CTkFrame(self.main, fg_color="transparent")
        self.frame.configure(width=1200, height=700)
        self.frame.grid(row=1, column=1, sticky="nsew")
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure((2, 3), weight=0)
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        #* INITIALIZE YOUR CLASS HERE, PASS self.frame AS YOUR WORKING SPACE
        self.e = Example(self.frame)
        self.e_two = Example(self.frame)

        #! create the sidebar
        self.sidebar(self.frame)

        #! run the Main GUI
        self.main.mainloop()

    def sidebar(self, frame):
        self.sidebar_frame = customtkinter.CTkFrame(frame, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        self.sidebar_frame.grid_columnconfigure((1,2,3),weight=0)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Top Movies by Year", font=TITLE_FONT)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        #* CREATE YOUR BUTTON HERE, PUT BUTTON ON NEXT ROW DOWN IN GRID
        #! EXAMPLE GUI

        self.ex = customtkinter.CTkButton(self.sidebar_frame, text="Example", command=self.example)  #! YOU NEED TO CREATE A METHOD IN THIS FILE TO CALL YOUR GUI
        self.ex.grid(row=3, pady=10)

        self.ex_two = customtkinter.CTkButton(self.sidebar_frame, text="Example Two", command=self.example_two)  #! YOU NEED TO CREATE A METHOD IN THIS FILE TO CALL YOUR GUI
        self.ex_two.grid(row=4, pady=10)


    #* YOUR GUI CALLING METHOD GOES HERE

    #! EXAMPLE!
    def example(self):
        if not self.e.clicked:
            self.e = Example(self.frame) #! RECREATE YOUR CLASS INSTANCE ON THE SAME VARIABLE, DESTROYS THE OLD VERSION TO CLEAN UP MEMORY

            #! UNPACK ANY OTHER GUIs HERE
            self.e_two.unpack()

            #! call your gui
            self.e.gui()

    def example_two(self):
        if not self.e_two.clicked:
            self.e_two = ExampleTwo(self.frame) #! RECREATE YOUR CLASS INSTANCE ON THE SAME VARIABLE, DESTROYS THE OLD VERSION TO CLEAN UP MEMORY

            #! UNPACK ANY OTHER GUIs HERE
            self.e.unpack()

            #! call your gui
            self.e_two.gui()


#! run the class
if __name__ == "__main__":
    Main()
