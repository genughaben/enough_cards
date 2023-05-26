# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../nbs/01_deck.ipynb 2
import random
from .card import *
from fastcore.utils import *

# %% ../nbs/01_deck.ipynb 4
class Deck:
    'A deck of 52 cards'
    def __init__(self):
        self.cards = [Card(s, r) for s in range(4) for r in range(2,15)]
    def __len__(self):
        return len(self.cards)
    def __str__(self):
        return "; ".join(map(str, self.cards))
    def __contains__(self, other: Card):
        return other in self.cards
    __repr__ = __str__
    
    def shuffle(self):
        "Randomizes card order in deck"
        random.shuffle(self.cards)

# %% ../nbs/01_deck.ipynb 14
@patch
def pop(self: Deck,
        idx:int=-1): # The index of the card to remove, defaulting to the last one
        "Remove one card from the deck"
        return self.cards.pop(idx)

# %% ../nbs/01_deck.ipynb 19
@patch
def remove(
    self: Deck, 
    card: Card): # Card to remove
    self.cards.remove(card)

# %% ../nbs/01_deck.ipynb 22
@patch
def draw(self: Deck,
        n:int=1, # Number of cards to be drawn
        replace:bool=True): # When true: drawn with replace, if false: not.
    deck.shuffle()
    if replace:
        return [random.choice(self.cards) for i in range(n)]
    else:
        return self.cards[:n]
