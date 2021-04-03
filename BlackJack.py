import random
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
card_point = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11,"A1":1}
deck = []
for i in range(0,4):
    for card in cards:
        deck.append(card)

def optimalAce(card,newVal):
    if("A" in card and newVal=="A"):
        return "A1"
    return newVal

def sumScores(cards):
    global card_point
    total = 0
    for i in range(len(cards)):
        total += card_point[cards[i]]
    return total


def optimalAceValue(currentScore):
    if(currentScore+11>21):
        return currentScore+1
    return currentScore+11

def showCards(cards):
    cardString = " "
    return cardString.join(cards)

def humanWins(humanScore):
    if humanScore == 21:
        print("Player wins")
        print("Blackjack!")
        quit()

def checkHumanBust(humanScore):
    if(humanScore == 21):
        print("Player wins" + "\nBlackjack!")
        quit()
    elif(humanScore > 21):
        print("Player busts with "+ str(humanScore) +"\nDealer wins")
        quit()

def checkDealerBust(dealerScore, humanScore, humanCards, dealerCards):
    if dealerScore == humanScore:
        print("TIE!")
        quit()
    elif dealerScore<=21 and humanScore<=21:
        if humanScore>dealerScore:
            print("Player wins!" + "\n"+showCards(humanCards)+" = " + str(humanScore) + " to Dealer's "+showCards(dealerCards) + " = " + str(dealerScore))
            quit()
        else:
            print("Player busts with " + str(humanScore) + "\nDealer wins")
            quit()



humanScore,dealerScore  = 0,0

humanCardOne = random.choice(deck) #chose player's first card randomly
deck.remove(humanCardOne) #remove that card from deck
humanCardTwo = random.choice(deck) #chose player's second card randomly
deck.remove(humanCardTwo) #remove that card from deck


dealerCardOne = random.choice(deck) #chose player's first card randomly
deck.remove(dealerCardOne) #remove that card from deck
dealerCardTwo = random.choice(deck) #chose player's second card randomly
deck.remove(dealerCardTwo) #remove that card from deck


if humanCardOne=="A" and humanCardTwo == "A":
    humanCardTwo = "A1"
if dealerCardOne=="A" and dealerCardTwo=="A":
    dealerCardTwo= "A1"

humanCards = [humanCardOne,humanCardTwo]
dealerCards = [dealerCardOne,dealerCardTwo]

dealerScore = sumScores(dealerCards)
humanScore = sumScores(humanCards)
print("Dealer has: " + dealerCards[0] + " ? " + "= ?")
print("Player has: " + showCards(humanCards)  +" = " + str(humanScore))

humanWins(humanScore)

while humanScore<21:
    hitOrStand = input("Would you like to (H)it or (S)tand? ")
    if hitOrStand.upper() == "H":
        human_card = optimalAce(humanCards,random.choice(deck))
        humanCards.append(human_card)
        #remove A if optimalAce returns A1
        if (human_card == "A1"):
            deck.remove("A")
        else:
            deck.remove(human_card)
        humanScore = sumScores(humanCards)
        if("A" in humanCards and humanScore>21):
            humanScore -= 10
        print("Player has: " + showCards(humanCards)  + " = " + str(humanScore))
        checkHumanBust(humanScore)
    elif hitOrStand.upper() == "S":
        print("Player stands with: "+showCards(humanCards) + " = " + str(humanScore))
        break

#humanWins(humanScore)
checkHumanBust(humanScore)
print()
print("Dealer has: " + showCards(dealerCards)+ " = " + str(dealerScore))
if(dealerScore>17):
    checkDealerBust(dealerScore,humanScore,humanCards,dealerCards)

while not dealerScore>=17:
    print("Dealer hits")
    dealer_card = optimalAce(dealerCards,random.choice(deck))
    dealerCards.append(dealer_card)
    if(dealer_card == "A1"):
        deck.remove("A")
    else:
        deck.remove(dealer_card)
    dealerScore = sumScores(dealerCards)
    #Do optimal ace check here
    if ("A" in dealerCards and dealerScore > 21):
        dealerScore -= 10
    print("Dealer has: " + showCards(dealerCards) + " = " + str(dealerScore))
    if(dealerScore == 17):
        print("Dealer stands")
    checkDealerBust(dealerScore, humanScore, humanCards, dealerCards)

