import os
import sys
script="""
from cx_Freeze import setup, Executable
import sys
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "$FILENOTPY$",
    version = "1.0",
    description = "$FILENOTPY$",
    executables = [Executable("$FILENAME$",appendScriptToExe = False,appendScriptToLibrary = True,icon="icon.ico")]
    )"""

def main(filename):
    global script
    file=open("temp.py","wt")
    script=script.replace("$FILENAME$",filename)
    name=filename[:-3]
    script=script.replace("$FILENOTPY$",name)
    file.write(script)
    file.close()
    os.system("python temp.py build")
    os.remove("temp.py")
    input("\nDONE")

if __name__=="__main__":
    if len(sys.argv)==2:
        print("Starting build ->")
        print(sys.argv[1])
        main(sys.argv[1])
    else:
        print("No argument\n Pass: Filename")
