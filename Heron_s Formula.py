#author: Alan Chen
#date: September 17
#purpose: Heron's formula (with edit loop)
#input: side lengths of a triangle
#output: area of the triangle
#--------------------------------------------------------------

import math

while (True):
    sideA = float (input("length of side A: "))
    sideB = float (input("length of side B: "))
    sideC = float (input("length of side C: "))
    if not(sideA<0 or sideB<0 or sideC<0 or sideA+sideB<=sideC \
           or sideA+sideC<=sideB or sideB+sideC<=sideA):
        break
    else:
        print ("Error: a triangle cannot be made with the above measurements", \
               "please input a new set of measurements.")

semiP = 1.0/2*(sideA+sideB+sideC)

print ("the area of your triangle is", \
       (math.sqrt(semiP*(semiP-sideA)*(semiP-sideB)*(semiP-sideC))), \
       "units squared")
