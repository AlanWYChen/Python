#Author: Alan Chen
#Date: September 21
#Purpose: Digits of a number
#Input: a positive integer
#Output: number of digits, sum of digits, reverse of the number, palindrome
#        check, digital root
#=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#input
Input = int (input("enter your number: "))

#editing input
while (Input<0):
    Input = int (input("enter your number: "))

#keeping an original copy of Input
copyOfInput = Input

#using for loop and div and mod to find sum of digits and number of digits
count = 0
flag = False
sumOfDigits = 0
for x in range(18, -1, -1):
    digit = 10**x
    valueOfDigit = Input//digit
    if (valueOfDigit!=0):
        flag=True
    if (flag==False):
        count+=1
    sumOfDigits += valueOfDigit
    Input -= digit*valueOfDigit

numberOfDigits = 19-count

print("number of digits:",numberOfDigits)
print("the sum of the digits:", sumOfDigits)

#reverse of the number
Input = copyOfInput
Reverse = 0
while(Input > 0):    
    Remainder = Input%10    
    Reverse = (Reverse*10) + Remainder    
    Input = Input//10
     
print("reverse of the number is: ",Reverse)

#palindrome check
#if input and reverse is the same then number is a palindrome
Input = copyOfInput

if(Input==Reverse):
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")

#digital root
#literally to temporaily hold the number
temporarilyHold = 0

#literally do sum of digit a bunch of time
while (sumOfDigits>10 and sumOfDigits<0):
    for x in range(0, 3):
        digit = 10**x
        valueOfDigit = Input//digit
        temporarilyHold +=valueOfDigit
    sumOfDigits = temporailyHold
    temporilyHold = 0

print("the digital root of the number is: ",sumOfDigits)

#READ THIS
#print("I.T. I.S. S.O. M.U.C.H. E.A.S.I.E.R. T.O. D.O. W.I.T.H. S.T.R.I.N.G.S.")
