import sys
import os.path
import numpy
from cx_Freeze import setup, Executable

add_ons = ["pdfkit", "pandas", "numpy", "numpy.core._methods", "numpy.lib.format", "tkinter", "webbrowser"]

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

setup(name = "Water Well Record Collection Tool" ,
      version = "0.8" ,
      description = "This tool is intended to speed up the process of collecting water well PDFs from the DNR website" ,
      #options = {'build_exe': {'includes': add_ons}},
      options = {
            'build_exe': {
                  'include_files':[
                        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                  ],
                  'packages': add_ons,
            }
      },
      executables = [Executable("collect-and-capture-v2.py")]
      )
      #executables = [Executable("collect-and-capture-v2.py", base="Win32GUI")])
