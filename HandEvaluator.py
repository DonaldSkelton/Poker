from pokerdeck import *
from random import choice, shuffle
from collections import Counter


def dealHand(deck:PokerDeck,size:int)->list:  #deal a hand of cards with "size" cards in it from "deck". returned as a list.
    hand=[]
    for n in range(size):
        card=choice(deck)
        hand+=[card]
        deck.remove(card)
    return hand


def evaluateHand(hand:list):             #"hand" should be a list containing 5 named-tuple "cards". returns the best poker hand (i.e. "4 of a kind")
    ranks=[]
    suits=[]
    ranks,suits=zip(*hand)                #unpack the hand into seperate lists of ranks and suits
    if suits.count(suits[0]) == 5:        #If all 5 suits are the same
        flush=True                        #you have a flush
    else:                                 #otherwise
        flush=False                       #you don't have a flush
    ranks=list(ranks)                     #unpacking turned my list into a tuple, so turn it back into a list.
    for i in range(len(ranks)):           #Convert named card ranks into integers
        if ranks[i] == 'J':
            ranks[i]=11
        elif ranks[i] == 'Q':
            ranks[i]=12
        elif ranks[i] == 'K':
            ranks[i]=13
        elif ranks[i] == 'A':
            ranks[i]=14
        else:
            ranks[i]=int(ranks[i])
    ranks.sort()                         #Put the cards in order
    if (ranks[4] == (ranks[0]+4)
        and ranks[3] == (ranks[0]+3) 
        and ranks[2] == (ranks[0]+2) 
        and ranks[1] == (ranks[0]+1)):       #If all of the cards are sequential
        straight=True                    #you have a straight.
    else:                                #Otherwise,
        straight=False                   #you don't have a straight.
    cardCount=Counter()                  #Inintialize a counter to count the ranks(check for pairs)
    for i in range(len(ranks)):          #For each card
        cardCount[ranks[i]]+=1           #increment the count for that rank.
    cardCount=cardCount.most_common()    #Convert the counts to a list sorted by most common
    if cardCount[0][1] == 4:             #If you have 4 of the same card
        bestHand='4 of a kind'           #that's 4 of a kind.
    elif cardCount[0][1] == 3:           #If you have three of one card
        if cardCount[1][1] == 2:         #and 2 of the next most common
            bestHand='Full House'        #that's a full house.
        else:
            bestHand='3 of a kind'       #If you don't have 2 of the next most common, that's just 3 of a kind.
    elif cardCount[0][1] == 2:           #If you have 2 of one card
        if cardCount[1][1] == 2:         #and 2 of the next most common card
            bestHand='2 Pair'            #that's 2 pair
        else:
            bestHand='1 Pair'            #otherwise it's just 1 pair
    else:
        bestHand='High Card'             #if you only have 1 of your most common card, it's just a high card
    if flush:                            #if you have a flush        
        bestHand='Flush'                 #your best hand is a flush(check for straight/royal flush in a second)
    if straight:                         #if you have a straight
        if flush:                        #and a flush
            if ranks[4] == 14:           #and your highest card is an ace
                bestHand='Royal Flush'   #you have a royal flush
            else:
                bestHand='Straight Flush'#if not ace high, you still got a straight flush
        else:
            bestHand='Straight'          #if not a flush at all you still got a straight


    #print('Flush status: '+str(flush))
    #print('Ranks as ints: '+str(ranks))
    #print('Straight status: '+str(straight))
    #print('Counted ranks: '+str(cardCount))   #printing debug info

    #print('The best hand you can call here is:  '+bestHand)
    return bestHand

def main():                                  # pragma: no cover
    deck = PokerDeck()                       #Generate a deck of cards
    shuffle(deck)                            #Shuffle the deck
    myHand=dealHand(deck,5)                  #Deal a hand of 5 cards
    print('Hand dealt: ')
    print(myHand)                            #Display the hand that was dealt
    best=evaluateHand(myHand)                     #Evaluate the hand and print the best hand to call in a game of poker
    print('The best hand you can call here is:  '+best)

    #Do the same thing with a rigged royal flush, instead of a hand dealt from a shuffled deck.
    print('\n\nroyal flush test (rigged hand)')
    myHand=[Card(rank='10', suit='♠'), Card(rank='J', suit='♠'), 
            Card(rank='Q', suit='♠'), Card(rank='K', suit='♠'), Card(rank='A', suit='♠')]
    print('Hand dealt: ')
    print(myHand)  
    best=evaluateHand(myHand)
    print('The best hand you can call here is:  '+best)

if __name__=='__main__': # pragma: no cover
    main()
