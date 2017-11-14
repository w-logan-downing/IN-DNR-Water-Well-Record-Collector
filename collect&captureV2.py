import pdfkit
import pandas as pd #for reading the excel file for well IDs
#note: pandas relies on xldr
from tkinter import *
from tkinter import filedialog

class Window(Frame):
    def __init__(self, master=None): #define the main window
        Frame.__init__(self, master) #initialize the window
        self.master = master #assign the main frame to a variable

        self.init_window() #a window inside of the frame for our application
        self.allWellIDs = pd.DataFrame([]) #instantiate the data frame for well ids

        #---Setup wkhtmltopdf options and configuration---#
        #specify the path to wkhtmltopdf for pdfkit
        self.config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        #remove the grayed background to print report to a plain white sheet.
        self.options = {'no-background': ''}

    def init_window(self):
        self.master.title("IDEM Water Well Record Collector") #set the title of the window (located inside of the frame)
        self.pack(fill=BOTH, expand=1) #allow the window to occupy the whole frame

        mainMenu = Menu(self.master) #Menu of the main window
        self.master.config(menu=mainMenu) #defines the instance of the menu

        #---Build out the menu button file---#
        file = Menu(mainMenu) #define the instance of file
        file.add_command(label='Exit', command=self.client_exit)
        mainMenu.add_cascade(label='File', menu=file)

        #---Build out the menu button edit---#
        #edit = Menu(mainMenu)
        #edit.add_command(label='Undo')
        #mainMenu.add_cascade(label='Edit', menu=edit)

        #quitButton = Button(self, text='Exit', command=self.displayDir)
        #quitButton.place(x=400, y=200)
        #---Build out the browse button to allow user to get data---#
        browseButton = Button(self, text='Browse', command=self.browseFunc)
        browseButton.place(x=400, y=200)

        #---Build the start button---#
        startButton = Button(self, text="Collect Records", command=self.collect)
        startButton.place(x=380, y=300)
        

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
        for i in range(len(self.allWellIDs)):
            wellID = self.allWellIDs[i]
            url = 'https://secure.in.gov/apps/dnr/water/dnr_waterwell?refNo=' + wellID + '&_from=SUMMARY&_action=Details' #create the url to turn into a pdf
            fileDestination = destination + '/' + wellID + '.pdf' #append the well ID to the destination folder
            pdfkit.from_url(url, fileDestination , options= self.options, configuration=self.config) #get the webpage

        print("All PDF files have been saved to the specified folder")
        

    def client_exit(self):
        exit()

root = Tk()
root.geometry("800x600") #set the default frame size
app = Window(root)

root.mainloop() #starts the window