#author: Alan
#date: Dec 5
#purpose: intGroup
#============================================================

import random

#author: Alan
#date: Jan 8
#purpose: intGroup class (integer array)
#data memeber:
#               _list: the list
#               size: stores the size of the list _list
#               sorted: if the _list is sorted, if no, then no, if yes
#                       then ascending or descending
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
#               initAsRandom: intialize with random values
#               linearSearch: search for a value (bruteforce)
#               sentinelSearch: search for a value
#                               (bruteforce but with a sentinel)
#               binarySearch: search for a value (divide and conquer)
#               exchangeSort: sort by exchange
#               selectionSort: sort by search for lowest in [x:]
#               insertionSort: sort by assuming [:x] is already sorted
class intGroup: #iGp
    #author: ALan
    #date: December 6
    #purpose: initialize an instance of intGroup
    #parameter: size
    #return: N/A
    def __init__(self, size=0):
        self.sorted = "no"
        size = str(size)
        if size.isdigit():
            size = int(size)
        else:
            self.size = 0

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
        for x in range(len(self._list)):
            strReturn += str(self._list[x])
            if x<len(self._list)-1:
                strReturn += ","
        strReturn += "] len: "+str(self.size)
        return strReturn

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
    #date: Jan 7
    #purpose: initialize the intGroup with random ints
    #parameter: size
    #return: N/A
    def initAsRandom(self, size):
        self.sorted = "no"
        size = str(size)
        if size.isdigit():
            size = int(size)
        else:
            self.size = 0
        
        self.size = size
        self._list = []
        for x in range(self.size):
            self._list.append(random.randint(0, self.size))

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
        if sort=="ascending" or sort == "descending":
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
        if sort=="ascending" or sort == "descending":
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
        if sort=="ascending" or sort == "descending":
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

#main
cont = "yes"
while cont=="yes":
    intGroupA = intGroup()
    size = getPositiveInteger(strPrompt=\
                              "Please enter the size of the intGroup: ",
                              intHigh=40)
    intGroupA.initAsRandom(size)
    print(intGroupA)

    search1 = input("Type of search (linear, sentinel, binary): ")
    while not(search1=="linear" or search1=="sentinel" or search1=="binary"):
        search1 = input("Type of search (linear, sentinel, binary): ")
    value1 = getPositiveInteger(strPrompt="the value to search for: ")
    
    if search1=="linear":
        print("It is at index: "+str(intGroupA.linearSearch(value1)))
    elif search1=="sentinel":
        print("It is at index: "+str(intGroupA.sentinelSearch(value1)))
    else:
        print("It is at index: "+str(intGroupA.binarySearch(value1)))

    sort = input("Type of sort (exchange, selection, insertion): ")
    while not(sort=="exchange" or sort=="selection" or sort=="insertion"):
        sort = input("Type of sort (exchange, selection, insertion): ")
    direction = input("Direction of sort (ascending or descending): ")
    while not (direction=="ascending" or direction=="descending"):
        direction = input("Direction of sort (ascending or descending): ")
    if sort=="exchange":
        intGroupA.exchangeSort(direction)
    elif sort=="selection":
        intGroupA.selectionSort(direction)
    else:
        intGroupA.insertionSort(direction)

    print("the sorted intGroup: "+str(intGroupA))

    search2 = input("Type of search (linear, sentinel, binary): ")
    while not(search2=="linear" or search2=="sentinel" or search2=="binary"):
        search2 = input("Type of search (linear, sentinel, binary): ")
    value2 = getPositiveInteger(strPrompt="the value to search for: ")

    if search2=="linear":
        print("It is at index: "+str(intGroupA.linearSearch(value2)))
    elif search2=="sentinel":
        print("It is at index: "+str(intGroupA.sentinelSearch(value2)))
    else:
        print("It is at index: "+str(intGroupA.binarySearch(value2)))

    cont = input("Do you wish to continue (yes or no): ")
    while not(cont=="yes" or cont=="no"):
        cont = input("Yes or no: ")
