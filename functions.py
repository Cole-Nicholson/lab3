from typing import * 
from dataclasses import dataclass
import unittest
import math
import sys
sys.setrecursionlimit(10**6)

LinkedList: TypeAlias = Optional['LLNode']

@dataclass(frozen=True)
class LLNode:
    value: int
    rest: LinkedList

def range(max_exclusive: int) -> LinkedList:
    pass

def occurs(ll:LinkedList, num: int) -> bool:
    pass

def has_dup(ll:LinkedList) -> int:
    pass

def insertion_sort(ll:LinkedList) -> LinkedList:
    pass

class Tests(unittest.TestCase):
    pass

if(__name__== '__main__'):
    unittest.main()