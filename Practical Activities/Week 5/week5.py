from collections import Counter, defaultdict
from functools import lru_cache

"""
Write a version of this function that uses set operations instead of a for loop.
"""

def uses_none_set(word, forbidden):
    return set(word.lower()).isdisjoint(set(forbidden.lower()))


"""
Write a function that takes a string of letters and a word, and checks whether the letters
can spell the word, taking into account how many times each letter appears.
"""

def can_spell_word(tiles, word):
    tile_count = Counter(tiles.upper())
    word_count = Counter(word.upper())
    return all(tile_count[letter] >= word_count[letter] for letter in word_count)


"""
Write a simplified version of this function using a defaultdict.
"""

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class PokerHand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def partition(self):
        suit_hands = defaultdict(PokerHand)
        for card in self.cards:
            suit_hands[card.suit].add_card(card)
        return list(suit_hands.values())


"""
Write a version of fibonacci with a single return statement using nested conditional expressions.
"""

def fibonacci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)


"""
Rewrite the body of the binomial_coeff function using nested conditional expressions.
"""

def binomial_coeff(n, k):
    return 1 if k == 0 else 0 if n == 0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)


"""
Make binomial_coeff more efficient by memoizing it.
"""

@lru_cache(maxsize=None)
def binomial_coeff_memo(n, k):
    return 1 if k == 0 else 0 if n == 0 else binomial_coeff_memo(n-1, k) + binomial_coeff_memo(n-1, k-1)


"""
Write a more concise version of Deck.__str__ using a list comprehension or generator expression.
"""

class Deck:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return '\n'.join(str(card) for card in self.cards)

    def add_card(self, card):
        self.cards.append(card)

# Testing functions

if __name__ == "__main__":
    print("Test uses_none_set:")
    print(uses_none_set("hello", "xyz"))  # True
    print(uses_none_set("hello", "e"))    # False

    print("\nTest can_spell_word:")
    print(can_spell_word("TABLE", "BELT"))  # True
    print(can_spell_word("TABLE", "BEET"))  # False

    print("\nTest fibonacci with single return:")
    print([fibonacci(n) for n in range(10)])  # 0 1 1 2 3 5 8 13 21 34

    print("\nTest binomial_coeff with nested conditionals:")
    print(binomial_coeff(10, 4))  # 210

    print("\nTest binomial_coeff with memoization:")
    print(binomial_coeff_memo(20, 10))  # 184756

    print("\nTest Deck __str__ with generator expression:")
    deck = Deck()
    deck.add_card(Card("Ace", "Spades"))
    deck.add_card(Card("10", "Hearts"))
    print(deck)

    print("\nTest PokerHand partition with defaultdict:")
    hand = PokerHand()
    hand.add_card(Card("2", "Hearts"))
    hand.add_card(Card("3", "Hearts"))
    hand.add_card(Card("4", "Clubs"))
    hand.add_card(Card("5", "Clubs"))
    hand.add_card(Card("6", "Spades"))
    suits = hand.partition()
    for i, suit_hand in enumerate(suits):
        print(f"\nSuit {i+1}:")
        for card in suit_hand.cards:
            print(card)