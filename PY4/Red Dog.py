#author: Alan
#date: October 11
#purpose: Simulation game - Red Dog
#=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import random

#author: Alan
#date: October 11
#purpose: store two integers
class TwoCard:
  def __init__(self, card1, card2):
    self.card1 = card1
    self.card2 = card2

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
#date: October 11
#purpose: get a random card
#parameter: N/A
#return: a random integer between 2 to 14

def getCard():
    intRnd = random.randint(2, 14)
    return intRnd

#author: Alan
#date: october 11
#purpose: get hand
#parameter: N/A
#return: a TwoCard object

def getHand():
    return TwoCard(getCard(), getCard())

#author: Alan
#date: October 11
#purpose: print the hand
#parameter: TwoCard object
#return: 2 integers in the object

def printHand(hand):
    if hand.card1 == 11:
      print ("the first card is Jack")
    elif hand.card1 == 12:
      print ("the first card is Queen")
    elif hand.card1 == 13:
      print ("the first card is King")
    elif hand.card1 == 14:
      print ("the first card is Ace")
    else:
        print("the first card is ",hand.card1)

    if hand.card2 == 11:
      print ("the second card is Jack")
    elif hand.card2 == 12:
      print ("the second card is Queen")
    elif hand.card2 == 13:
      print ("the second card is King")
    elif hand.card2 == 14:
      print ("the second card is Ace")
    else:
      print("the second card is ",hand.card2)

#author: Alan
#date: October 11
#purpose: determine the type of hand
#parameter: TwoCard object
#return: type of hand (pair, consecutive, or non-consecutive)

def getHandType(hand):
    strReturn = ""
    if hand.card1 == hand.card2:
        strReturn = "pair"
    elif abs(hand.card1 - hand.card2)==1:
        strReturn = "consecutive"
    else:
        strReturn = "non-consecutive"
    return strReturn

#author: Alan
#date: October 11
#purpose: find the spread of a TwoCard Object
#parameter: TwoCard object
#return: the spread

def getSpread(hand):
    return max(hand.card1, hand.card2)-min(hand.card1, hand.card2)-1

#author: Alan
#date: October 11
#purpose: find the payout of a hand
#parameter: TwoCard object
#return: payout

def getPayout(hand):
    intReturn = 1
    if getSpread(hand)==1:
        intReturn = 5
    elif getSpread(hand)==2:
        intReturn = 4
    elif getSpread(hand)==3:
        intReturn = 2
    return intReturn

#author: Alan
#date: October 11
#purpose: if a card is between (exclusive) a TwoCard object
#parameter: an integer and a TwoCard object
#return: true if the int is between the TwoCard object, else, false

def isBetween(card, hand):
    blnReturn = False
    if card<max(hand.card1, hand.card2) and card>min(hand.card1, hand.card2):
        blnReturn = True
    return blnReturn

#main

#instructions
print("HOW TO PLAY RED DOG:")
print("1. Your wallet starts with $100")
print("2. Each round you make a bet between $1 to how much money in your wallet")
print("3. The system randomly picks two cards")
print("   a. If the two cards are equal:")
print("      Randomly picks a third card, if all three are equal, gain bet x 11")
print("      If not, tied")
print("   b. If the two cards are consecutives, tied")
print("   c. If the two cards are neither of the above, then bet a third bet:")
print("       adsaf")
print("")
print("")

blnFlag = True
intPurse = 100

print("your wallet have: $", intPurse)

while blnFlag == True and intPurse > 0:
    intBet = getPositiveInteger ("enter your bet: ", 1, intPurse)
    hand = getHand()
    printHand(hand)
    if getHandType(hand)=="pair":
        intCard = getCard()
        
        if intCard == 11:
          print ("the third card is Jack")
        elif intCard == 12:
          print ("the third card is Queen")
        elif intCard == 13:
          print ("the third card is King")
        elif intCard == 14:
          print ("the third card is Ace")
        else:
          print ("the third card is ", intCard)
        
        if intCard == hand.card1:
          intPurse += intBet*11 
        else:
          print("It was a tie!")
    elif getHandType(hand)=="consecutive":
        print("It was a tie!")
    else:
        intSeconndBetLim = min(intPurse-intBet, intBet)
        intAdditionalBet = getPositiveInteger \
        ("enter your additional bet: ", intHigh = min(intPurse, intBet))
        intBet += intAdditionalBet
        intPurse -= intAdditionalBet
        intCard = getCard()
        
        if intCard == 11:
          print ("the third card is Jack")
        elif intCard == 12:
          print ("the third card is Queen")
        elif intCard == 13:
          print ("the third card is King")
        elif intCard == 14:
          print ("the third card is Ace")
        else:
          print ("the third card is ", intCard)
        
        if isBetween(intCard, hand):
            intPurse += intBet*getPayout(hand)
        else:
            intPurse -= intBet
    print("your wallet still have: $", intPurse)

    if intPurse > 0:
      strReExecute = input("do you wish to continue? (Yes or No) ")
      while (strReExecute!="Yes" and strReExecute!="No"):
        strReExecute = input("Please enter Yes or No: ")
    if strReExecute == "No":
        blnFlag = False
