#Author: Alan
#Date: September 23
#Purpose: Smallest and largest number
#Input: x number of integers with the last one being -99999
#Output: Smallest and largest number
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#create list to store the value of all numbers

import sys

sumOfNumbers = 0
count = -1
Input = int (input("enter a number: "))

if (Input!=-9999):
    sumOfNumbers+=Input
else:
    while (Input==-9999):
        Input = int (input("Error: enter a number: "))
    sumOfNumber = Input

intSmallest = Input
intLargest = Input

while (Input!=-9999):
    Input = int(input("enter a number: "))
    if (Input!=-9999):
        if (Input<intSmallest):
            intSmallest = Input
        if (Input>intLargest):
            intLargest = Input
        sumOfNumbers += Input
        count+=1    #number of inputs (for enrichment)

#sort function sorts the list from smallest to largest
print("the smallest number is: ",intSmallest)
print("the largest number is: ",intLargest)

#enrichment

average = sumOfNumbers/(count+1)

print("the average of the valid numbers is: ",average)

