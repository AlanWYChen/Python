#author: Alan
#date: September 17
#purpose: middle
#input: 3 even positive integers
#output: the middle number
#--------------------------------------------------

while True:
    intX = int (input("first number: "))
    intY = int (input("second number: "))
    intZ = int (input("third number: "))
    if (intX>0 and intY>0 and intZ>0 and intX%2==0 and intY%2==0 and intZ%2==0):
        break


list = [intX, intY, intZ]
list.sort()

print ("the middle number is: ",list[1])
