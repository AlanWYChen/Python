#author: Alan
#date: september 17
#purpose: loops
#input: N/A
#output: sequences
#--------------------------------------------------

import sys

intA = 5
print("sequence 1:")
while (intA<=50):
    sys.stdout.write(str(intA))
    if (intA<=47):
        sys.stdout.write(", ")
    intA = intA + 3
print()
print()

intB = 90
print("sequence 2:")
while (intB>=50):
    sys.stdout.write(str(intB))
    if (intB>=54):
        sys.stdout.write(", ")
    intB = intB - 4
print()
print()

intC = 3
print("sequence 3:")
while (intC<=24576):
    sys.stdout.write(str(intC))
    if (intC<=12288):
        sys.stdout.write(", ")
    intC = intC*2
print()
print()

intD = 1
print("sequence 4:")
while (intD<=4782969):
    sys.stdout.write(str(intD))
    if (intD<=1594323):
        sys.stdout.write(", ")
    intD = intD*3
