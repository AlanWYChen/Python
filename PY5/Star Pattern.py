#Author: Alan
#Date: October 20
#Purpose: Output star patterns
#=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from tkinter import *

#global variables
interface = Tk()
interface.geometry("680x377+0+0")
interface.title("Pattern Generator")

intShape = IntVar()
intShape.set(0)

intSize = IntVar()
intSize.set(1)

intType = IntVar()
intType.set(0)

#functions/procedures

#author: Alan
#date: October 25
#purpose: draw the shape depending on what the user selected
#parameter: N/A
#return: N/A
def draw():
    txtDisplay.configure(state=NORMAL)
    if intShape.get()==0:
        if intType.get()==0:
            for x in range(0, intSize.get()):
                txtDisplay.insert(END, "* "*intSize.get())
                txtDisplay.insert(END, "\n")
        else:
            for x in range(0, intSize.get()):
                for y in range(0, intSize.get()):
                    if x == 0 or x == intSize.get()-1 \
                       or y == 0 or y == intSize.get() -1:
                        txtDisplay.insert(END, "* ")
                    else:
                        txtDisplay.insert(END, "  ")
                txtDisplay.insert(END, "\n")
    elif intShape.get()==1:
        if intType.get()==0:
            for x in range(1,intSize.get()+1):
                for y in range(0,x):
                    txtDisplay.insert(END, "* ")
                txtDisplay.insert(END, "\n")
        else:
            for x in range(1,intSize.get()+1):
                for y in range(0,x):
                    if y == 0 or y == x-1 or x == intSize.get():
                        txtDisplay.insert(END, "* ")
                    else:
                        txtDisplay.insert(END, "  ")
                txtDisplay.insert(END, "\n")
    elif intShape.get()==2:
        intMarker = 1
        if intType.get()==0:
            for x in range(0,intSize.get()):
                for space in range(0,(intSize.get()-intMarker)//2):
                    txtDisplay.insert(END, "  ")
                for y in range(0,intMarker):
                    txtDisplay.insert(END, "* ")
                if x+1<intSize.get()//2+1:
                    intMarker = intMarker + 2
                else:
                    intMarker = intMarker - 2
                txtDisplay.insert(END, "\n")
        else:
            for x in range(0,intSize.get()):
                for space in range(0,(intSize.get()-intMarker)//2):
                    txtDisplay.insert(END, "  ")
                for y in range(0,intMarker):
                    if y == 0 or y == intMarker-1:
                        txtDisplay.insert(END, "* ")
                    else:
                        txtDisplay.insert(END, "  ")
                if x+1<intSize.get()//2+1:
                    intMarker = intMarker + 2
                else:
                    intMarker = intMarker - 2
                txtDisplay.insert(END, "\n")
    else:
        output = [["  " for i in range(intSize.get()*3)] \
                  for j in range(intSize.get()*2+1)]
        if intType.get()==0:
            for x in range (intSize.get()*2+1):
                for y in range (intSize.get()):
                    output[x][x+y] = "* "
            for x in range (intSize.get()*2+1):
                for y in range (intSize.get()*3-1, intSize.get()*2-1, -1):
                    output[x][y-x] = "* "
            for x in range (intSize.get()*2+1):
                for y in range (intSize.get()*3):
                    txtDisplay.insert(END, output[x][y])
                txtDisplay.insert(END, "\n")
        else:
            for x in range (intSize.get()*2+1):
                for y in range (intSize.get()):
                    if x==0 or x==intSize.get()*2 or y==0 or \
                       y==intSize.get()-1:
                        output[x][x+y] = "* "
            for x in range (intSize.get()*2+1):
                for y in range (intSize.get()*3-1, intSize.get()*2-1, -1):
                    if x==0 or x==intSize.get()*2 or y==intSize.get()*3-1 \
                       or y==intSize.get()*2:
                        output[x][y-x] = "* "
            for x in range (intSize.get()*2+1):
                for y in range (intSize.get()*3):
                    txtDisplay.insert(END, output[x][y])
                txtDisplay.insert(END, "\n")

    txtDisplay.configure(state=DISABLED)
    btnClear.configure(state=NORMAL)
    btnDraw.configure(state=DISABLED)

#author: Alan
#date: Octber 25
#purpose: clear the textbox
#parameter: N/A
#return: N/A
def clear():
    txtDisplay.configure(state=NORMAL)
    txtDisplay.delete("1.0", END)
    txtDisplay.configure(state=DISABLED)
    btnDraw.configure(state=NORMAL)

#author: Alan
#date: Octber 25
#purpose: edit for odd-only or below 8
#parameter: n
#return: N/A
def editDorC(n):
    if intShape.get()==2:
        sclSize.config(to = 23)
        past = 0
        n = int(n)
        if not n%2:
            if n>past:
                sclSize.set(n+1)
            else:
                sclSize.set(n-1)
    elif intShape.get()==3:
        sclSize.config(to = 7)
        n = int(n)
        if n>7:
            sclSize.set(7)
    else:
        sclSize.config(to = 23)

#main
frmShape = Frame (interface, relief="groove", \
                  borderwidth = 2, height = 235, width = 160, bg = "blue")
frmShape.place(x = 5, y = 5)

lblShapeTitle = Label (frmShape, text = "Shape", height=2, width=15, \
                bg = "light grey", relief=RIDGE)
lblShapeTitle.place(x = 7, y = 5)

rdbSquare = Radiobutton(frmShape, text="Square", variable=intShape, \
            value=0, width = 15, height = 2, \
            command = lambda:editDorC(intSize.get()))
rdbSquare.place(x = 7, y = 50)

rdbTriangle = Radiobutton(frmShape, text="Triangle", variable=intShape, \
              value=1, width = 15, height = 2, \
              command = lambda:editDorC(intSize.get()))
rdbTriangle.place(x = 7, y = 95)

rdbDiamond = Radiobutton(frmShape, text="Diamond", variable=intShape, \
             value=2, width = 15, height = 2, \
             command = lambda:editDorC(intSize.get()))
rdbDiamond.place(x = 7, y = 140)

rdbCross = Radiobutton(frmShape, text="Cross", variable=intShape, \
           value=3, width = 15, height = 2, \
           command = lambda:editDorC(intSize.get()))
rdbCross.place(x = 7, y = 185)

lblSize = Label(interface, text = "Size of the pattern", width = 15, \
          height = 2, bg = "light grey", relief="groove")
lblSize.place(x = 190, y = 10)

sclSize = Scale(interface, from_ = 1, to = 23, width = 15, orient=HORIZONTAL, \
          variable = intSize, length = 138, command= editDorC, relief="groove")
sclSize.place(x = 190 , y = 49)

frmType = Frame (interface, relief="groove", \
          borderwidth = 2, height = 150, width = 140, bg = "blue")
frmType.place(x = 190, y = 90)

lblTypeTitle = Label (frmType, text = "Type", height=2, width=13, \
                bg = "light grey" ,relief=RIDGE)
lblTypeTitle.place(x = 6, y = 5)

rdbSolid = Radiobutton (frmType, text = "Solid", variable = intType, \
           value = 0, height=2, width = 13)
rdbSolid.place(x = 6, y = 50)

rdbHollow = Radiobutton (frmType, text = "Hollow", variable = intType, \
            value = 1, height=2, width = 13)
rdbHollow.place(x = 6, y = 100)

txtDisplay = Text (interface, width = 46, height = 24, bg = "light grey", \
             state = DISABLED, wrap=WORD)
txtDisplay.place(x = 345, y = 5)

btnDraw = Button(interface, text = "Draw", command=lambda: draw(), \
          width = 33, height = 2)
btnDraw.place(x = 5, y = 245)

btnClear = Button(interface, text = "Clear", command=lambda: clear(), \
           width = 33, height = 2)
btnClear.place(x = 5, y = 285)

btnExit = Button(interface, text = "Exit", command=lambda: \
          interface.destroy(), width = 33, height = 2)
btnExit.place(x = 5, y = 325)

mainloop()
