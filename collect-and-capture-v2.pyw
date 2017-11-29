import pdfkit
import numpy
import pandas as pd #for reading the excel file for well IDs
#note: pandas relies on xldr
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import webbrowser

class Window(Frame):
    def __init__(self, master=None): #define the main window
        Frame.__init__(self, master) #initialize the window
        self.master = master #assign the main frame to a variable

        self.init_window() #a window inside of the frame for our application
        self.allWellIDs = pd.DataFrame([]) #instantiate the data frame for well ids

        #---Setup wkhtmltopdf options and configuration---#
        #specify the path to wkhtmltopdf for pdfkit
        #(add (x86) for 64 bit systems)
        self.config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe')
        #remove the grayed background to print report to a plain white sheet.
        self.options = {'no-background': ''}

        #---Display instructions at top---#
        self.info = Label(self, text="Use the browse button to select a data source\nand the Collect Records button to select\nan output location.")
        self.info.pack(side=TOP)

        #---Establish the progressbar---#
        #self.progress = ttk.Progressbar(self, orient='horizontal', length=250, mode='indeterminate')
        #self.progress.pack(side=BOTTOM, pady=(0, 50))

    def init_window(self):
        self.master.title("IDEM Water Well Record Collector") #set the title of the window (located inside of the frame)
        self.pack(fill=BOTH, expand=1) #allow the window to occupy the whole frame

        mainMenu = Menu(self.master) #Menu of the main window
        self.master.config(menu=mainMenu) #defines the instance of the menu

        #---Build out the menu button file---#
        file = Menu(mainMenu) #define the instance of file
        file.add_command(label='Exit', command=self.client_exit)
        mainMenu.add_cascade(label='File', menu=file)

        #--Build out the help button---#
        mainMenu.add_command(label='Help', command=self.openURL) #goes to html doc

        #---Build out the browse button to allow user to get data---#
        browseButton = Button(self, text='Browse', command=self.browseFunc)
        browseButton.place(x=210, y=100)

        #---Build the start button---#
        startButton = Button(self, text="Collect Records", command=self.collect)
        startButton.place(x=210, y=150)


    #---Gets source data from user specified file---#
    def browseFunc(self):
        fileName = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("excel files","*.xlsx;*.xls"),("all files","*.*")))
        data = fileName #store the path of the user's data file
        df = pd.read_excel(data) #store excel file in a dataframe
        self.allWellIDs = df['Well ID'].values #store IDs to a numpy array
        self.allWellIDs = self.allWellIDs.astype(str) #converts values into strings for concatenation later
        self.allWellIDs = self.allWellIDs[~pd.isnull(self.allWellIDs)] #remove nan values


    def collect(self):
        destination = filedialog.askdirectory()

        #self.progress.maximum = len(self.allWellIDs)
        #self.progress.start()
        #---Initialize a progress counter---#
        counter = 0
        self.filesConverted = Label(self, text= str(counter) + '/' + str(len(self.allWellIDs)))
        self.filesConverted.pack(side=BOTTOM, pady=(0,10))

        for i in range(len(self.allWellIDs)):
            wellID = self.allWellIDs[i]
            url = 'https://secure.in.gov/apps/dnr/water/dnr_waterwell?refNo=' + wellID + '&_from=SUMMARY&_action=Details' #create the url to turn into a pdf
            fileDestination = destination + '/' + wellID + '.pdf' #append the well ID to the destination folder
            pdfkit.from_url(url, fileDestination , options= self.options, configuration=self.config) #get the webpage
            #self.progress.step([])
            self.filesConverted.pack_forget() #delete the current label for new label
            #root.update() #update UI to remove
            counter += 1
            self.filesConverted = Label(self, text= str(counter) + '/' + str(len(self.allWellIDs)))
            self.filesConverted.pack(side=BOTTOM, pady=(0,10))
            root.update()

        #self.progress.stop()
        self.completedText = Label(self, text="All PDF files have been saved to the specified folder")
        self.completedText.pack(side=BOTTOM, pady=(0, 0))


    def client_exit(self):
        exit()

    def openURL(self):
        webbrowser.open("help.html")

root = Tk()
root.geometry("320x280") #set the default frame size
app = Window(root)

root.mainloop() #starts the window
