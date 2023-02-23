import customtkinter
import tkinter

#! IMPORT YOUR FILE AND CONSTANTS HERE
from const import *
from example2scraper import ExampleScraper

#! THIS IS JUST AN EXAMPLE, NOT WHAT THE GUI WILL BE

class ExampleTwo:

    def __init__(self,frame):
        #! LEAVE THESE 2 ATRIBUTES
        self.main = frame
        self.clicked = False

        #* DEFINE YOUR GUI VARIABLES HERE
        self.searchTerms = [] 
        self.locationTerms = [] 

        self.searchLine = 1 
        self.locationLine = 1 

    def gui(self):
        self.clicked=True #! SET TO TRUE

        #* CREATE YOUR GUI HERE, USING self.main AS YOUR FRAME THAT YOU'RE WORKING ON
        self.frame = customtkinter.CTkFrame(self.main,width=560,fg_color='transparent')
        self.frame.grid(row=0, rowspan=10,column=1,columnspan = 2, sticky="nsew")

        self.frame.grid_rowconfigure(4)
        self.frame.grid_columnconfigure((1,2,3,4),weight=1)

        # search entry and location entry boxes for user input
        self.searchEntry = customtkinter.CTkEntry(self.frame,placeholder_text='Search Term')
        self.searchEntry.grid(row=0,column=1,padx=(20,20),pady=(20,20),sticky='ew')
        self.searchTextbox = customtkinter.CTkTextbox(self.frame,width=250,state='disabled',font=TEXT_FONT)
        self.searchTextbox.grid(row=1,column=1,padx=(20,20),pady=(10,0),sticky='nsew')

        
        self.insertText = customtkinter.CTkButton(self.frame,text='Add',text_color=('gray10','#DCE4EE'),command=self.__insertTextButton)
        self.insertText.grid(row=0,column=3,padx=(20,20),pady=(20,20),sticky='ew')

        # checkboxes for extra information the user wants scraped
        self.checkboxFrame = customtkinter.CTkFrame(self.frame)
        self.checkboxFrame.grid(row=1,column=3,padx=(20,10),pady=(10,0),sticky='nsew')

        self.extraLinksVar = tkinter.IntVar(value=0)
        self.categoriesVar = tkinter.IntVar(value=0)

        self.checkLabel = customtkinter.CTkLabel(self.checkboxFrame,text='Extra Options',font=HEADER_FONT)
        self.checkLabel.grid(row=0,column=2,padx=10,pady=10,sticky='ew')

        self.extraLinks = customtkinter.CTkCheckBox(self.checkboxFrame,variable=self.extraLinksVar,text='Extra Links')
        self.extraLinks.grid(row=1,column=2,pady=10,padx=20,sticky='nw')

        self.categories = customtkinter.CTkCheckBox(self.checkboxFrame,variable=self.categoriesVar,text='Categories')
        self.categories.grid(row=2,column=2,pady=10,padx=20,sticky='nw')

        # confirm button to run the program query
        self.confirm = customtkinter.CTkButton(self.checkboxFrame,text='Run query',text_color=('gray10','#DCE4EE'),command=self.__confirmButton)
        self.confirm.grid(row=6,column=2,padx=(20,20),pady=(20,0),sticky='ew')

    #! THIS IS A MANDATORY METHOD FOR YOUR PROGRAM
    def unpack(self):
        if self.clicked:
            self.clicked = False
            self.frame.destroy() #! DESTROY YOUR VERSION OF THE FRAME, NOT self.main


    def __insertTextButton(self):

        self.searchTextbox.configure(state='normal') # unlock box temporarily

        if self.searchEntry.get() != '':

            self.searchTextbox.insert("end", f"{self.searchLine}. {self.searchEntry.get()}\n")
            self.searchTerms.append(self.searchEntry.get())
            self.searchEntry.delete(0,'end')
            self.searchLine += 1
        
        self.searchTextbox.configure(state='disabled') # lock box again

    def __confirmButton(self):
        scraper = ExampleScraper()    