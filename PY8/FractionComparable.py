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

        sign = 0
        
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
                intCom=1
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

        sign = 0
        
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

    #author: Alan
    #date: November 26
    #purpose: randomize the value of a fraction object
    #parameter: lim
    #return: N/A
    def randomize(self, lim=1):
        self.b = random.randint(0, lim)
        self.c = random.randint(0, lim)

        if random.randint(0, 1)==1:
            self.sign = 1
        else:
            self.sign = 0

    #author: Alan
    #date: November 26
    #purpose: allows print() to print fractions
    #parameter: N/A
    #return: N/A
    def __str__(self):
        strReturn = ""
        if self.a==0:
            if self.b!=0:
                strReturn = str(self.b*self.sign)+"/"+str(self.c)
            else:
                strReturn = "0"
        else:
            if self.b==0:
                strReturn = str(self.a*self.sign)
            else:
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

        tempOther = other.calcInverse()

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

fracA = Fraction(a = -1)
fracB = Fraction(b = 1, c=4)
print  (fracA*fracB)
