#author: Alan
#date: Dec 12
#purpose: Text justification
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from tkinter import *
import os.path

interface = Tk()
interface.title("Text Justification")
interface.geometry("1000x600+0+0")

strInputFile = StringVar()
strInputFile.set("input.txt")
strOutputFile = StringVar()
strOutputFile.set("output.txt")
intWidth = IntVar()
intWidth.set(30)

strType = StringVar()
strType.set("l")

strFreq = StringVar()
strFreq.set("")

#author: Alan
#date: December 21
#purpose: store word and count
#data member:
#               word: the word
#               count: the count for the word
#methods:
#               __init__: initialize an instance of wordCount
#               __str__: override str() function
class wordCount:
    #author: Alan
    #date: december 21
    #purpose: initialize an isntance of wordCount
    #parameter: word, count
    #return: N/A
    def __init__(self, word="", count=1):
        self.word = word
        self.count = count

    #author: Alan
    #date: december 21
    #purpose: override str() function
    #parameter: N/A
    #return: str(self.word)+" - "+str(self.count)
    def __str__(self):
        return str(self.word)+" - "+str(self.count)

#author: Alan
#date: December 15
#purpose:   read text from a file, justify it, and write the justified version
#           into another file
#data member:
#           wordsList: array of words (from the input file)
#           docList: array of line (of words)
#           strInputFile: name of input file
#           strOutputFile: name of output file
#           strJustification: way of justification
#           intWidth: width of each line
#methods:
#           __init__: initialize an instance of justify text
#           readFile: read from a file and put the words into wordsList
#           writeFile: write a justified text into output file
#           createDoc: create a justified text
#           justifyLeft: justify the text (left)
#           justifyRight: justify the text (right)
#           justifyCenter: justify the text (center)
#           justifyFully: justify the text (fully)
#           __str__: override the str() function
#           wordsFrequency: count the frequency of all words in the text
class JustifyText:
    #author: Alan
    #date: December 16
    #purpose: initialize an instance of JustifyText
    #parameter: self, strInputFile, strOutputFile, strJustification, intWidth
    #return: N/A
    def __init__(self,
                 strInputFile="input.txt", \
                 strOutputFile="output.txt", \
                 strJustification="l", \
                 intWidth=30):
        self.wordsList = []
        self.docList = []
        self.strInputFile = strInputFile
        self.strOutputFile = strOutputFile
        if not(strJustification=="l" or strJustification=="r" or \
               strJustification=="c" or strJustification=="f"):
            strJustification = "l"
        self.strJustification = strJustification
        intWidth = str(intWidth)
        if intWidth.isdigit():
            intWidth = int(intWidth)
        else:
            intWidth = 30
        if intWidth<30 or intWidth>90:
            intWidth = 30
        self.width = intWidth
        self.readFile()
        self.createDoc()

    #author: Alan
    #date: December 16
    #purpose: read from a file 
    #parameter: N/A
    #return: N/A
    def readFile(self):
        data = ""
        with open(self.strInputFile, 'r') as inputFile:
            data = inputFile.read().strip()
        inputFile.close()
        data = data.replace("\n", " ``` ")
        self.wordsList = data.split(" ")
        for i in range(len(self.wordsList)):
            self.wordsList[i].strip()
            if len(self.wordsList[i])>30:
                self.wordsList[i] = self.wordsList[i][:30]


    #author: Alan
    #date: December 16
    #purpose: write a justified text into a file
    #parameter: N/A
    #return: N/A
    def writeFile(self):
        outputFile = open(self.strOutputFile, "w")
        outputFile.write(self.__str__())
        outputFile.close()

    #author: Alan
    #date: December 16
    #purpose: justify the text
    #parameter: N/A
    #return: N/A
    def createDoc(self):
        if self.strJustification=="l":
            self.justifyLeft()
        elif self.strJustification=="r":
            self.justifyRight()
        elif self.strJustification=="c":
            self.justifyCenter()
        else:
            self.justifyFully()
        
    #author: Alan
    #date: December 16
    #purpose: justify the text (left)
    #parameter: N/A
    #return: N/A
    #author: Alan
    def justifyLeft(self):
        strAppend = ""
        x = 0
        while x<len(self.wordsList):
            if self.wordsList[x]=="```":
                strAppend = strAppend[:(len(strAppend)-1)]
                self.docList.append(strAppend.strip())
                strAppend = ""
            elif len(strAppend)+len(self.wordsList[x])<=self.width:
                strAppend = strAppend + self.wordsList[x]+" "
            else:
                strAppend = strAppend[:(len(strAppend)-1)]
                self.docList.append(strAppend.strip())
                strAppend = ""
                x -= 1
            x += 1
        self.docList.append(strAppend[:(len(strAppend)-1)])

    #author: Alan
    #date: December 16
    #purpose: justify the text (right)
    #parameter: N/A
    #return: N/A
    def justifyRight(self):
        self.justifyLeft()
        for i in range(0, len(self.docList)):
            space = self.width-len(self.docList[i])            
            self.docList[i]=(" "*space)+self.docList[i]

    #author: Alan
    #date: December 16
    #purpose: justify the text (center)
    #parameter: N/A
    #return: N/A
    def justifyCenter(self):
        self.justifyLeft()
        for i in range(0, len(self.docList)):
            space = self.width-len(self.docList[i])            
            self.docList[i]=(" "*(space//2))+self.docList[i]

    #author: Alan
    #date: December 16
    #purpose: justify the text (fully)
    #parameter: N/A
    #return: N/A
    def justifyFully(self):
        self.justifyLeft() 
        for i in range(len(self.docList)-1):
            if not self.docList[i].__contains__("```") \
               and self.docList[i+1]!="" and self.docList[i]!="":
                line = self.docList[i].split(" ")
                if len(line)>1:
                    space = self.width-len(self.docList[i])
                    count = len(line)-1
                    insert = space//count
                    if insert != 0:
                        self.docList[i] = \
                        self.docList[i].replace(" ", (" "*(insert+1)))
                    space -= count*insert
                    self.docList[i] = \
                    self.docList[i].replace((" "*(insert+1)), \
                                            (" "*(insert+2)), space)
            
    #author: Alan
    #date: December 16
    #purpose: override str() function
    #parameter: N/A
    #return: N/A               
    def __str__(self):
        strReturn = ""
        for x in range(len(self.docList)):
            strReturn += self.docList[x]+"\n"
        return strReturn

    #author: Alan
    #date: December 16
    #purpose: count the frequency of each word
    #parameter: N/A
    #return: N/A
    def wordsFrequency(self):
        word = []
        freq = []
        count = []
        if len(self.wordsList)>0:
            for x in range(len(self.wordsList)):
                if self.wordsList[x] not in word:
                    word.append(self.wordsList[x])
                    freq.append(1)
                else:
                    i = 0
                    cont = True
                    while cont:
                        if word[i]==self.wordsList[x]:
                            cont = False
                            freq[i] += 1
                        i += 1
        for x in range(0, len(word)):
            count.append(wordCount(word[x], freq[x]))
        return count

#author: Alan
#date: December 18
#purpose: import text, justify, and output (while writing output
#         into output file)
#parameter: N/A
#return: N/A
def new():
    if os.path.isfile(strInputFile.get()) and \
       os.path.isfile(strOutputFile.get()):
        Text =  JustifyText(strInputFile.get(), strOutputFile.get(), \
                       strType.get(), intWidth.get())
        txtBox.configure(state=NORMAL)
        txtBox.delete("1.0", END)
        txtBox.insert(END, "ORIGINAL\n")
        for x in range (len(Text.wordsList)):
            txtBox.insert(END, Text.wordsList[x].replace("```", "\n"))
            if Text.wordsList[x]!="```":
                txtBox.insert(END, " ")
        txtBox.insert(END, "\n \n")
        txtBox.insert(END, "JUSTIFIED\n")
        txtBox.insert(END, str(Text))
        txtBox.configure(state=DISABLED)
        count = Text.wordsFrequency()
        strFreq.set(str(count[0]))
        for i in range(1, len(count)):
            if count[i].word!="```" and count[i].word!="":
                strFreq.set(strFreq.get()+"\n"+str(count[i]))
        Text.writeFile()
    else:
        messagebox.showinfo("Alert", "No such file exists")

def word():
    messagebox.showinfo("Frequency", strFreq.get())

#main
master = Frame(interface)
master.place(x=5, y=5)
scroll = Scrollbar(master)
scroll.pack(side = RIGHT, fill = Y)

txtBox = Text (master, yscrollcommand = scroll.set, width=102, height=39, \
               bg = "grey", state=DISABLED)
txtBox.pack(side=LEFT, fill = Y)
scroll.config(command=txtBox.yview)

lblInputFile = Label (interface, text = "Input File Name", width=25)
lblInputFile.place (x = 753, y = 15)
entryInputFile = Entry (interface, textvariable = strInputFile, \
                        width = 25)
entryInputFile.place (x = 753, y = 40)
lblOutputFile = Label (interface, text = "Output File Name", width=25)
lblOutputFile.place (x = 753, y = 75)
entryOutputFile = Entry (interface, textvariable = strOutputFile, \
                         width = 25)
entryOutputFile.place (x = 753, y = 100)

frmType = Frame (interface, height = 256, width = 232, bg = "grey")
frmType.place(x = 755, y = 140)

lblType = Label (frmType, height = 2, width = 23, text = "Justification")
lblType.place (x = 8, y = 8)

rdbLeft = Radiobutton (frmType, text = "Left", variable = strType, \
           value = "l", height=2, width = 23)
rdbLeft.place(x =8, y = 58)

rdbRight = Radiobutton (frmType, text = "Right", variable = strType, \
            value = "r", height=2, width = 23)
rdbRight.place(x = 8, y = 108)

rdbCenter = Radiobutton (frmType, text = "Center", variable = strType, \
            value = "c", height=2, width = 23)
rdbCenter.place(x = 8, y = 158)

rdbFully = Radiobutton (frmType, text = "Fully", variable = strType, \
            value = "f", height=2, width = 23)
rdbFully.place(x = 8, y = 208)

sclWidth = Scale(interface, from_= 30, to = 90, orient=HORIZONTAL, \
                 variable = intWidth, label="Width of justification", \
                length=233)
sclWidth.place(x=753, y=400)

btnInput = Button (interface, width = 23, \
                   text = "Import, Justify Export (and Print)", \
                   command=lambda: new())
btnInput.place(x=753, y = 475)

btnFreq = Button (interface, width = 23, \
                  text = "Get words frequency", \
                  command=lambda: word())
btnFreq. place(x = 753,  y = 525)
mainloop()
