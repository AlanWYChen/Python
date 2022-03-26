#Author: Alan
#Date: September 28
#Purpose: Output star patterns
#Input: Type of star, hollow or not hollow, and size
#Output: the pattern using "* "
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import sys

#=================================================

restart = "yes"

while restart=="yes" or restart=="y":
    #input
    typeOfShape = int(input("Type of shape: 1 is square, 2 is triangle, 3 is diamond, 4 is cross: "))
    if typeOfShape!=4:
        hollowness = int(input("Solid, press 1, hollow, press 2: "))
    size = int(input("Enter the size of your shape: "))

    #editing the size if the user wants to print a diamond
    while typeOfShape == 3 and size%2 == 0:
        size = int(input("Enter the size of your shape again, it must be odd: "))

    #square
    if typeOfShape == 1:
        #solid
        if hollowness == 1:
            for x in range(0,size):
                for y in range(0,size):
                    sys.stdout.write("* ")
                print()
        #hollow
        if hollowness == 2:
            for x in range(0,size):
                for y in range(0,size):
                    if x == 0 or x == size-1 or y == 0 or y == size -1:
                        sys.stdout.write("* ")
                    else:
                        sys.stdout.write("  ")
                print()

    #triangle
    if typeOfShape == 2:
        #solid
        if hollowness == 1:
            for x in range(1,size+1):
                for y in range(0,x):
                    sys.stdout.write("* ")
                print()
        #hollow
        if hollowness == 2:
            for x in range(1,size+1):
                for y in range(0,x):
                    if y == 0 or y == x-1 or x == size:
                        sys.stdout.write("* ")
                    else:
                        sys.stdout.write("  ")
                print()

    #diamond
    if typeOfShape == 3:
        marker = 1
        #solid
        if hollowness == 1:
            for x in range(0,size):
                for space in range(0,(size-marker)//2):
                    sys.stdout.write("  ")
                for y in range(0,marker):
                    sys.stdout.write("* ")
                if x+1<size//2+1:
                    marker = marker + 2
                else:
                    marker = marker - 2
                print()
        #hollow
        if hollowness == 2:
            for x in range(0,size):
                for space in range(0,(size-marker)//2):
                    sys.stdout.write("  ")
                for y in range(0,marker):
                    if y == 0 or y == marker-1:
                        sys.stdout.write("* ")
                    else:
                        sys.stdout.write("  ")
                if x+1<size//2+1:
                    marker = marker + 2
                else:
                    marker = marker - 2
                print()

    #Cross
    if typeOfShape == 4:
        counter = 1
        for x in range(0,size):
            for mark in range(0,counter):
                sys.stdout.write("* ")
            for space in range(0,size+2-2*counter):
                sys.stdout.write("  ")
            for mark in range(0,counter):
                if counter + mark <size+2:
                    sys.stdout.write("* ")
            counter += 1
            print()
            
        sys.stdout.write("  ")
        for x in range(0,size):
            sys.stdout.write("* ")
        print()
        if size %2 == 1:
            counter = 1
        else:
            counter = 2
        for x in range(0,size):
            cOne = 0
            for mark in range(0,size-x):
                sys.stdout.write("* ")
                cOne+=1
            if x>(size)//2-1:
                for space in range(0,counter):
                    sys.stdout.write("  ")
                counter+=2
            for mark in range(0,size-x):
                if size%2==1:
                    if mark+cOne+space<size+2:
                        sys.stdout.write("* ")
                else:
                    if mark+cOne+space<=size+2:
                        sys.stdout.write("* ")
            print()

    restart = input("do you want to restart? Yes or No ")    
