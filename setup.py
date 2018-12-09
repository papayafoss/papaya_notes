from cx_Freeze import setup, Executable

base = None    

executables = [Executable("myfirstprog.py", base=base)]

packages = ["idna", "sys", "tkinter", "askopenfilename"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Papaya Notes",
    options = options,
    version = "1",
    description = 'Simple Notepad Application By Papayafoss',
    executables = executables
)
