#a uthor: Alan Chen
#date: October 16
#purpose: Number theory with GUI
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from tkinter import *

interface = Tk()
interface.geometry("350x400+0+0")
interface.title("Number Theory")

#global variable================================================================

strInput1 = StringVar()
strInput1.set("0")
strInput2 = StringVar()
strInput2.set("0")
strPermutation = StringVar()
strPermutation.set("")
strCombination = StringVar()
strCombination.set("")
strGCD = StringVar()
strGCD.set("")
strLCM = StringVar()
strLCM.set("")
strRP = StringVar()
strRP.set(value = "")

#functions/procedures===========================================================

#author: Alan
#date: October 10
#purpose: Edit input for a integer between intLow and intHigh
#parameter: strPrompt, intLow, intHigh
#return: one positive integer
def getPositiveInteger(strPrompt, strInput, intLow=0, intHigh=100):
    intReturn = 0
    strInput = str (strInput)
    if not strInput.isdigit():
        messagebox.showinfo(strPrompt, "Error, input must be integers")
        intReturn = -1
    else:
        if int (strInput)<=0 or int (strInput)>=100:
            messagebox.showinfo \
            (strPrompt, "Error, input must be between 0 and 100 (exclusive)")
            intReturn = -1
        if (intReturn!=-1):
            intReturn = int (strInput)
        return intReturn

#author: Alan
#date: October 10
#purpose: calculate the factorial of a number
#parameter: an integer
#return: the factorial of a number
def calcFactorial(intN):
    if intN==0 or intN==1:
        return 1
    else:
        return int (intN*calcFactorial(intN-1))

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
    blnReturn = False
    if calcGCD(intM, intN)==1:
        blnReturn = True
    return blnReturn
    

#author: Alan
#date: October 18
#purpose: output
#parameter: N/A
#return: N/A
def output():
    intN1 = getPositiveInteger("ERROR: First Input", strInput1.get())
    intN2 = getPositiveInteger("ERROR: Second Input", strInput2.get())
    if not (intN1 == -1 or intN2 == -1):
        strPermutation.set(str(calcPermutations(intN1, intN2)))
        strCombination.set(str(calcCombinations(intN1, intN2)))
        strGCD.set(str(calcGCD(intN1, intN2)))
        strLCM.set(str(calcLCM(intN1, intN2)))
        blnRP = isRelativelyPrime(intN1, intN2)
        if blnRP == True:
            strRP.set("True")
        else:
            strRP.set("False")

#author: Alan
#date: October 29
#purpose: clear the interface
#parameter: N/A
#return: N/A
def clear():
    strInput1.set("0")
    strInput2.set("0")
    strPermutation.set("")
    strCombination.set("")
    strGCD.set("")
    strLCM.set("")
    strRP.set("")

#author: Alan
#date: October 29
#purpose: change font to Helvetica
#parameter: N/A
#return: N/A
def fontHelvetica():
    lblInput1.config(font=("Helvetica"))
    entryInput1.config(font=("Helvetica"))
    lblInput2.config(font=("Helvetica"))
    entryInput2.config(font=("Helvetica"))
    buttonCalc.config(font=("Helvetica"))
    lblPermutation.config(font=("Helvetica"))
    lblPOutput.config(font=("Helvetica"))
    lblCombination.config(font=("Helvetica"))
    lblCOutput.config(font=("Helvetica"))
    lblGCD.config(font=("Helvetica"))
    lblGCDOutput.config(font=("Helvetica"))
    lblLCM.config(font=("Helvetica"))
    lblLCMOutput.config(font=("Helvetica"))
    lblRelativePrime.config(font=("Helvetica"))
    lblRPOutput.config(font=("Helvetica"))
    entryInput1.config(width = 23)
    entryInput2.config(width = 23)
    lblPOutput.config(width = 23)
    lblCOutput.config(width = 23)
    lblGCDOutput.config(width = 23)
    lblLCMOutput.config(width = 23)
    lblRPOutput.config(width = 23)

#author: Alan
#date: October 29
#purpose: change font to Default
#parameter: N/A
#return: N/A
def fontDefault():
    lblInput1.config(font=("Default"))
    entryInput1.config(font=("Default"))
    lblInput2.config(font=("Default"))
    entryInput2.config(font=("Default"))
    buttonCalc.config(font=("Default"))
    lblPermutation.config(font=("Default"))
    lblPOutput.config(font=("Default"))
    lblCombination.config(font=("Default"))
    lblCOutput.config(font=("Default"))
    lblGCD.config(font=("Default"))
    lblGCDOutput.config(font=("Default"))
    lblLCM.config(font=("Default"))
    lblLCMOutput.config(font=("Default"))
    lblRelativePrime.config(font=("Default"))
    lblRPOutput.config(font=("Default"))
    entryInput1.config(width = 20)
    entryInput2.config(width = 20)
    lblPOutput.config(width = 20)
    lblCOutput.config(width = 20)
    lblGCDOutput.config(width = 20)
    lblLCMOutput.config(width = 20)
    lblRPOutput.config(width = 20)

#author: Alan
#date: October 29
#purpose: change font to Symbol
#parameter: N/A
#return: N/A
def fontSymbol():
    lblInput1.config(font=("Symbol"))
    entryInput1.config(font=("Symbol"))
    lblInput2.config(font=("Symbol"))
    entryInput2.config(font=("Symbol"))
    buttonCalc.config(font=("Symbol"))
    lblPermutation.config(font=("Symbol"))
    lblPOutput.config(font=("Symbol"))
    lblCombination.config(font=("Symbol"))
    lblCOutput.config(font=("Symbol"))
    lblGCD.config(font=("Symbol"))
    lblGCDOutput.config(font=("Symbol"))
    lblLCM.config(font=("Symbol"))
    lblLCMOutput.config(font=("Symbol"))
    lblRelativePrime.config(font=("Symbol"))
    lblRPOutput.config(font=("Symbol"))
    entryInput1.config(width = 25)
    entryInput2.config(width = 25)
    lblPOutput.config(width = 25)
    lblCOutput.config(width = 25)
    lblGCDOutput.config(width = 25)
    lblLCMOutput.config(width = 25)
    lblRPOutput.config(width = 25)

#main===========================================================================
    
menubar = Menu(interface)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_separator()
filemenu.add_command(label="Clear",command=lambda: clear())
filemenu.add_command(label="Exit",command=lambda:interface.destroy())
menubar.add_cascade(label="File", menu=filemenu)


fontmenu = Menu(menubar, tearoff=0)
fontmenu.add_command(label="Default", command=lambda: fontDefault())
fontmenu.add_command(label="Helvetica", command=lambda: fontHelvetica())
fontmenu.add_command(label="Symbol", command=lambda: fontSymbol())
menubar.add_cascade(label="Font", menu=fontmenu)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)

interface.config(menu=menubar)


lblInput1 = Label (interface, text = "First Number:", width = 15, height = 3)
lblInput1.place (x = 15, y = 5)


entryInput1 = Entry (interface, textvariable = strInput1)
entryInput1.place (x = 135, y = 20)

lblInput2 = Label (interface, text = "Second Number:", width = 15, height = 2)
lblInput2.place (x = 5, y = 55)

entryInput2 = Entry (interface, textvariable = strInput2)
entryInput2.place (x = 135, y = 60)

buttonCalc = Button (interface, text = "Calculate!", width = 10, height = 2, \
             command = lambda: output())
buttonCalc.place (x = 117, y = 91)

lblPermutation = Label(interface, text = "Permutation: ", width = 15, \
                 height = 2)
lblPermutation.place (x = 5, y = 135)

lblPOutput = Label(interface, textvariable = strPermutation, width = 20, \
             height = 2, borderwidth = 2, relief="groove")
lblPOutput.place (x = 135, y = 135)

lblCombination = Label(interface, text = "Combination: ", width = 15, \
                 height = 2)
lblCombination.place (x = 5, y = 185)

lblCOutput = Label(interface, textvariable = strCombination, width = 20, \
             height = 2,borderwidth = 2, relief="groove")
lblCOutput.place (x = 135, y = 185)

lblGCD = Label(interface, text = "GCD: ", width = 15, height = 2)
lblGCD.place (x = 5, y = 235)

lblGCDOutput = Label(interface, textvariable = strGCD, width = 20, \
               height = 2, borderwidth = 2, relief="groove")
lblGCDOutput.place (x = 135, y = 235)

lblLCM = Label(interface, text = "LCM: ", width = 15, height = 2)
lblLCM.place (x = 5, y = 285)

lblLCMOutput = Label(interface, textvariable = strLCM, width = 20, \
               height = 2, borderwidth = 2, relief="groove")
lblLCMOutput.place (x = 135, y = 285)

lblRelativePrime = Label(interface, text = "Relative Prime: ", width = 15, \
                   height = 2)
lblRelativePrime.place (x = 5, y = 335)

lblRPOutput = Label(interface, textvariable = strRP, width = 20, height = 2, \
              borderwidth = 2, relief="groove")
lblRPOutput.place (x = 135, y = 335)

interface.mainloop()
