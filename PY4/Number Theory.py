#author: Alan
#date: October 9
#purpose: Functions - number Theory
#function: getPositiveInteger, calcFactorial, calcPermutations,
#          calcCombinations, calcGCD, calcLCM, isRelativelyPrime
#input: 2 positive integer
#output: print the permutations, combinations, GCD, LCM, if they are
#        relative primes
#=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#author: Alan
#date: October 24
#purpose: type check
#parameter: strPrompt, strInput
#return: one integer
def typeCheck(strPrompt, strInput):
    while not strInput.isdigit():
        strInput = input(strPrompt)
    return int (strInput)

#author: Alan
#date: October 24
#purpose: Edit input for a integer between intLow and intHigh
#parameter: strPrompt, intLow, intHigh
#return: one positive integer
def getPositiveInteger(strPrompt="Please enter a number: ", intLow=0, intHigh=100):
    intInput = typeCheck(strPrompt, input(strPrompt))
    while intInput<intLow or intInput>intHigh:
        intInput = intInput = typeCheck(strPrompt, input(strPrompt))
    return intInput
    

#author: Alan
#date: October 10
#purpose: calculate the factorial of a number
#parameter: an integer
#return: the factorial of a number
def calcFactorial(intN):
    if intN==0 or intN==1:
        return 1
    else:
        return int(intN*calcFactorial(intN-1))

#author: Alan
#date: October 10
#purpose: calculate intN P intR
#parameter: intN, intR
#return: intN P intR
def calcPermutations(intN, intR):
    if intN<intR:
        store = intN
        intN = intR
        intR = store
    return int (calcFactorial(intN)/(calcFactorial(intN-intR)))

#author: Alan
#date: October 10
#purpose: calculate intN C intR
#parameter: intN, intR
#return: intN C intR
def calcCombinations(intN, intR):
    if intN<intR:
        store = intN
        intN = intR
        intR = store
    return int (calcFactorial(intN)/ \
           (calcFactorial(intR)*(calcFactorial(intN-intR))))

#author: Alan
#date: October 10
#purpose: calculate the GCD of two numbers
#parameter: intM, intN
#return: GCD
def calcGCD(intM, intN):
    intT = intM%intN
    while intT != 0:
        intM = intN
        intN = intT
        intT = intM%intN
    return intN

#author: Alan
#date: October 10
#purpose: Calculate LCM of two numbers
#parameter: intM, intN
#return: LCM
def calcLCM(intM, intN):
    return int (intM*intN/calcGCD(intM, intN))

#author: Alan
#date: October 10
#purpose: check if two number are relatively prime
#parameter: intM, intN
#return: true if they are relatively prime, else false
def isRelativelyPrime(intM, intN):
    if calcGCD(intM, intN)==1:
        return True
    return False

#main
blnFlag = True

while blnFlag:
    intInput1 = getPositiveInteger("Enter the value of the first number: ")
    intInput2 = getPositiveInteger("Enter the value of the second number: ")

    print(max(intInput1,intInput2), "P", min(intInput1,intInput2),"=", calcPermutations(intInput1, intInput2))
    print(max(intInput1,intInput2), "C", min(intInput1,intInput2),"=",calcCombinations(intInput1, intInput2))
    print("GCD of", intInput1, "and", intInput2, "is", calcGCD(intInput1, intInput2))
    print("LCM of", intInput1, "and", intInput2, "is",calcLCM(intInput1, intInput2))

    if isRelativelyPrime(intInput1, intInput2):
        print("They are relatively prime")
    else:
        print("They are not relatively prime")
    
    strReExecute = input("do you wish to rerun the program?")
    while strReExecute != "Yes" and strReExecute != "yes" and strReExecute != "No" and strReExecute != "no":
        strReExecute = input("do you wish to rerun the program? (Yes or No)")
    if strReExecute == "No" or strReExecute == "no":
        blnFlag = False


