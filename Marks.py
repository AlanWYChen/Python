#author: Alan
#date: September 17
#purpose: Marks
#input: a number between 0 and 100 (inclusive)
#output: the mark converted to level
#-----------------------------------

while True: 
    grade = float (input("your mark: "))
    if grade>=0 and grade<=100:
        break

if grade<=39:
    print("fail")
elif grade<=49:
    print("Credit Recovery")
elif grade <= 59:
    print("Level 1")
elif grade <=69:
    print("Level 2")
elif grade <=79:
    print("Level 3")
else:
    print("Level 4")
    
