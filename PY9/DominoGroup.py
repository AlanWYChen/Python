#author:
#date:
#purpose:
#====================

import random
from tkinter import *

interface = Tk()
interface.geometry("905x305+0+0")
interface.title("DominoGroup")

intSizeP = IntVar()
intSize = IntVar()
intRun = IntVar()

#size: length = 30-100, width = length*2
#author: Alan
#date: November 6
#purpose: Domino class
#data members:
#               value: value of the domino: 0-66 | both digit cannot be > 6
#               size: size of the domino (when printed on a canvas | 30-100
#               diameter: diameter of each dots on the domino
#               gap: gap between each dot on the domino
#               orientation: orientation of the domino; horizonal or vertial
#               face: face up or down of the triangle
#methods:
#               __init__: initialize the domino object
#               __str__: print the object throught print statement
#               getValue: change the value of the Domino (talking to user)
#               setValue: change the value of the Domino (no interaction
#                         with user)
#               flip: flip the value of the domino
#               setOrientation: set orientation (no interaction with the user)
#               setSize: set size (no interaction with the user)
#               setFace: set face (no interaction with the user)
#               randomize: randomize a value
#               drawPatternVertical: draw the dot pattern (Horizontal)
#               drawMatternHorizontal: draw the dot pattern (Vertical)
#               draw: draw the Domino on a Canvas
#               typeCheck: edit for an integer (talk to user)
#               getPositiveInteger: edit for a positive integer (talk to user)
class Domino:
    #author: Alan
    #date: November 7
    #purpose: initialize the domino object
    #parameter: size
    #return: N/A
    def __init__(self, size=30, orientation=True, face=True):
        size = str(size)
        if not size.isdigit():
            size=30
        else:
            size = int(size)
            if (size<30):
                size = 30
        self.value = 10*random.randint(0, 6)+random.randint(0, 6)
        self.size = size #30-100
        self.diameter = self.size//5
        self.gap = self.diameter//2
        self.orientation = orientation #true is verital and false is horizonal
        self.face = face #true is up and false is down

    #author: Alan
    #date: November 7
    #purpose: make sure print function can print a domino variable
    #parameter: N/A
    #return: all the values of the object
    def __str__(self):
        return str(str(self.value)+str(self.size)+str(self.orientation)+ \
               str(self.face))

    #author: Alan
    #date: November 7
    #purpose: get value from user (talking to user)
    #parameter: value
    #return: N/A
    def getValue(self):
        value = getPositiveIneger("Enter a value, 0-66 both digit <6: ", 0, 66)
        value1 = value//10
        value2 = value%10
        while value1>6 or value2>6:
            value = getPositiveIneger\
                    ("Enter a value, 0-66 both digit <6: ", 0, 66)
            value1 = value//10
            value2 = value%10
        self.value = value

    #author: Alan
    #date: November 7
    #purpose: set value via parameter
    #parameter: value
    #return: N/A
    def setValue(self, value):
        value=str(value)
        if not (value.isdigit()):
            value=0
        else:
            value=int(value)
            value1 = value//10
            value2 = value%10
            if (value1>6 or value2>6):
                value = 0
        self.value = value

    #author: Alan
    #date: November 7
    #purpose: flip the value AB -> BA
    #parameter: N/A
    #return: N/A
    def flip(self):
        value1 = self.value//10
        value2 = self.value%10
        value1, value2 = value2, value1
        self.value = value1*10+value2

    #author: Alan
    #date: November 7
    #purpose: set orientation via parameter
    #parameter: orientation
    #return: N/A
    def setOrientation(self, orientation):
        if orientation == False:
            self.orientation = False
        elif orientation == True:
            self.orientation = True

    #author: Alan
    #date: November 7
    #purpose: set size via parameter
    #parameter: size
    #return: N/A
    def setSize(self, size):
        size = str(size)
        if size.isdigit:
            size = int(size)
            if size>=30 and size<=100:
                self.size = size
                self.diameter = size//5
                self.gap = self.diameter//2
            else:
                self.size = 30
                self.diameter = size//5
                self.gap = self.diameter//2

    #author: Alan
    #date: November 7
    #purpose: set face via parameter
    #parameter: face
    #return: N/A
    def setFace(self, face):
        if face == False:
            self.face = False
        elif face == True:
            self.face = True

    #author: Alan
    #date: November 7
    #purpose: set self to random values 
    #parameter: N/A
    #return: N/A
    def randomize(self):
        self.value = 10*randint(0, 6)+randint(0, 6)
        self.size = randint(30, 100)
        orientation = randint(0, 1)
        face = randint(0, 1)
        if orientation == 0:
            self.orientation = False
        else:
            self.orientation = True
        if face == 0:
            self.face = False
        else:
            self.face = True

    #author: Alan
    #date: November 9
    #purpose: draw the dot pattern
    #parameter: canvas, x, y, dot
    #return: N/A
    def drawPatternVertical(self, canvas, x, y, dot):
        if dot%2==1:
            canvas.create_oval(x+self.gap*2+self.diameter, \
                                       y+self.gap*2+self.diameter, \
                                       x+self.gap*2+self.diameter*2, \
                                       y+self.gap*2+self.diameter*2,\
                                       fill="black")
        if dot!=0 and dot!=1:
            canvas.create_oval(x+self.gap, \
                                       y+self.gap, \
                                       x+self.gap+self.diameter, \
                                       y+self.gap+self.diameter, \
                                       fill="black")
            canvas.create_oval(x+self.gap*3+self.diameter*2, \
                                       y+self.gap*3+self.diameter*2, \
                                       x+self.gap*3+self.diameter*3, \
                                       y+self.gap*3+self.diameter*3, \
                                       fill="black")
        if dot>=4:
            canvas.create_oval(x+self.gap*3+self.diameter*2, \
                                       y+self.gap, \
                                       x+self.gap*3+self.diameter*3, \
                                       y+self.gap+self.diameter, \
                                       fill="black")
            canvas.create_oval(x+self.gap, \
                                       y+self.gap*3+self.diameter*2, \
                                       x+self.gap+self.diameter, \
                                       y+self.gap*3+self.diameter*3, \
                                       fill="black")
        if dot==6:
            canvas.create_oval(x+self.gap, \
                                       y+self.gap*2+self.diameter, \
                                       x+self.gap+self.diameter, \
                                       y+self.gap*2+self.diameter*2, \
                                       fill="black")
            canvas.create_oval(x+self.gap*3+self.diameter*2, \
                                       y+self.gap*2+self.diameter, \
                                       x+self.gap*3+self.diameter*3, \
                                       y+self.gap*2+self.diameter*2, \
                                       fill="black")

    #author: Alan
    #date: November 9
    #purpose: draw the dot pattern
    #parameter: canvas, x, y, dot
    #return: N/A
    def drawPatternHorizontal(self, canvas, x, y, dot):
        if dot%2==1:
            canvas.create_oval(x+self.gap*2+self.diameter, \
                               y+self.gap*2+self.diameter, \
                               x+self.gap*2+self.diameter*2, \
                               y+self.gap*2+self.diameter*2, \
                               fill="black")
        if dot!=0 and dot!=1:
            canvas.create_oval(x+self.gap*3+self.diameter*2, \
                               y+self.gap, \
                               x+self.gap*3+self.diameter*3, \
                               y+self.gap+self.diameter, \
                               fill="black")
            canvas.create_oval(x+self.gap, \
                               y+self.gap*3+self.diameter*2, \
                               x+self.gap+self.diameter, \
                               y+self.gap*3+self.diameter*3, \
                               fill="black")
        if dot>=4:
            canvas.create_oval(x+self.gap, \
                               y+self.gap, \
                               x+self.gap+self.diameter, \
                               y+self.gap+self.diameter, \
                               fill="black")
            canvas.create_oval(x+self.gap*3+self.diameter*2, \
                               y+self.gap*3+self.diameter*2, \
                               x+self.gap*3+self.diameter*3, \
                               y+self.gap*3+self.diameter*3, \
                               fill="black")
        if dot==6:
            canvas.create_oval(x+self.gap*2+self.diameter, \
                               y+self.gap, \
                               x+self.gap*2+self.diameter*2, \
                               y+self.gap+self.diameter, \
                               fill="black")
            canvas.create_oval(x+self.gap*2+self.diameter, \
                               y+self.gap*3+self.diameter*2, \
                               x+self.gap*2+self.diameter*2, \
                               y+self.gap*3+self.diameter*3, \
                               fill="black")

    
    
    #author: Alan
    #date: November 7
    #purpose: draw the domino to a canvas
    #parameter: canvas, x, y (coordinates)
    #return: N/A
    def draw(self, canvas, x, y):
        if self.face==True:
            if self.orientation == True:
                canvas.create_rectangle(x, y, x+self.size, y+self.size, \
                                         outline = "black", fill="white")
                canvas.create_rectangle(x, y+self.size, x+self.size, \
                                         y+2*self.size, outline = "black", \
                                         fill="white")
                
                self.drawPatternVertical(canvas, x, y, self.value//10)
                
                self.drawPatternVertical(canvas, x, y+self.size, self.value%10)
            else:
                canvas.create_rectangle(x, y, x+self.size, y+self.size, \
                                         outline = "black", fill="white")
                canvas.create_rectangle(x+self.size, y, x+2*self.size, \
                                         y+self.size, outline = "black", \
                                         fill="white")

                self.drawPatternHorizontal(canvas, x, y, self.value//10)

                self.drawPatternHorizontal(canvas, x+self.size, \
                                           y, self.value%10)
        else:
            if self.orientation==True:
                canvas.create_rectangle(x, y, x+self.size, y+self.size, \
                                        outline = "white", fill="black")
                canvas.create_rectangle(x, y+self.size, x+self.size, \
                                        y+2*self.size, outline = "white", \
                                        fill="black")
            else:
                canvas.create_rectangle(x, y, x+self.size, y+self.size, \
                                        outline = "white", fill="black")
                canvas.create_rectangle(x+self.size, y, x+self.size*2, \
                                        y+self.size, outline = "white", \
                                        fill="black")
    
    #author: Alan
    #date: October 24
    #purpose: type check
    #parameter: strPrompt, strInput
    #return: one integer
    def typeCheck(self, strPrompt, strInput):
        while not strInput.isdigit():
            strInput = input(strPrompt)
        return int (strInput)

    #author: Alan
    #date: October 24
    #purpose: Edit input for a integer between intLow and intHigh
    #parameter: strPrompt, intLow, intHigh
    #return: one positive integer
    def getPositiveInteger(self, strPrompt="Please enter a number: ", \
                           intLow=0, intHigh=100):
        intInput = self.typeCheck(strPrompt, input(strPrompt))
        while intInput<intLow or intInput>intHigh:
            intInput = intInput = self.typeCheck(strPrompt, input(strPrompt))
        return intInput

#author: Alan
#date: Dec 10
#purpose: DominoGroup class
#data members:
#           size: size of the _list
#           _list: the domino list (1D-array of dominos)
#methods:
#           __init__: initialize an instance of DominoGroup
#           __str__: override str() function
#           findFirst: find the first appearance of the given value 
#           initDeal: intialize an instnace of DominoGroup but no repeats
#           calcTotal: calculate the Total Value of the dominos (sum)
#           findLargest: find the largest domino in the group
#           calcFreq: return the frequency of given value
#           insertAt: insert value at position
#           removeAt: remove the element at position
#           removeAll: remove all appearances of value
#           drawList: draw the list on a canvas
#           setSize: set the size of all dominos
class DominoGroup:
    #author: Alan
    #date: Dec 10
    #purpose: intialize
    #parameter: size
    #return: N/A
    def __init__(self, size=0):
        size = str(size)
        if size.isdigit():
            size = int(size)
            if size<0 or size>7:
                self.size = 0
            else:
                self.size = size
        else:
            self.size = 0

        self._list = [Domino() for i in range(self.size)]

    #author: Alan
    #date: Dec 10
    #purpose: over ride Str() function
    #parameter: N/A
    #return: strReturn
    def __str__(self):
        strReturn = "["
        for i in range(0, self.size):
            strReturn += str(self._list[i].value//10)+"|"+\
                         str(self._list[i].value%10)
            if i<self.size-1:
                strReturn += ", "
        strReturn += "] size: "+str(self.size)
        return strReturn

    #author: Alan
    #date: Dec 10
    #purpose: find the first appearance of the given value
    #parameter: value
    #return: intReturn
    def findFirst(self, value):
        value = 10*min(value//10, value%10)+max(value//10, value%10)
        intReturn = -1
        for i in range(len(self._list)-1, 0, -1):
            V = self._list[i].value
            V = 10*min(V//10, V%10)+max(V//10, V%10)
            if V == value:
                intReturn = i
        return intReturn

    #author: Alan
    #date: Dec 10
    #purpose: intialize the DominoGroup
    #parameter: size
    #return: N/A
    def initDeal(self, size=0):
        size = str(size)
        if size.isdigit():
            size = int(size)
            if size<0 or size>7:
                self.size = 0
            else:
                self.size = size
        else:
            self.size = 0
        self._list = []
        for i in range(self.size):
            self._list.append(Domino())
            while self.calcFreq(self._list[i].value)>1:
                self._list[i] = Domino()

    #author: Alan
    #date: Dec 10
    #purpose: return the sum of all the value in the _list
    #parameter: N/A
    #return: intReturn
    def calcTotal(self):
        intReturn = 0
        for i in range(self.size):
            intReturn += self._list[i].value
        return intReturn

    #author: Alan
    #date: Dec 10
    #purpose: return the value of the largest element in the _list
    #parameter: N/A
    #return: dmoReturn
    def findLargest(self):
        dmoReturn = Domino()
        dmoReturn.setValue(00)
        for i in range(self.size):
            if self._list[i].value>dmoReturn.value:
                dmoReturn.setValue(self._list[i].value)
        return dmoReturn

    #author: Alan
    #date: Dec 10
    #purpose: return the number of appearance of value
    #parameter: value
    #return: intCOunt 
    def calcFreq(self, value):
        intCount = 0
        value = 10*min(value//10, value%10)+max(value//10, value%10)
        for i in range(self.size):
            V = self._list[i].value
            V = 10*min(V//10, V%10)+max(V//10, V%10)
            if V == value:
                intCount += 1
        return intCount

    #author: Alan
    #date: Dec 10
    #purpose: insert value at position
    #parameter: position, value
    #return: N/A
    def insertAt(self, position, value):
        position = str(position)
        if position.isDigit():
            position = int(position)-1
            if position>self.size-1:
                self._list.append(value)
            else:
                self._list.insert(position, value)

    #author: Alan
    #date: Dec 10
    #purpose: remove the element at position
    #parameter: position
    #return: N/A
    def removeAt(self, position):
        position = str(position)
        if position.isDigit():
            position = int(position)-1
            del self._list[position]
        self.size = len(self._list)

    #author: Alan
    #date: Dec 10
    #purpose: remove all instances of the value
    #parameter: value
    #return: N/A
    def removeAll(self, value):        
        value = str(value)
        if value.isDigit():
            value = int(value)
            value = 10*min(value//10, value%10)+max(value//10, value%10)
            for x in range(self.size):
                V = self._list[x].value
                V = 10*min(V//10, V%10)+max(V//10, V%10)
                if V==value:
                    del self.list[x]
                    x -= 1
        self.size = len(self._list)

    #author: Alan
    #date: Dec 10
    #purpose:  draw the list on a canvas
    #parameter: canvas, x, y
    #return: N/A
    def drawList(self, canvas, x, y):
        for i in range(self.size):
            self._list[i].draw(canvas, x+100*(i), y)

    #author: Alan
    #date: Dec 10
    #purpose: set the size of all domino in the _list
    #parameter: size
    #return: N/A
    def setSize(self, size): 
        size = str(size)
        if size.isdigit():
            size = int(size)
        if size<30 or size>100:
            size = 30
        for i in range(self.size):
            self._list[i].setSize(size)

#author: Alan
#date: December 11
#purpose: draw group
#parameter: canvas, group, x, y
#return: N/A
def drawGroup(canvas, group, x, y):
    canvas.delete("all")
    group.setSize(intSizeP.get())
    group.drawList(canvas, x, y)

#author: Alan
#date: December 11
#purpose: create a new group
#parameter: group
#return: N/A
def createNewGroup(group):
    group.size = intSize.get()
    group._list = []
    for i in range(intSize.get()):
        group._list.append(Domino())

#author: Alan
#date: December 11
#purpose: about
#parameter: N/A
#return: N/A
def about():
    messagebox.showinfo("About","This program creates an array of Dominos,"\
                        +"and displays the array on a canvas")

#main
Group = DominoGroup(intSize.get())

menubar = Menu(interface)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_separator()
filemenu.add_command(label="New Group", \
                     command=lambda: createNewGroup(Group))
filemenu.add_command(label="Exit",command=lambda:interface.destroy())
menubar.add_cascade(label="File", menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=lambda: about())
menubar.add_cascade(label="Help", menu=helpmenu)

interface.config(menu=menubar)

cvsDraw = Canvas(interface, height=200, width=900, bg="grey")
cvsDraw.place(x=0, y=0)

sclSizeP = Scale(interface, from_= 30, to = 80, orient=HORIZONTAL, \
                variable = intSizeP, label="Size (of Dominos)", width=20, length=150)
sclSizeP.place(x=50, y=210)

sclSize = Scale(interface, from_= 0, to = 7, orient=HORIZONTAL, \
                variable = intSize, label="Size of Group", width=20, length=150)
sclSize.place(x=550, y=210)

btnDisplay = Button(interface, width=15, height=0, text="Display", \
                    command=lambda: drawGroup(cvsDraw, Group, 5, 5))
btnDisplay.place(x=300, y=245)

mainloop()
