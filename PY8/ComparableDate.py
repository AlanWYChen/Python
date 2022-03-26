#author: Alan
#date: November 20
#purpose: date class and comparable
#============================================

#author: Alan
#date: November 1
#purpose: date container class with methods that return different information
#data members:
#               year: stores the year of the date
#               month: stores the month of the date
#               day: stores the day of the date
#methods:
#               __intit__: initialize
#               returnMonthName: return the month's name in words
#               leapYearCheck: return true if it is a leap year, else false
#               ReturnMaxDay: return the max number of days for that month
#               calcZeller: return the day of the week (0-6), 0 is sunday and 6
#                           is saturday
#               returnDayName: return the day of the week in word
#               calcValid: return true if the date is valid
#               getDate: edit for a valid date (during input)
#               __str__: return the date (ex. Monday, 24 October 2011)
#               dayOfyear: return the day of the year
#               displayCalendar: return the calendar for the month of that year
#               typeCheck: checks for type (int)
#               getPositiveInteger: edit for a positive integer
#               __sub__: allow subtraction between dates
#               __add__: allow addition between dates
#               __gt__: allow > to work between dates
#               __ge__: allow >= to work between dates
#               __lt__: allow < to work between dates
#               __le__: allow <= to work between dates
#               __eq__: allow == to work between dates 
#               __ne__: allow != to work between dates
class Date:
    def __init__ (self, year=2000, month=1, day=1):
        year = str(year)
        month = str(month)
        day = str(day)
        if year.isdigit() and month.isdigit() and day.isdigit():
            self.year = int(year)
            self.month = int(month)
            self.day = int(day)
        else:
            self.year = 2000
            self.month = 1
            self.day = 1
        if not self.calcValid():
            self.year = 2000
            self.month = 1
            self.day = 1

    #author: Alan
    #date: November 1
    #purpose: return the Month Name in words
    #parameter: self
    #return: the Month Name in words
    def returnMonthName(self):
        strReturn = ""
        if self.month == 1:
            strReturn = "January"
        elif self.month == 2:
            strReturn = "February"
        elif self.month == 3:
            strReturn = "March"
        elif self.month == 4:
            strReturn = "April"
        elif self.month == 5:
            strReturn = "May"
        elif self.month == 6:
            strReturn = "June"
        elif self.month == 7:
            strReturn = "July"
        elif self.month == 8:
            strReturn = "August"
        elif self.month == 9:
            strReturn = "September"
        elif self.month == 10:
            strReturn = "October"
        elif self.month == 11:
            strReturn = "November"
        else:
            strReturn = "December"
        return strReturn

    #author: Alan
    #date: November 1
    #purpose: check if the year is leap year
    #parameter: self
    #return: true if it's a leap year, else false
    def leapYearCheck(self):
        blnReturn = True
        if self.year%4!=0:
            blnReturn = False
        elif self.year%100!=0:
            blnReturn = True
        elif self.year%400!=0:
            blnReturn = False
        return blnReturn

    #author: Alan
    #date: November 1
    #purpose: return the max # of day in the month
    #parameter: self
    #return: 
    def returnMaxDay(self):
        intReturn = 0
        if self.month==2:
            if self.leapYearCheck():
                intReturn = 29
            else:
                intReturn = 28
        else:
            if self.month==1:
                intReturn = 31
            elif self.month==3:
                intReturn = 31
            elif self.month==4:
                intReturn = 30
            elif self.month==5:
                intReturn = 31
            elif self.month==6:
                intReturn = 30
            elif self.month==7:
                intReturn = 31
            elif self.month==8:
                intReturn = 31
            elif self.month==9:
                intReturn = 30
            elif self.month==10:
                intReturn = 31
            elif self.month==11:
                intReturn = 30
            else:
                intReturn = 31
        return intReturn

    #author: Alan
    #date: November 1
    #purpose: calculate the day of the week in 0-6
    #parameter: self
    #return: 0-6 represent the day of the week
    def calcZeller(self):
        month = self.month
        year = self.year
        day = self.day
        if month == 1 or month == 2:
            month += 12
            year -= 1 
        return ((day + 13 * (month+1) // 5 + year + year // \
                4 - year// 100 + year // 400 )%7)-1

    #author: Alan
    #date: November 1
    #purpose: return the day of the week in words
    #parameter: self
    #return: a string containing the day of the week
    def returnDayName(self):
        strReturn = ""
        if self.calcZeller()==0:
            strReturn = "Sunday"
        elif self.calcZeller()==1:
            strReturn = "Monday"
        elif self.calcZeller()==2:
            strReturn = "Tuesday"
        elif self.calcZeller()==3:
            strReturn = "Wednesday"
        elif self.calcZeller()==4:
            strReturn = "Thursday"
        elif self.calcZeller()==5:
            strReturn = "Friday"
        else:
            strReturn = "Saturday"
        return strReturn

    #author: Alan
    #date: November 1
    #purpose: check if the date is valid
    #parameter: self
    #return: true if the date is valid, else, false
    def calcValid(self):
        blnReturn = True
        if self.year <1600:
            blnReturn = False
        if self.month<1 or self.month>12:
            blnReturn = False
        if self.day<1 or self.day>self.returnMaxDay():
            blnReturn = False
        return blnReturn

    #author: Alan
    #date: November 1
    #purpose: edit for a valid date (input)
    #parameter: self
    #return: N/A
    def getDate(self):
        year = self.getPositiveInteger("Please enter a date >= 1600: ", \
                  intLow = 1600, intHigh = 5000)
        self.year = year
        month = self.getPositiveInteger("Please enter a month: ", \
                   intLow = 1, intHigh = 12)
        self.month = month
        intDate = self.getPositiveInteger("Please enter a date: ", \
                  intLow = 1, intHigh = self.returnMaxDay())
        self.date = intDate

    #author: Alan
    #date: November 1
    #purpose: return a string of the date (formatted)
    #parameter: self
    #return: a string of the date (formatted)
    def __str__ (self):
        month = str(self.month)
        day = str(self.day)
        year = str(self.year)
        return month+"/"+day+"/"+year

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
    #date: November 7
    #purpose: print the day of the year
    #parameter: self
    #return: N/A
    def dayOfYear(self):
        numberOfDays = 0
        for x in range(1, self.month):
            thisDate = Date(year = self.year, month = x)
            numberOfDays += thisDate.returnMaxDay()
        return numberOfDays + self.day
    
    #author: Alan
    #date: November 6
    #purpose: print the calendar
    #parameter: self
    #return: N/A
    def displayCalendar(self):
        print(self)
        print(self.returnMonthName())
        sys.stdout.write("    Sunday")
        sys.stdout.write("    Monday")
        sys.stdout.write("   Tuesday")
        sys.stdout.write(" Wednesday")
        sys.stdout.write("  Thursday")
        sys.stdout.write("    Friday")
        sys.stdout.write("  Saturday")
        print()
        intCount = 0;
        dateFirst = Date (str(self.year), str(self.month), "1")
        if (dateFirst.calcZeller()==0):
            intCount = 1
        elif (dateFirst.calcZeller()==1):
            intCount = 0
        elif (dateFirst.calcZeller()==2):
            intCount = -1
        elif (dateFirst.calcZeller()==3):
            intCount = -2
        elif (dateFirst.calcZeller()==4):
            intCount = -3
        elif (dateFirst.calcZeller()==5):
            intCount = -4
        else:
            intCount = -5

        for x in range(6):
            for y in range(7):
                if (intCount>0 and intCount<=self.returnMaxDay()):
                    sys.stdout.write("%10.i" %intCount)
                else:
                    sys.stdout.write(" "*10)
                intCount+=1
            print()

    #author: Alan
    #date: November 22
    #purpose: allow subtraction between dates
    #parameter: self, other
    #return: intReturn
    def __sub__(self, other):
        intReturn = 0
        intA = self.dayOfYear()
        intB = other.dayOfYear()
        for x in range(1600, self.year):
            date1 = Date(x, 12, 31)
            intA += date1.dayOfYear()
        for y in range(1600, other.year):
            date2 = Date(y, 12, 31)
            intB += date2.dayOfYear()
        intReturn = intA-intB
        return intReturn

    #author: Alan
    #date: November 22
    #purpose: allow addition between dates
    #parameter: self, other
    #return: dateReturn
    def __add__(self, other):
        intDay = abs(self - other)
        print (intDay)
        if self > other:
            dateReturn = self
        else:
            dateReturn = other
        for x in range(intDay):
            dateReturn.day += 1
            if not dateReturn.calcValid():
                if dateReturn.month>12:
                    dateReturn.year += 1
                    dateReturn.month = 1
                else:
                    dateReturn.day = 1
                    dateReturn.month += 1
                    if dateReturn.month>12:
                        dateReturn.year += 1
                        dateReturn.month = 1
        return dateReturn

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
    date1 = Date(input("Please enter a year (>=1600): "), \
                input("Please enter a month: "), \
                input("Please enter a day: "))
    date2 = Date(input("Please enter a year (>=1600): "), \
                input("Please enter a month: "), \
                input("Please enter a day: "))
    print("There are "+str(abs(date1-date2))+" days between the two dates")
    if (date1>date2):
        print("First date is greater than second date")
    elif (date<date2):
        print("First date is smaller than second date")
    else:
        print("First date is equal to second date")
    strReExecute = input("Do you wish to continue? (yes or no) ")
    while not (strReExecute == "yes" or strReExecute == "no"):
        strReExecute = input("Please enter yes or no: ")
