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
            data = inputFile.read()
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
    #date: December 16
    #purpose: justify the text (left)
    #parameter: N/A
    #return: N/A
    def justifyLeft(self):
        strAppend = ""
        x = 0
        while x<len(self.wordsList):
            if self.wordsList[x]=="```":
                strAppend = strAppend[:(len(strAppend)-1)]
                self.docList.append(strAppend)
                strAppend = ""
            elif len(strAppend)+len(self.wordsList[x])<=self.width:
                strAppend = strAppend + self.wordsList[x]+" "
            else:
                strAppend = strAppend[:(len(strAppend)-1)]
                self.docList.append(strAppend)
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
        for i in range(len(self.docList)):
            if not self.docList[i].__contains__("```"):
                line = self.docList[i].split(" ")
                if len(line)>2:
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
        word  = []
        count = []
        for x in range(len(self.wordsList)):
            if self.wordsList[x] not in word:
                word.append(self.wordsList[x])
                count.append(1)
            else:
                i = 0
                cont = True
                while cont:
                    if word[i]==self.wordsList[x]:
                        cont = False
                        count[i] += 1
                    i += 1
        for i in range(len(word)):
            print(str(word[i])+" - "+str(count[i]))

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

A = wordCount("asgq", 1)
print(A)
