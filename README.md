# IN-DNR-Water-Well-Record-Collector
A basic python script that allows the user to select an input file of Well IDs and download all associated PDF files from the Indiana DNR into a specified folder.


This program was built using python 3.6


---SETUP---
First, run pip install -r requirements.txt from the project folder to install the necessary dependencies.
Once that has been completed, you'll need to install wkhtmltopdf version 0.12.4. It should install into C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe -->If that doesn't occur, you will need to modify the self.config variable for the program to work.
