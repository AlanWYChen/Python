#author: Alan
#date: Dec 5
#purpose: intGroup
#============================================================

import random

#author:
#date:
#purpose:
#data memeber:
#               _list: the list
#               size: stores the size of the list _list
#methods:
#               __init__: initialize an instance of intGroup object
#               __str__: convert an intGroup object into a string
#               intitAsNum: initialize the whole list as num
#               initAsSeq: initialize as a arithemetic sequence
#               calcTotal: return the sum of all elements
#               calcMean: return the mean of all elements
#               findLargest: find the largest element
#               calcFreq: return the frequency of an element
#               insertAt: append a value at given position
#               removeAt: remove a value at a given position
#               removeAll: remove all instances of the value
#               findFirst: find the first instance of a value
#               isSorted: check if the elements are in accending order
#               merge: given a second intGroup, merge the two objects into a
#                      third if both originals are already sorted
class intGroup: #iGp
    #author: ALan
    #date: December 6
    #purpose: initialize an instance of intGroup
    #parameter: size
    #return: N/A
    def __init__(self, size=0):
        size = str(size)
        if size.isdigit():
            size = int(size)
        else:
            self.size = 0

        if size>20:
            size = 0
        self.size = size
        self._list = []
        for x in range(self.size):
            self._list.append(random.randint(0, self.size))
            
    #author: ALan
    #date: December 6
    #purpose: convert an intGroup to a string
    #parameter: N/A
    #return: N/A
    def __str__(self):
        strReturn = "["
        for x in range(self.size):
            strReturn += str(self._list[x])
            if x!=self.size-1:
                strReturn += " ,"
        strReturn += "] size: "+str(self.size)
        return (strReturn)

    #author: ALan
    #date: December 6
    #purpose: initialize the intGroup with random numbers up to lim
    #parameter: lim, size
    #return: N/A
    def initAsNum(self, num=0, size=0):
        num = str(num)
        size = str(size)
        if num.isdigit():
            num = int(num)
        else:
            num = 0
        if size.isdigit():
            self.size = int(size)
        else:
            self.size = 0

        if size>20:
            self.size = 0
        self._list = [num for x in range(self.size)]

    #author: ALan
    #date: December 6
    #purpose: initialize the intGroup as squence (1, 2, 3, 4, 5, 6...)
    #parameter: size
    #return: N/A           
    def initAsSeq(self, size):
        size = str(size)
        if size.isdigit():
            self.size = int(size)
        else:
            self.size = 0
        if self.size>20:
            self.size = 0

        self._list = []
        for x in range(self.size):
            self._list.append(x)

    #author: ALan
    #date: December 6
    #purpose: return total of all element
    #parameter: N/A
    #return: intReturn
    def calcTotal(self):
        intReturn = 0
        for x in range(self.size):
            intReturn += self._list[x]

        return intReturn

    #author: ALan
    #date: December 6
    #purpose: return the mean of all elements
    #parameter: N/A
    #return: self.calcTotal()/self.size
    def calcMean(self):
        return self.calcTotal()/self.size

    #author: ALan
    #date: December 6
    #purpose: return the largest element
    #parameter: N/A
    #return: intLargest
    def findLargest(self):
        intLargest = float('-inf')
        for x in range(self.size):
            if self._list[x]>intLargest:
                intLargest = self._list[x]

        return intLargest

    #author: ALan
    #date: December 6
    #purpose: count the frequency of appearance of a value
    #parameter:
    #return:
    def calcFreq(self, element):
        intCount = 0
        for x in range(self.size):
            if self._list[x]==element:
                intCount += 1
        return intCount

    #author: ALan
    #date: December 6
    #purpose: append value at position 
    #parameter: position, value
    #return: N/A
    def insertAt(self, position, value):
        position = str(position)
        if position.isDigit():
            position = int(position)-1            
            if position>=self.size:
                self._list.append(value)
            else:
                self._list.insert(position, value)
            self.size += 1

    #author: ALan
    #date: December 6
    #purpose: remove the element at position
    #parameter: position
    #return: N/A
    def removeAt(self, position):
        position = str(position)
        if position.isDigit():
            position = int(position)-1
            del self._list[position]
            self.size -= 1

    #author: ALan
    #date: December 6
    #purpose: remove all elements of the value
    #parameter: value
    #return: N/A
    def removeAll(self, value):
        value = str(value)
        if value.isDigit():
            value = int(value)
            for x in range(self.size):
                if self._list[x] == value:
                    del self.list[x]
                    x -= 1
            self.size = len(self.__list__)

    #author: ALan
    #date: December 6
    #purpose: find the first appearance of value
    #parameter: value
    #return: intReturn
    def findFirst(self, value):
        intReturn = -1
        for x in range(self.size):
            if self._list[x] == value:
                if intReturn == -1:
                    intReturn = x
        return intReturn

    #author: ALan
    #date: December 6
    #purpose: check if the _list is in accending order
    #parameter: N/A
    #return: blnReturn
    def isSorted(self):
        blnReturn = True
        for x in range(1, self.size):
            if self._list[x]<self._list[x-1]:
                blnReturn = False
        return blnReturn

    #author: ALan
    #date: December 6
    #purpose: if two intGroup are sorted, merge them into a new intGroup
    #parameter: other
    #return: intGroupReturn
    def merge(self, other):
        intGroupReturn =intGroup(size=0)
        if self.isSorted() and other.isSorted():
            intGroupReturn.size = self.size+other.size
            intA = 0
            intB = 0
            for i in range(self.size+other.size):
                if intA<self.size and intB<other.size:
                    if self._list[intA]<self._list[intB]:
                        intGroupReturn.append(self._list[intA])
                        intA+=1
                    else:
                        intGroupReturn.append(other._list[intB])
                        intB+=1
                if intA==self.size:
                    for x in range(intB, other.size):
                        intGroupReturn.append(other._list[x])
                elif intB==other.size:
                    for x in range(intA, self.size):
                        intGroupReturn.append(self._list[x])                                   
        return intGroupReturn

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

#main
size1 = getPositiveInteger(strPrompt="Please enter the first size: ")
iGpA = intGroup(size1)
size2 = getPositiveInteger(strPrompt="Please enter the second size: ")
iGpB = intGroup(size2)

print ("The first list: "+str(iGpA))
print ("First list total: "+str(iGpA.calcTotal()))
print ("The second list: "+str(iGpB))
print ("Second list total: "+str(iGpB.calcTotal()))

insert = input("Do you wish to insert an element into the group? ")
while not (insert=="yes" or insert=="no"):
    insert = input("yes or no ")
if insert=="yes":
    group = getPositiveInteger(strPrompt="Which group? 1 or 2 ",\
                               intLow=1, intHigh = 2)
    index = getPositiveInteger(strPrompt="Please Enter an index")
    value = getPositiveInteger(strPrompt="Please Enter a value")
    if group == 1:
        iGpA.insertAt(index, value)
    else:
        iGpB.insertAt(index, value)

remove = input("Do you wish to remove an element from the group? ")
while not (insert=="yes" or insert=="no"):
    remove = input("yes or no ")
if remove=="yes":
    group = getPositiveInteger(strPrompt="Which group? 1 or 2 ",\
                               intLow=1, intHigh = 2)
    index = getPositiveInteger(strPrompt="Please Enter an index")
    if group==1:
        iGpA.removeAt(index)
    else:
        iGpB.removeAt(index)
    
removeValue = input("Do you wish to remove a value from the group? ")
while not (insert=="yes" or insert=="no"):
    removeValue = input("yes or no ")
if removeValue=="yes":
    group = getPositiveInteger(strPrompt="Which group? 1 or 2 ",\
                               intLow=1, intHigh = 2)
    value = getPositiveInteger(strPrompt="Please Enter a value")
    if group==1:
        iGpA.removeAll(value)
    else:
        iGpB.removeAll(value)

print("the mean value of the first list "+str(iGpA.calcMean()))
print("the mean value of the second list "+str(iGpB.calcMean()))

frequency = input("Do you wish to find the frequency of a value from the group? ")
while not (insert=="yes" or insert=="no"):
    frequency = input("yes or no ")
if frequency=="yes":
    group = getPositiveInteger(strPrompt="Which group? 1 or 2 ",\
                               intLow=1, intHigh = 2)
    value = getPositiveInteger(strPrompt="Please Enter a value")
    if group==1:
        print("the frequency of the value is "+str(iGpA.calcFreq(value)))
    else:
        print("the frequency of the value is "+str(iGpB.calcFreq(value)))

print("the largest element in the first list is "+str(iGpA.findLargest()))

print("the largest element in the second list is "+str(iGpB.findLargest()))

if iGpA.isSorted():
    print("The first list is sorted")
else:
    print("The first list is not sorted")

if iGpB.isSorted():
    print("The second list is sorted")
else:
    print("The second list is not sorted")

if iGpA.isSorted() and iGpB.isSorted():
    print (str(iGpA.merge(iGpB)))
