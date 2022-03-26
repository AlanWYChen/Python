#author: Alan
#date: November 22
#purpose: domino class with comparable
#=======================================================================

import random

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
#               __sub__: allow subtraction between dominos
#               __add__: allow addition between dominos
#               __mul__: allow multiplication between dominos
#               __gt__: allow > to work between dominos
#               __ge__: allow >= to work between dominos
#               __lt__: allow < to work between dominos
#               __le__: allow <= to work between dominos
#               __eq__: allow == to work between dominos 
#               __ne__: allow != to work between dominos
class Domino:
    #author: Alan
    #date: November 7
    #purpose: initialize the domino object
    #parameter: size
    #return: N/A
    def __init__(self, size=30):
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
        self.orientation = True #true is verital and false is horizonal
        self.face = True #true is up and false is down

    #author: Alan
    #date: November 7
    #purpose: make sure print function can print a domino variable
    #parameter: N/A
    #return: all the values of the object
    def __str__(self):
        return str(self.value)

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
            else:
                self.size = 30

    #author: Alan
    #date: November 7
    #purpose: set face via parameter
    #parameter: face
    #return: N/A
    def setFace(self, face):
        if face == False:
            self.face = False

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
    #date: November 22
    #purpose: allow subtraction between dates
    #parameter: self, other
    #return: intA-intB
    def __sub__(self, other):
        intA = 10*min(self.value//10, self.value%10)+\
                  max(self.value//10, self.value%10)
        intB = 10*min(other.value//10, other.value%10)+\
                  max(other.value//10, other.value%10)
        return intA - intB

    #author: Alan
    #date: November 22
    #purpose: allow addition between dates
    #parameter: self, other
    #return: intA + intB
    def __add__(self, other):
        intA = 10*min(self.value//10, self.value%10)+\
                  max(self.value//10, self.value%10)
        intB = 10*min(other.value//10, other.value%10)+\
                  max(other.value//10, other.value%10)
        return intA+intB

    #author: Alan
    #date: November 22
    #purpose: allow multipication between dates
    #parameter: self, other
    #return: intA*intB
    def __mul__(self, other):
        intA = 10*min(self.value//10, self.value%10)+\
                  max(self.value//10, self.value%10)
        intB = 10*min(other.value//10, other.value%10)+\
                  max(other.value//10, other.value%10)
        return intA*intB

    #author: Alan
    #date: November 22
    #purpose: allow > to work between dates
    #parameter: self, other
    #return: blnReturn
    def __gt__(self, other):
        blnReturn = False
        if self-other>0:
            blnReturn = True
        return blnReturn

    #author: Alan
    #date: November 22
    #purpose: allow >= to work between dates
    #parameter: self, other
    #return: blnReturn
    def __ge__(self, other):
        blnReturn = False
        if self-other>=0:
            blnReturn = True
        return blnReturn

    #author: Alan
    #date: November 22
    #purpose: allow < to work between dates
    #parameter: self, other
    #return: blnReturn
    def __lt__(self, other):
        blnReturn = False
        if self-other<0:
            blnReturn = True
        return blnReturn

    #author: Alan
    #date: November 22
    #purpose: allow <= to work between dates
    #parameter: self, other
    #return: blnReturn
    def __le__(self, other):
        blnReturn = False
        if self-other<=0:
            blnReturn = True
        return blnReturn

    #author: Alan
    #date: November 22
    #purpose: allow == to work between dates
    #parameter: self, other
    #return: blnReturn
    def __eq__(self, other):
        blnReturn = False
        if self-other==0:
            blnReturn = True
        return blnReturn

    #author: Alan
    #date: November 22
    #purpose: allow != to work between dates
    #parameter: self, other
    #return: blnReturn
    def __ne__(self, other):
        blnReturn = False
        if self-other!=0:
            blnReturn = True
        return blnReturn

#main
strReExecute = "yes"
while strReExecute=="yes":
    domino1 = Domino()
    domino2 = Domino()
    print ("First Domino is ", end="")
    print (domino1)
    print ("Second Domino is ", end="")
    print (domino2)
    domino1 = 10*min(domino1.value%10, domino1.value//10)+\
              max(domino1.value%10, domino1.value//10)
    domino2 = 10*min(domino2.value%10, domino2.value//10)+\
              max(domino2.value%10, domino2.value//10)
    print ("Sorted:")
    print ("First Domino is ", end="")
    print (domino1)
    print ("Second Domino is ", end="")
    print (domino2)
    print (domino1, end="")
    print (' + ', end="")
    print (domino2, end="")
    print (' = ', end="")
    print (domino1+domino2)
    print (domino1, end="")
    print (' - ', end="")
    print (domino2, end="")
    print (' = ', end="")
    print (domino1-domino2)
    print (domino1, end="")
    print (' x ', end="")
    print (domino2, end="")
    print (' = ', end="")
    print (domino1*domino2)
    if (domino1>domino2):
        print ("First Domino is greater than second")
    elif (domino1==domino2):
        print ("The two dominos are equal")
    else:
        print ("Second Domino is greater than first")
    strReExecute = input("Do you wish to continue? (yes or no) ")
    while not (strReExecute == "yes" or strReExecute == "no"):
        strReExecute = input("Please enter yes or no: ")
