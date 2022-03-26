#Name: Alan
#Date: September 25
#Purpose: Cashier problem
#Input:Purchased amount and given cash
#Output: Most optimal Change
#=========================================================
# input
purchase = float(input("enter your purchase price: "))
while purchase <0:
    purchase = int (input("enter your purchase price again, previous one was invalid: "))

givenCash = float(input("enter your cash given: "))
while givenCash<purchase:
    givenCash = int (input("enter your cash given again, previous one was invalid: "))
    
#calculatinng the amount of change per type of bill
    #using floor division to get the number of bills
    #using mod to find the remainder and moves on the next type of bills
#mulitplies everything by 100
    #easier to work with integers rather than variable
    #div and mod can't work with decimal numbers
changeDue = (givenCash-purchase)*100
if changeDue%5>=3:
    remain = changeDue%5
    changeDue += 5-remain
fiftiesDue = changeDue//5000
fiftiesRemainder = changeDue%5000

twentiesDue = fiftiesRemainder//2000
twentiesRemainder = fiftiesRemainder%2000

tensDue = twentiesRemainder//1000
tensRemainder = twentiesRemainder%1000

fivesDue = tensRemainder//500
fivesRemainder = tensRemainder%500

twosDue = fivesRemainder//200
twosRemainder = fivesRemainder%200

onesDue = twosRemainder//100
onesRemainder = twosRemainder%100

quartersDue = onesRemainder//25
quartersRemainder = onesRemainder%25

dimesDue = quartersRemainder//0.10
dimesRemainder = quartersRemainder%10

nickelsDue = dimesRemainder//5
nickelsRemainder = dimesRemainder%5

#rounding to the nnearest $0.05
if nickelsRemainder>=3:
    nickelsDue+=1
    
#output
changeDue = changeDue/100
print ("purchase price:","%0.2f" % purchase)
print ("cash given:","%0.2f" % givenCash)
print ("change Due:","%0.2f" % changeDue)

if fiftiesDue>0:
    print("%10.i" % (fiftiesDue),"- $50.00 =","%10.2f" % (fiftiesDue*50.00))
if twentiesDue>0:
    print("%10.i" % (twentiesDue),"- $20.00 =","%10.2f" % (twentiesDue*20.00))
if tensDue>0:
    print("%10.i" % (tensDue),"- $10.00 =","%10.2f" % (tensDue*10.00))
if fivesDue>0:
    print("%10.i" % (fivesDue),"-  $5.00 =","%10.2f" % (fivesDue*5.00))
if twosDue>0:
    print("%10.i" % (twosDue),"-  $2.00 =","%10.2f" % (twosDue*2.00))
if onesDue>0:
    print("%10.i" % (onesDue),"-  $1.00 =","%10.2f" % (onesDue*2.00))
if quartersDue>0:
    print("%10.i" % (quartersDue),"-  $0.25 =","%10.2f" % (quartersDue*0.25))
if dimesDue>0:
    print("%10.i" % (dimesDue),"-  $0.10 =","%10.2f" % (dimesDue*0.10))
if nickelsDue>0:
    print("%10.i" % (nickelsDue),"-  $0.05 =","%10.2f" % (nickelsDue*0.05))



