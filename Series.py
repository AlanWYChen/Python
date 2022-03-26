#author: Alan
#date: september 17
#purpose: series (calculation)
#input: N/A
#output: the answer to the sequence
#--------------------------------------------------------

Ans1 = 1
A = 1
while (A<=20):
    Ans1 = Ans1*A
    A += 1

print("Sequence 1: ", Ans1)

Ans2 = 0
X = 1
B = 0
while(B<=1000000):
    if (B%2==0):
        Ans2 = Ans2 + 1/X
    else:
        Ans2 = Ans2 - 1/X
    X = X + 2
    B += 1
    
print("Sequence 2: ", 4*Ans2)
    
Ans3 = 0
Y = 1
C = 0
while C<1000000:
    Ans3 = Ans3 + 1/(Y*(Y+2))
    Y = Y + 2
    C += 1

print("Squence 3: ", Ans3)
