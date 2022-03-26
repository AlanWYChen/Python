#Author: Alan Chen
#Date: September 21
#Purpose: Digits of a number
#Input: a positive integer
#Output: number of digits, sum of digits, reverse of the number, palindrome
#        check, digital root
#=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#sys.maxint = 9,223,372,036,854,775,807

import sys

Input = int (input("enter your number: "))

while (Input<0):
    Input = int (input("Error: enter a new number: "))

number = []

for x in range(0, 19):
    number.append(0)

for x in range(18, -1, -1):
    digit = 10**x
    number[18-x] = Input//digit
    Input = Input - digit*number[18-x]

numberOfDigits = 0

for x in range(0, 19):
    if (number[x]!=0):
        numberOfDigits+=1

print("the number of digits in the number is: ",numberOfDigits)

sumOfDigits = 0

for x in range(0, 19):
    sumOfDigits += number[x]

print ("the sum of the digits is:",sumOfDigits)

sys.stdout.write("the reverse of the number: ")
for x in range (18, 18-numberOfDigits, -1):
    sys.stdout.write(str(number[x]))

flag = True

for x in range(0, numberOfDigits):
    if (number[x]!=number[numberOfDigits-x-1]):
        flag = False

print()

if(flag):
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")


digitalRootList = []

for x in range(len(sumOfDigits)-1, -1, -1):
    digitalRootList.appends()
    








