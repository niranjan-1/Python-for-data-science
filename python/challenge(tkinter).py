try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

keys = [[('C',1),("CE",1)],
        [('7',1),("8",1),("9",1),("+",1)],
        [('4',1),("5",1),("6",1),("-",1)],
        [('1',1),("2",1),("3",1),("*",1)],
        [('0',1),("=",1),("/",1)],
        ]
mainWindowPadding=8
mainWindow= tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("640x480-8-200")
mainWindow['padx']= mainWindowPadding
#mainWindow["background"]="black"

#entry configurations
result= tkinter.Entry(mainWindow)
result.grid(row=0,column=0,sticky='nsew')

# buttons
keypad =tkinter.Frame(mainWindow)
keypad.grid(row=1,column=0,stick='nsew')

row=0
for keyRow in keys:
    col=0
    for key in keyRow:
        tkinter.Button(keypad,text=key[0]).grid(row=row, column=col, columnspan=key[1],sticky=tkinter.E + tkinter.W)
        col = key[1]
    row+=1

mainWindow.mainloop()
