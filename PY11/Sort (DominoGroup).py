#author: Alan
#date: Jan 8
#purpose: domino group with sort and search
#====================

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
    #date: Jan 17
    #purpose: compareTo for dominos (>)
    #parameter: other
    #return tempS>tempO
    def __gt__(self, other):
        tempS = 10*min(self.value%10, self.value//10)+\
                max(self.value%10, self.value//10)
        tempO = 10*min(self.value%10, self.value//10)+\
                max(self.value%10, self.value//10)
        return tempS>tempO

    #author: Alan
    #date: Jan 17
    #purpose: compareTo for dominos (<)
    #parameter: other
    #return tempS<tempO
    def __lt__(self, other):
        tempS = 10*min(self.value%10, self.value//10)+\
                max(self.value%10, self.value//10)
        tempO = 10*min(self.value%10, self.value//10)+\
                max(self.value%10, self.value//10)
        return tempS<tempO

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
#           isSorted: check if the dominoGroup is sorted
#           initAsRandom: intialize with random values
#           linearSearch: search for a value (bruteforce)
#           sentinelSearch: search for a value
#                           (bruteforce but with a sentinel)
#           binarySearch: search for a value (divide and conquer)
#           exchangeSort: sort by exchange
#           selectionSort: sort by search for lowest in [x:]
#           insertionSort: sort by assuming [:x] is already sorted
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
    #date: Jan 7
    #purpose: check if _list is sorted
    #parameter: N/A
    #return: blnReturn
    def isSorted(self):
        blnReturn = True
        for x in range(self.size-1):
            if self._list[x]>self._list[x+1]:
                blnReturn = False
        return blnReturn

    #author: Alan
    #date: Jan 7
    #purpose: initialize the group in a random orde 
    #parameter: size
    #return: N/A
    def initAsRandom(self, size):
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
    #date: Jan 7
    #purpose: linear search the array
    #parameter: value
    #return: intReturn
    def linearSearch(self, value):
        cont = True
        count = 0
        intReturn = -1
        while cont:
            if self._list[count] == value:
                intReturn = count
                cont = False
            count+=1
            if count==self.size:
                    cont = False
        return intReturn

    #author: Alan
    #date: Jan 7
    #purpose: sentinel search the array
    #parameter: value
    #return: intReturn
    def sentinelSearch(self, value):
        intReturn = -1
        self._list.append(value)
        count = 0
        cont = True
        while cont:
            if self._list[count] == value:
                if count!=self.size:
                    intReturn = count
                cont = False
            count+=1
        del self._list[self.size]
        return intReturn

    #author: Alan
    #date: Jan 7
    #purpose: binary search the array
    #parameter: value
    #return: intReturn
    def binarySearch(self, value):
        intReturn = -1
        if self.isSorted():
            first = 0
            last = len(self._list)-1
            found = False
            if self.sorted=="ascending":
                while first<=last and not found:
                    midpoint = (first + last)//2
                    if self._list[midpoint] == value:
                        found = True
                        intReturn = midpoint
                    else:
                        if value < self._list[midpoint]:
                            last = midpoint-1
                        else:
                            first = midpoint+1
            else:
                while first<=last and not found:
                    midpoint = (first+last)//2
                    if self_list[midpoint] == value:
                        found = True
                        intReturn = midpoint
                    else:
                        if value<self._list[midpoint]:
                            first = midpoint+1
                        else:
                            last = midpoint-1
        return intReturn

    #author: Alan
    #date: Jan 7
    #purpose: sort (exchange)
    #parameter: N/A
    #return: N/A
    def exchangeSort(self, sort="ascending"):
        if sort=="ascending" or sort = "descending":
            if sort=="ascending":
                for x in range(self.size-1):
                    for y in range(self.size-1):
                        if self._list[y]>self._list[y+1]:
                            self._list[y], self._list[y+1] = \
                                           self._list[y+1], self._list[y]
            else:
                for x in range(self.size-1, -1, -1):
                    for y in range(self.size-1, -1, -1):
                        if self._list[y]<self._list[y+1]:
                            self._list[y], self._list[y+1] = \
                                           self._list[y+1], self._list[y]
            self.sorted = sort

    #author: Alan
    #date: Jan 7
    #purpose: sort (selection)
    #parameter: N/A
    #return: N/A
    def selectionSort(self, sort="ascending"):
        if sort=="ascending" or sort = "descending":
            if sort=="ascending":
                for x in range(0, self.size):
                    minIndex = x
                    smallest = self._list[x]
                    for y in range(x, self.size):
                        if self._list[y]<smallest:
                            smallest = self._list[y]
                            minIndex = y
                    if minIndex!=x:
                        self._list[x], self._list[minIndex] = \
                                       self._list[minIndex], self._list[x]
            else:
                for x in range(self.size-1, -1, -1):
                    maxIndex = x
                    biggest = self._list[x]
                    for y in range(0, x):
                        if self._list[y]>biggest:
                            biggest = self._list[y]
                            maxIndex = y
                    if maxIndex!=x:
                        self._list[x], self._list[maxIndex] = \
                                       self._list[maxIndex], self._list[x]
            self.sorted = sort
                

    #author: Alan
    #date: Jan 7
    #purpose: sort (insertion)
    #parameter: N/A
    #return: N/A
    def insertionSort(self):
        if sort=="ascending" or sort = "descending":
            if sort=="ascending":
                for i in range(1, self.size): 
                    key = self._list[i]
                    j = i-1
                    while j>=0 and key < self._list[j]:
                        self._list[j+1] = self._list[j] 
                        j -= 1
                    self._list[j+1] = key
            else:
                for i in range(self.size-2, -1, -1):
                    hey = self._list[i]
                    j = i+1
                    while j<=self.size-1 and key > self._list[j]:
                        self._list[j-1] = self._list[j]
                        j+=1
                    self._list[j-1] = key

#author: Alan
#date: October 24
#purpose: type check
#parameter: strPrompt, strInput
#return: one integer
def typeCheck(strPrompt, strInput):
    while not strInput.isdigit():
        strInput = input(strPrompt)
    return int (strInput)

#author: Alan
#date: October 24
#purpose: Edit input for a integer between intLow and intHigh
#parameter: strPrompt, intLow, intHigh
#return: one positive integer
def getPositiveInteger(strPrompt="Please enter a number: ", \
                       intLow=0, intHigh=100):
    intInput = typeCheck(strPrompt, input(strPrompt))
    while intInput<intLow or intInput>intHigh:
        intInput = intInput = typeCheck(strPrompt, input(strPrompt))
    return intInput

#author: Alan
#date: Jan 14
#purpose: get a valid value for a domino
#parameter: strPrompt
#return: dominoInput
def getDomino(strPrompt):
    dominoInput = typeCheck(strPrompt, input(strPrompt))
    while not(dominoInput//10<=6 and dominoInput//10>=0 and\
          dominoInput%10<=6 and dominoInput%10>=0):
        dominoInput = typeCheck(strPrompt, input(strPrompt))
    return dominoInput

#main
cont = "yes"
while cont=="yes":
    dominoGroupA = dominoGroup()
    size = getPositiveInteger(strPrompt=\
                              "Please enter the size of the dominoGroupA: ",
                              intHigh=40)
    dominoGroupA.initAsRandom(size)
    print(dominoGroupA)

    search1 = input("Type of search (linear, sentinel, binary): ")
    while not(search1=="linear" or search1=="sentinel" or search1=="binary"):
        search1 = input("Type of search (linear, sentinel, binary): ")
    value1 = getDomino("the value to search for: ")

    if search1=="linear":
        print("It is at index: "+str(intGroupA.linearSearch(value1)))
    elif search1=="sentinel":
        print("It is at index: "+str(intGroupA.sentinelSearch(value1)))
    else:
        print("It is at index: "+str(intGroupA.binarySearch(value1)))

    sort = input("Type of sort (exchange, selection, insertion): ")
    if not(sort=="exchange" or sort=="selection" or sort=="insertion"):
        sort = input("Type of sort (exchange, selection, insertion): ")
    direction = input("Direction of sort (ascending or descending): ")
    while not (direction=="ascending" or direction=="descending"):
        direction = input("Direction of sort (ascending or descending): ")
    if sort=="exchange":
        intGroupA.exchangeSort()
    elif sort=="selection":
        intGroupA.selectionSort()
    else:
        intGroupA.insertionSort()

    print("the sorted intGroup: "+str(intGroupA))

       search2 = input("Type of search (linear, sentinel, binary): ")
    while not(search2=="linear" or search2=="sentinel" or search2=="binary"):
        search2 = input("Type of search (linear, sentinel, binary): ")
    value2 = getDomino("the value to search for: ")

    if search2=="linear":
        print("It is at index: "+str(intGroupA.linearSearch(value2)))
    elif search2=="sentinel":
        print("It is at index: "+str(intGroupA.sentinelSearch(value2)))
    else:
        print("It is at index: "+str(intGroupA.binarySearch(value2)))

    cont = input("Do you wish to continue (yes or no): ")
    while not(cont=="yes" or cont=="no"):
        cont = input("Yes or no: ")
