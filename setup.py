#!/usr/bin/env python
import sys
import os.path
import numpy
from cx_Freeze import setup, Executable

#Set up python directory and environment
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

files_to_include = [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), "wkhtmltopdf/", "examples/", "help.html", "style.css"]

#files_to_exclude = ['matplotlib', 'PyQt4', 'PyQt5', 'sqlalchemy', 'urllib', 'urllib2', 'sqlite3']

add_ons = ["pdfkit", "pandas.core", "numpy", "numpy.core._methods", "numpy.lib.format", "tkinter", "webbrowser"]

setup(name = "Water Well Record Collection Tool" ,
      version = "0.8" ,
      description = "This tool is intended to speed up the process of collecting water well PDFs from the DNR website" ,
      #options = {'build_exe': {'includes': add_ons}},
      author = 'W. Logan Downing',
      options = {
            'build_exe': {
                  #'excludes': files_to_exclude,
                  'include_files': files_to_include,
                  'packages': add_ons,
                  'optimize': 2,
            },
      },
      executables = [Executable("collect-and-capture-v2.py")],
      #executables = [Executable("collect-and-capture-v2.py", base="Win32GUI", icon="logo.ico")]
      )

      
