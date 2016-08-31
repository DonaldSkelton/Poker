import unittest
from pokerdeck import *
from HandEvaluator import evaluateHand, dealHand


class TestHandEval(unittest.TestCase):
    def testDealHand(self):
        deck = PokerDeck()
        myHand = dealHand(deck, 5)
        self.assertEqual(5, len(myHand))
        self.assertEqual(47, len(deck))
    def testHighCard(self):
        myHand=[Card(rank='10', suit='♠'),Card(rank='8', suit='♠'),
        Card(rank='3', suit='♠'),Card(rank='J', suit='♠'),Card(rank='5', suit='♦')]
        self.assertEqual(evaluateHand(myHand),'High Card')
        
    def test1Pair(self):
        myHand=[Card(rank='10', suit='♠'),Card(rank='8', suit='♠'),
        Card(rank='3', suit='♠'),Card(rank='J', suit='♠'),Card(rank='10', suit='♦')]
        self.assertEqual(evaluateHand(myHand),'1 Pair')
        
    def test2Pair(self):
        myHand=[Card(rank='10', suit='♠'),Card(rank='8', suit='♠'),
        Card(rank='3', suit='♠'),Card(rank='8', suit='♦'),Card(rank='10', suit='♦')]
        self.assertEqual(evaluateHand(myHand),'2 Pair')
        
    def test3ofakind(self):
        myHand=[Card(rank='10', suit='♠'),Card(rank='8', suit='♠'),
        Card(rank='3', suit='♠'),Card(rank='10', suit='♣'),Card(rank='10', suit='♦')]
        self.assertEqual(evaluateHand(myHand),'3 of a kind')        
        
    def testStraight(self):
        myHand=[Card(rank='10', suit='♠'),Card(rank='8', suit='♠'),
        Card(rank='7', suit='♠'),Card(rank='9', suit='♣'),Card(rank='J', suit='♦')]
        self.assertEqual(evaluateHand(myHand),'Straight')    
        
    def testFlush(self):
        myHand=[Card(rank='10', suit='♠'),Card(rank='8', suit='♠'),
        Card(rank='3', suit='♠'),Card(rank='2', suit='♠'),Card(rank='K', suit='♠')]
        self.assertEqual(evaluateHand(myHand),'Flush')         
        
    def testFullHouse(self):
        myHand=[Card(rank='10', suit='♠'),Card(rank='8', suit='♠'),
        Card(rank='8', suit='♣'),Card(rank='10', suit='♣'),Card(rank='10', suit='♦')]
        self.assertEqual(evaluateHand(myHand),'Full House')        
        
    def test4ofakind(self):
        myHand=[Card(rank='10', suit='♠'),Card(rank='8', suit='♠'),
        Card(rank='10', suit='♥'),Card(rank='10', suit='♣'),Card(rank='10', suit='♦')]
        self.assertEqual(evaluateHand(myHand),'4 of a kind')      
        
    def testStraightFlush(self):
        myHand=[Card(rank='10', suit='♠'),Card(rank='8', suit='♠'),
        Card(rank='7', suit='♠'),Card(rank='9', suit='♠'),Card(rank='J', suit='♠')]
        self.assertEqual(evaluateHand(myHand),'Straight Flush')   
        
    def testRoyalFlush(self):
        myHand=[Card(rank='10', suit='♠'), Card(rank='J', suit='♠'), 
        Card(rank='Q', suit='♠'), Card(rank='K', suit='♠'), Card(rank='A', suit='♠')]  
        self.assertEqual(evaluateHand(myHand),'Royal Flush')
        
        
if __name__=='__main__':
    unittest.main()
        
