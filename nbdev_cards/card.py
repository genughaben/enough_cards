# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_card.ipynb 3
from fastcore.utils import *

# %% ../nbs/00_card.ipynb 4
suits = ["♣️","♠️","❤️","♦️"]
ranks = [None, None] + [str(x) for x in range(2,11)] + ["J", "Q", "K", "A"]

# %% ../nbs/00_card.ipynb 13
class Card: 
    'A playing card'
    def __init__(self, 
                 suit:int,  # An index into `suits` 
                 rank:int): # An index into `ranks`
        self.suit, self.rank = suit, rank
    def __str__(self): return f"{suits[self.suit]}{ranks[self.rank]}"
    __repr__ = __str__
    

# %% ../nbs/00_card.ipynb 20
@patch
def __eq__(self: Card, other:Card): return (self.suit, self.rank)==(other.suit, other.rank)

# %% ../nbs/00_card.ipynb 22
Card(suit=1, rank=1) == Card(suit=1, rank=1)

# %% ../nbs/00_card.ipynb 23
Card(suit=1, rank=1) == Card(suit=2, rank=1)

# %% ../nbs/00_card.ipynb 25
@patch
def __lt__(self: Card, other:Card): return self.rank < other.rank

# %% ../nbs/00_card.ipynb 26
# Example
Card(suit=1, rank=1) < Card(suit=2, rank=2)

# %% ../nbs/00_card.ipynb 28
Card(suit=1, rank=1) > Card(suit=2, rank=1)

# %% ../nbs/00_card.ipynb 30
@patch
def __gt__(self: Card, other:Card): return self.rank > other.rank

