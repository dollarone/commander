from random import Random
import copy

class Deck:

    def __init__(self, name="Unnamed Deck"):
        self.name = name
        self.deck = []

    def __str__(self):
        buffer = "Deck name:\n" + self.name + "\nCards in deck:\n"
        for card in self.deck:
            buffer += str(card) + "\n"
        return buffer

    def addCard(self, card):
        """Add a card to the deck"""
        self.deck.append(card)

    def shuffle(self, rand):
        rand.shuffle(self.deck)

    def size(self):
        """Returns the size of the deck"""
        return len(self.deck)

    def getNextCard(self):
        """Gets the next card in the deck"""
        if self.size() > 0:
            return self.deck.pop()
        else:
            return None



#------------------------------------------------------------------------------

class Card:

    def __init__(self, name="Unnamed Card"):
        self.name = name

    def __str__(self):
        return self.name



#------------------------------------------------------------------------------
def main():
    """..."""
    rand = Random()
    rand.seed() # use currenttime as seed
    deck = Deck("Maarth's Mana Deck")
    deck.addCard(Card("Mean Goblin Rider"))
    deck.addCard(Card("Archer elf"))
    deck.addCard(Card("Fireball wizard"))
    deck.addCard(Card("Grumpy bear"))
    deck.addCard(Card("Skeletonwitch"))
    deck.shuffle(rand)
    deck2 = copy.deepcopy(deck) # take a copy of the deck to use in this game
    print(str(deck))
    print(str(deck2))
    card = deck.getNextCard()
    while(card is not None):
        print("Next card: " + str(card))
        card = deck.getNextCard()
    print(str(deck))
    print(str(deck2))

if __name__ == '__main__':
    main()
