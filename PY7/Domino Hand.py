#author: Alan
#date: November 13
#purpose: Domino Hand Class
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#author: Alan
#date: November 5
#purpose: Domino class
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import random
from tkinter import *
import sys

interface = Tk()
interface.geometry("905x305+0+0")
interface.title("Hand")

intSize = IntVar()
intRun = IntVar()
strRun = StringVar()

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
        self.size = size                #30-100
        self.diameter = self.size//5
        self.gap = self.diameter//2
        self.orientation = orientation  #true is verital and false is horizonal
        self.face = face                #true is up and false is down

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
#date: November 20
#purpose: a hand of dominos
#data members:
#               domino1
#               domino2
#               domino3
#methods:
#               __init__: initialize the hand object
#               __str__: allows print function to print a hand object
#               setSize: set the size of the hand (through parameters)
#               sort: sort the 3 dominos in hand from least to greatest
#               roll: randomize the values of the 3 dominos
#               draw: draw the 3  dominos onto a canvas
#               getRun: return the max number of runs of the hand
#               drawRun: draw the domino displaying the max run
class Hand:
    #author: Alan
    #date: November 20
    #purpose: initialze the hand object
    #parameter: size
    #return: N/A
    def __init__(self, size=30):
        size = str(size)
        if size.isdigit():
            size = int(size)
        else:
            size = 30
        self.domino1 = Domino(size = size, orientation=False)
        self.domino2 = Domino(size = size, orientation=False)
        self.domino3 = Domino(size = size, orientation=False)

    #author: Alan
    #date: November 20
    #purpose: let print function print a hand
    #parameter: N/A
    #return: a string of the values of the 3 dominos
    def __str__(self):
        return str(self.domino1.value)+" - "+str(self.domino2.value)+" - "+\
               str(self.domino3.value)

    #author: Alan
    #date: November 20
    #purpose: set the size of hand (display)
    #parameter: size
    #return: N/A
    def setSize(self, size):
        size = str(size)
        if size.isdigit():
            size = int(size)
            if size>=30 and size<=100:
                self.domino1.setSize(size)
                self.domino2.setSize(size)
                self.domino3.setSize(size)

    #author: Alan
    #date: November 20
    #purpose: sort the 3 dominos
    #parameter: N/A
    #return: N/A
    def sort(self):
        a = self.domino1.value
        b = self.domino2.value
        c = self.domino3.value

        if a>b:
            a, b = b, a
        if b>c:
            b, c = c, b
        if a>b:
            a, b = b, a

        self.domino1.value = a
        self.domino2.value = b 
        self.domino3.value = c

    #author: Alan
    #date: November 20
    #purpose: set a new value to the 3 domino (random)
    #parameter: N/A
    #return: N/A
    def roll(self):
        self.domino1.value = 10*random.randint(6)+random.randint(6)
        self.domino2.value = 10*random.randint(6)+random.randint(6)
        self.domino3.value = 10*random.randint(6)+random.randint(6)

    #author: Alan
    #date: November 20
    #purpose: draw 3 dominos
    #parameter: canvas, x, y
    #return: N/A
    def draw(self, canvas, x, y):
        self.domino1.draw(canvas, x, y)
        self.domino2.draw(canvas, \
                          x+self.domino2.size*3, y)
        self.domino3.draw(canvas, \
                          x+self.domino3.size*6, y)

    #author: Alan
    #date: November 20
    #purpose: return max # of run
    #parameter: N/A
    #return: max run of the hand
    def getRun(self):
        d1 = Domino(size = 30, orientation=False)
        d2 = Domino(size = 30, orientation=False)
        d3 = Domino(size = 30, orientation=False)
        
        maxRun = 0

        for x in range(3):
            if x==0:
                d1.value = self.domino1.value
                d2.value = self.domino2.value
                d3.value = self.domino3.value
            if x==1:
                d1.value = self.domino1.value
                d2.value = self.domino3.value
                d3.value = self.domino2.value
            elif x==2:
                d1.value = self.domino2.value
                d2.value = self.domino1.value
                d3.value = self.domino3.value
            for y1 in range(2):
                for y2 in range(2):
                    for y3 in range(2):
                        if y1==1:
                            d1.value = 10*max(d1.value//10, d1.value%10)+\
                                       min(d1.value//10, d1.value%10)
                        else:
                            d1.value = 10*min(d1.value//10, d1.value%10)+\
                                       max(d1.value//10, d1.value%10)
                        if y2==1:
                            d2.value = 10*max(d2.value//10, d2.value%10)+\
                                       min(d2.value//10, d2.value%10)
                        else:
                            d2.value = 10*min(d2.value//10, d2.value%10)+\
                                       max(d2.value//10, d2.value%10)
                        if y3==1:
                            d3.value = 10*max(d3.value//10, d3.value%10)+\
                                       min(d3.value//10, d3.value%10)
                        else:
                            d3.value = 10*min(d3.value//10, d3.value%10)+\
                                       max(d3.value//10, d3.value%10)
                        
                        intRun = 0
                        
                        if d1.value%10==d2.value//10 \
                           and d2.value%10==d3.value//10:
                            intRun = 3
                        else:
                            if d1.value%10==d2.value//10 or\
                               d2.value%10==d3.value//10:
                                intRun = 2

                        #print ("temp run:")
                        #print(intRun)
                        
                        if intRun>maxRun:
                            maxRun = intRun
                            #print ("temp maxRun:")
                            #print (maxRun)
        #print (maxRun)
        return maxRun

    #author: Alan
    #date: November 20
    #purpose: draw a possible way to order the dominos to get the max run
    #parameter: canvas, _x, _y
    #return: N/A
    def drawRun(self, canvas, _x, _y):
        canvas.delete("all")
        d1 = Domino(size = 30, orientation=False)
        d2 = Domino(size = 30, orientation=False)
        d3 = Domino(size = 30, orientation=False)
        ansD1 = Domino(size = intSize.get(), orientation=False)
        ansD2 = Domino(size = intSize.get(), orientation=False)
        ansD3 = Domino(size = intSize.get(), orientation=False)
        maxRun = 0
        for x in range(3):
            if x==0:
                d1.value = self.domino1.value
                d2.value = self.domino2.value
                d3.value = self.domino3.value
            if x==1:
                d1.value = self.domino1.value
                d2.value = self.domino3.value
                d3.value = self.domino2.value
            elif x==2:
                d1.value = self.domino2.value
                d2.value = self.domino1.value
                d3.value = self.domino3.value
            for y1 in range(2):
                for y2 in range(2):
                    for y3 in range(2):
                        if y1==1:
                            d1.value = 10*max(d1.value//10, d1.value%10)+\
                                       min(d1.value//10, d1.value%10)
                        else:
                            d1.value = 10*min(d1.value//10, d1.value%10)+\
                                       max(d1.value//10, d1.value%10)
                        if y2==1:
                            d2.value = 10*max(d2.value//10, d2.value%10)+\
                                       min(d2.value//10, d2.value%10)
                        else:
                            d2.value = 10*min(d2.value//10, d2.value%10)+\
                                       max(d2.value//10, d2.value%10)
                        if y3==1:
                            d3.value = 10*max(d3.value//10, d3.value%10)+\
                                       min(d3.value//10, d3.value%10)
                        else:
                            d3.value = 10*min(d3.value//10, d3.value%10)+\
                                       max(d3.value//10, d3.value%10)
                        
                        intRun = 0
                        
                        if d1.value%10==d2.value//10 \
                           and d2.value%10==d3.value//10:
                            intRun = 3
                        else:
                            if d1.value%10==d2.value//10:
                                intRun = 2
                            if d2.value%10==d3.value//10:
                                intRun = 2
                        if intRun>maxRun:
                            maxRun = intRun
                            ansD1.value = d1.value
                            ansD2.value = d2.value
                            ansD3.value = d3.value
        #print(d1)
        #print(ansD1)
        #print(d2)
        #print(ansD2)
        #print(d3)
        #print(ansD3)
        ansD1.draw(canvas, _x, _y)
        ansD2.draw(canvas, _x+intSize.get()*3, _y)
        ansD3.draw(canvas, _x+intSize.get()*6, _y)

#author: Alan
#date: November 20
#purpose: draw hand
#parameter: canvas, hand, x, y
#return: N/A
def drawHand(canvas, hand, x, y):
    canvas.delete("all")
    hand.setSize(intSize.get())
    hand.draw(canvas, x, y)

#author: Alan
#date: November 20
#purpose: create a new hand
#parameter: N/A
#return: N/A
def createNewHand(hand):
    hand.domino1.value = 10*random.randint(0, 6)+random.randint(0, 6)
    hand.domino2.value = 10*random.randint(0, 6)+random.randint(0, 6)
    hand.domino3.value = 10*random.randint(0, 6)+random.randint(0, 6)
    intRun.set(int(hand.getRun()))
    strRun.set("Run: "+str(intRun.get()))
    drawHand(cvsDraw, hand, 5, 5)
    #print(intRun.get())

#author: Alan
#date: November 20
#purpose: about
#parameter: N/A
#return: N/A
def about():
    messagebox.showinfo("About","This program creates a hand of Domino "+\
                        "and displays it; can be sorted, and can be "+\
                        "displayed with it's run.")

#author: Alan
#date: November 27
#purpose: print (sort)
#parameter: canvas, hand, x, y
#return: N/A
def sort(canvas, hand, x, y):
    canvas.delete("all")
    temp = Hand()
    temp.domino1.setValue(hand.domino1.value)
    temp.domino2.setValue(hand.domino2.value)
    temp.domino3.setValue(hand.domino3.value)
    temp.setSize(intSize.get())
    temp.sort()
    temp.draw(canvas, x, y)

#author: Alan
#date: November 27
#purpose: simulate (10000 times)
#parameter: N/A
#return: N/A
def simulate():
    intZero = 0
    intTwo = 0
    intThree = 0
    for x in range(1000):
        hand = Hand(30)
        if hand.getRun()==0:
            intZero += 1
        elif hand.getRun()==2:
            intTwo += 1
        else:
            intThree += 1
    messagebox.showinfo("Result",\
                        "Run of zero: "+str(intZero/10)+"%\n"\
                        "Run of two: "+str(intTwo/10)+"%\n"
                        "Run of three: "+str(intThree/10)+"%")

#main
hand = Hand(size = intSize.get())

intRun.set(hand.getRun())
strRun.set("Run: "+str(intRun.get()))

menubar = Menu(interface)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_separator()
filemenu.add_command(label="New Hand", \
                     command=lambda: createNewHand(hand))
filemenu.add_command(label="Simulate (1000 times)", command=lambda: simulate())
filemenu.add_command(label="Exit",command=lambda:interface.destroy())
menubar.add_cascade(label="File", menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=lambda: about())
menubar.add_cascade(label="Help", menu=helpmenu)

interface.config(menu=menubar)

cvsDraw = Canvas(interface, height=200, width=900, bg="grey")
cvsDraw.place(x=0, y=0)

sclSize = Scale(interface, from_= 30, to = 100, orient=HORIZONTAL, \
                variable = intSize, label="size", width=20, length=150)
sclSize.place(x=50, y=210)

btnDisplay = Button(interface, width=15, height=0, text="Display", \
                    command=lambda: drawHand(cvsDraw, hand, 5, 5))
btnDisplay.place(x=300, y=245)

btnSort = Button(interface, width=15, height=0, text="Sort", \
                    command=lambda: sort(cvsDraw, hand, 5, 5))
btnSort.place(x=500, y=245)

btnDrawRun = Button(interface, width=15, height=0, text="Draw Run", \
                    command=lambda: hand.drawRun(cvsDraw, 5, 5))
btnDrawRun.place(x=700, y=245)

lblRun = Label (interface, width=20, height=2, bg="dark grey", \
                textvariable=strRun)
lblRun.place(x=355, y=165)

drawHand(cvsDraw, hand, 5,  5)

mainloop()
