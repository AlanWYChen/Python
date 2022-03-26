#author: Alan
#date: November 22
#purpose: Fraction class
#======================================================

import random
from tkinter import *

interface = Tk()
interface.geometry("460x250+0+0")

interface.title("Fraction game")

strFracA = StringVar()

strOperation = StringVar()

strFracB = StringVar()

strFracC = StringVar()

intScore = IntVar()
intScore.set(0)

intCount = IntVar()
intCount.set(0)

strScore = StringVar()

#author: Alan
#date: November 26
#purpose: Fraction class with overloading
#data members:
#           a
#           b
#           c
#           sign
#               a fraction is stored as a b/c with sign storing + and -
#methods:
#           __init__: initialize fraction object
#           calcGCD: return GCD of 2 numbers
 #           getImproperFrac: return the fraction as b/c
#           setValue: set the value of the fraction
#           randomize: set the value of the fraction to a random number
#           __str__: let print() be able to print a fraction
#           calcInverse: given b/c, return c/b
#           __sub__: allows - between fractions
#           __add__: allows + between fractions
#           __mul__: allows * between fractions
#           __truediv__: allows / between fractions
#           __eq__: allows == between fractions
class Fraction:
    #author: Alan
    #date: November 26
    #purpose: initialize the fraction object
    #parameter: a, b, c // a b/c
    #return: N/A
    def __init__(self, a=0, b=0, c=1): #a b/c
        a = str(a)
        b = str(b)
        c = str(c)

        sign = 1
        
        if a[0]=='-':
            sign+=1
            a = a[1:]
        if b[0]=='-':
            sign+=1
            b = b[1:]
        if c[0]=='-':
            sign+=1
            c = c[1:]
        if sign==1 or sign==3:
            self.sign = -1
        else:
            self.sign = 1

        if a.isdigit():
            a = int(a)
        else:
            a=0
        
        if b.isdigit():
            b = int(b)
        else:
            b=1

        if c.isdigit():
            c = int(c)
        else:
            c=0

        self.a = a
        self.b = b
        self.c = c
        self.reduce()

    #author: Alan
    #date: November 26
    #purpose: return the GCD of 2 numbers
    #parameter: x, y
    #return: gcd
    def calcGCD(self, x, y):
        gcd = 0
        if x > y: 
            small = y 
        else: 
            small = x 
        for i in range(1, small+1): 
            if((x % i == 0) and (y % i == 0)): 
                gcd = i                  
        return gcd

    #author: Alan
    #date: November 26
    #purpose: reduce the fraction to lowest terms and into mixed number form
    #parameter: N/A
    #return: N/A
    def reduce(self):
        if self.sign==1:
            sign = 0
            self.a = str(self.a)
            self.b = str(self.b)
            self.c = str(self.c)

            if self.a[0]=='-':
                sign+=1
                self.a = self.a[1:]
            if self.b[0]=='-':
                sign+=1
                self.b = self.b[1:]
            if self.c[0]=='-':
                sign+=1
                self.c = self.c[1:]
            if sign%2==1:
                self.sign = -1
            else:
                self.sign = 1

            self.a = int(self.a)
            self.b = int(self.b)
            self.c = int(self.c)
            
        if self.c==0:
            self.a = 0
            self.b = 0
            self.c = 1
        else:
            intCom = 0
            while (intCom!=1):
                intCom = 1
                for x in range(1, max(int(self.b), int(self.c))):
                    if self.b%x==0 and self.c%x==0:
                        intCom = x
                        self.b /= intCom
                        self.c /= intCom

        while (self.b>=self.c):
            self.b -= self.c
            self.a += 1

        self.a = int(self.a)
        self.b = int(self.b)
        self.c = int(self.c)

    #author: Alan
    #date: November 26
    #purpose: change the fraction to an improper fraction
    #parameter: N/A
    #return: N/A
    def getImproperFrac(self):
        self.b += self.a*self.c
        self.a = 0

    #author: Alan
    #date: November 26
    #purpose: set the value of a fraction object
    #parameter: a, b, c
    #return: N/A
    def setValue(self, a=0, b=0, c=1):
        a = str(a)
        b = str(b)
        c = str(c)

        sign = 1
        
        if a[0]=='-':
            sign+=1
            a = a[1:]
        if b[0]=='-':
            sign+=1
            b = b[1:]
        if c[0]=='-':
            sign+=1
            c = c[1:]
        
        if sign%2==1:
            self.sign = -1
        else:
            self.sign = 1

        if a.isdigit():
            a = int(a)
        else:
            a=0
        
        if b.isdigit():
            b = int(b)
        else:
            b=1

        if c.isdigit():
            c = int(c)
        else:
            c=0

        self.a = a
        self.b = b
        self.c = c
        self.reduce()
        print (self)

    #author: Alan
    #date: November 26
    #purpose: randomize the value of a fraction object
    #parameter: lim
    #return: N/A
    def randomize(self, lim=1):
        self.a = 0
        self.b = random.randint(0, lim)
        self.c = random.randint(1, lim)

        if random.randint(0, 1)==1:
            self.sign = 1
        else:
            self.sign = -1
        self.reduce()

    #author: Alan
    #date: November 26
    #purpose: allows print() to print fractions
    #parameter: N/A
    #return: N/A
    def __str__(self):
        self.reduce()
        strReturn = ""
        if self.a==0:
            if self.b==0:
                strReturn = "0"
            elif self.b!=0:
                strReturn = str(self.b*self.sign)+"/"+str(self.c)
        elif self.a!=0:
            if self.b==0:
                strReturn = str(self.a*self.sign)
            elif self.b!=0:
                strReturn = str(self.a*self.sign)+" "+str(self.b)+"/"+\
                            str(self.c)
        return strReturn

    #author: Alan
    #date: November 26
    #purpose: change the fraction to an inverse
    #parameter: N/A
    #return: N/A
    def calcInverse(self):
        self.getImproperFrac()
        self.b, self.c = self.c, self.b
        self.reduce()

    #author: Alan
    #date: November 29
    #purpose: change the fraction to a decimal
    #parameter: N/A
    #return: self.a+(self.b/self.c)
    def toDecimal(self):
        return self.a+(self.b/self.c)
    
    #author: Alan
    #date: November 26
    #purpose: allows - between fractions
    #parameter: other
    #return: fractionReturn
    def __sub__(self, other):
        self.getImproperFrac()

        other.getImproperFrac()
        
        diff = self.calcGCD(self.c, other.c)
        
        self.b *= diff
        self.c *= diff

        other.b *= diff
        other.c *= diff
        
        fractionReturn = Fraction(b = self.b*self.sign-other.b*other.sign, \
                                  c = self.c)
        fractionReturn.reduce()
        self.reduce()
        other.reduce()

        return fractionReturn

    #author: Alan
    #date: November 26
    #purpose: allows + between fractions
    #parameter: other
    #return: fractionReturn
    def __add__(self, other):
        self.getImproperFrac()

        other.getImproperFrac()
        
        diff = self.calcGCD(self.c, other.c)
        
        self.b *= diff
        self.c *= diff

        other.b *= diff
        other.c *= diff
        
        fractionReturn = Fraction(b = self.b*self.sign+other.b*other.sign, \
                                  c = self.c)
        fractionReturn.reduce()
        self.reduce()
        other.reduce()

        return fractionReturn

    #author: Alan
    #date: November 26
    #purpose: allows * between fractions
    #parameter: other
    #return: fractionReturn
    def __mul__(self, other):
        self.getImproperFrac()

        other.getImproperFrac()

        fractionReturn = Fraction(b = self.b*other.b*self.sign*other.sign, \
                                  c = self.c*other.c)
        fractionReturn.reduce()
        self.reduce()
        other.reduce()

        return fractionReturn

    #author: Alan
    #date: November 26
    #purpose: allows / between fractions
    #parameter: other
    #return: self*tempOther
    def __truediv__(self, other):
        self.getImproperFrac()

        tempOther = other
        tempOther.calcInverse()
        other.reduce()
        
        tempOther.getImproperFrac()
        
        return self*tempOther

    #author: Alan
    #date: November 26
    #purpose: allows == between fractions
    #parameter: other
    #return: blnReturn
    def __eq__(self, other):
        blnReturn = False
        if self.a==other.a and self.b==other.b and \
            self.c==other.c and self.sign == other.sign:
                blnReturn = True
        return blnReturn

fracA = Fraction(a=0, b=0, c=1)
fracB = Fraction(a=0, b=0, c=1)
fracC = Fraction(a=0, b=0, c=1)

#author: Alan
#date: November 26
#purpose: new fractions
#parameter: N/A
#return: N/A
def new():
    fracA.randomize(5)
    operation = random.randint(0, 4)
    if operation == 0:
        strOperation.set("+")
        fracC = fracA+fracB
    elif operation == 1:
        strOperation.set("-")
        fracC = fracA-fracB
    elif operation == 2:
        strOperation.set("x")
        fracC = fracA*fracB
    else:
        strOperation.set("/")
        fracC = fracA/fracB

    fracB.randomize(lim=5)

    fracC.randomize(lim=5)

    strFracA.set(fracA)
    strFracB.set(fracB)
    strFracC.set(fracC)
    strScore.set(str(intScore.get())+"/"+str(intCount.get()))

#author: Alan
#date: November 26
#purpose: check if it is true
#parameter: N/A
#return: N/A
def checkTrue():
    operation = strOperation.get()
    if operation=="+":
        if fracA+fracB==fracC:
            intScore.set(intScore.get()+1)
    elif operation=="-":
        if fracA-fracB==fracC:
            intScore.set(intScore.get()+1)
    elif operation=="x":
        if fracA*fracB==fracC:
            intScore.set(intScore.get()+1)
    else:
        if fracA/fracB==fracC:
            intScore.set(intScore.get()+1)
    intCount.set(intCount.get()+1)
    new()

#author: Alan
#date: November 26
#purpose: check if it is false
#parameter: N/A
#return: N/A
def checkFalse():
    operation = strOperation.get()
    if operation=="+":
        if fracA+fracB!=fracC:
            intScore.set(intScore.get()+1)
    elif operation=="-":
        if fracA-fracB!=fracC:
            intScore.set(intScore.get()+1)
    elif operation=="x":
        if fracA*fracB!=fracC:
            intScore.set(intScore.get()+1)
    else:
        if fracA/fracB!=fracC:
            intScore.set(intScore.get()+1)
    intCount.set(intCount.get()+1)
    new()

#main
menubar = Menu(interface)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_separator()
filemenu.add_command(label="Exit", \
                     command=lambda: interface.destroy())
menubar.add_cascade(label="File", menu=filemenu)
interface.config(menu=menubar)

new()
lblFirstFrac = Label (interface, width = 5, height = 0, \
                      textvariable=strFracA)
lblFirstFrac.place (x=50, y=50)

lblOperation = Label (interface, width = 5, height = 0, \
                      textvariable=strOperation)
lblOperation.place (x=125, y=50)

lblSecondFrac = Label (interface, width = 5, height = 0, \
                       textvariable=strFracB)
lblSecondFrac.place (x=200, y=50)

lblEqual = Label (interface, width = 5, height = 0, \
                  text='=')
lblEqual.place (x=275, y=50)

lblAns = Label (interface, width = 6, height = 0, \
                textvariable=strFracC)
lblAns.place (x=350, y=50)

lblScoreLabel = Label (interface, width = 15, height = 0, \
                text="Score")
lblScoreLabel.place (x=155, y=125)

lblScore = Label (interface, width = 15, height = 0, \
                textvariable=strScore)
lblScore.place (x=155, y=145)

btnYes = Button (interface, width = 10, height = 0, \
                 text="True", command= lambda: checkTrue())
btnYes.place (x=80, y=200)

btnNo = Button (interface, width = 10, height = 0, \
                text="False", command= lambda: checkFalse())
btnNo.place (x=250, y=200)

mainloop()
