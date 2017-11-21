# IN-DNR-Water-Well-Record-Collector
A basic python script that allows the user to select an input file of Well IDs and download all associated PDF files from the Indiana DNR into a specified folder.


This program was built using python 3.6


<h2>---SETUP---</h2>
<ul>
  <li>First, run pip install -r requirements.txt from the project folder to install the necessary dependencies.</li>
  <li>Install wkhtmltopdf version 0.12.4. It should install into C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe -->If that doesn't occur, you will need to modify the self.config variable for the program to work.
  <br>NOTE: On 64 bit systems, wkhtmltopdf will install in C:/Program Files (x86)/wkhtmltopdf/bin/wkhtmltopdf.exe, the self.config variable in the script will need to be updated to reflect this difference.
  </li>
</ul>
<br>
You should be ready to begin downloading DNR water well records in PDF format!
