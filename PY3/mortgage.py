#Author: Alan
#Date: September 28
#Purpose: Calculate monthly mortgage
#Input: interest rate and the number of years
#Output: a table for monthly mortgage rate with
#        different number of years and different interest rate
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import sys

#=================================================================

restart = "yes"

while restart=="yes" or restart=="y":
    #input
    mortgageAmount = float (input("enter your amount of mortage: "))

    #edit loop
    while (mortgageAmount<50000):
        mortgageAmount =  float (input("enter your amount of mortage: "))

    
    #formatting purposes
    print ("                                                        years")
    sys.stdout.write("             ")

    #printing the chart
    for year in range(5, 36, 5):
        sys.stdout.write("%14.i" %year)

    print()
    print(" interest rate")

    for interestRate in range(1, 25):
        rate = interestRate/4
        sys.stdout.write("%14.2f" %rate)
        sys.stdout.write("  ")
        for years in range(5, 36, 5):
            n = years*12
            i = ((1+(rate/200))**(1/6))-1
            f = 1/((1-(1+i)**-n)/i)
            monthlyPayment = f*mortgageAmount
            sys.stdout.write("$%10.2f" %monthlyPayment)
            sys.stdout.write("   ")
        print()

    restart = input("do you want to restart? Yes or No ")
