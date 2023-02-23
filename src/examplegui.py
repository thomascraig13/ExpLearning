
#! NEEDED LIBRARIES
import customtkinter
import tkinter
from tkinter import messagebox
from const import *

#! IMPORT SCRAPER FILE
from examplescraper import Scraper

class Example:

    def __init__(self,frame):
        #! MUST HAVE VARIABLES
        self.main = frame # the frame that the rest of the program is build on
        self.clicked = False # used to determine is GUI should be opened

        #* used to store entered search/location terms
        self.years = [] # empty list to hold search terms

        #* used to count total searches
        self.yearLine = 1 # keeps line count for textbox

    def gui(self):
        self.clicked=True

        # create frame that can be destroyed by main program
        self.frame = customtkinter.CTkFrame(self.main,width=560,fg_color='transparent')
        self.frame.grid(row=0, rowspan=10,column=1,columnspan = 2, sticky="nsew")

        self.frame.grid_rowconfigure(4)
        self.frame.grid_columnconfigure((1,2,3,4),weight=1)

        # search entry and location entry boxes for user input
        self.yearEntry = customtkinter.CTkEntry(self.frame,placeholder_text='Enter Year')
        self.yearEntry.grid(row=0,column=1,padx=(20,20),pady=(20,20),sticky='ew')
        self.yearTextbox = customtkinter.CTkTextbox(self.frame,width=250,state='disabled',font=TEXT_FONT)
        self.yearTextbox.grid(row=1,column=1,padx=(20,20),pady=(10,0),sticky='nsew')

        self.insertText = customtkinter.CTkButton(self.frame,text='Add',text_color=('gray10','#DCE4EE'),command=self.__insertTextButton)
        self.insertText.grid(row=0,column=3,padx=(20,10),pady=(10,0),sticky='ew')

        self.confirm = customtkinter.CTkButton(self.frame,text="Run query",text_color=("gray10", "#DCE4EE"),command=self.__confirmButton)
        self.confirm.grid(row=1, column=3, padx=(20, 10), pady=(10, 0), sticky="nsew")


    def unpack(self):
        if self.clicked:
            self.clicked = False
            self.frame.destroy()

    def __insertTextButton(self):

        self.yearTextbox.configure(state='normal') # unlock box temporarily

        if self.yearEntry.get() != '':

            self.yearTextbox.insert("end", f"{self.yearLine}. {self.yearEntry.get()}\n")
            self.years.append(self.yearEntry.get())
            self.yearEntry.delete(0,'end')
            self.yearLine += 1
        
        self.yearTextbox.configure(state='disabled') # lock box again


    def __confirmButton(self):

        self.__insertTextButton()

        cont = True
        error = ''

        message = 'Selected Years:\n'
        if len(self.years) > 0:
            for year in self.years:
                message+=(f'{year}\n')
        else:
            cont = False
            error += 'You must enter in a year!\n'


        # ask user yes or no if all data is found, else ask them to enter in the info needed
        if cont:
            confirm_message = tkinter.messagebox.askyesno(title='Confirmation',message=message,)

            if confirm_message:
                scraper = Scraper()

                for year in self.years:
                    print(f'Scraping {year}')
                    scraper.page_parse(year)

                scraper.create_file()
                print('Created file')