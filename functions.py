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

#return a linked list of numbers from 0 to a max num
def range(max_exclusive: int) -> LinkedList:
    #helper to build range
    def helper(current: int) -> LinkedList:
        if current == max_exclusive:
            return None
        return LLNode(current, helper(current + 1))
    return helper(0)

#returns true if a number is in linked list
def occurs(ll:LinkedList, num: int) -> bool:
    match ll:
        case None:
            return False
        case LLNode(value, rest):
            if num == value:
                return True
            return occurs(rest, num)
        
#Check linked list for duplicates
def has_dup(ll:LinkedList) -> bool:
    match ll:
        case None:
            return False
        case LLNode(value,rest):
            if occurs(rest, value):
                return True
            return has_dup(rest)
    
#helper to insert number
def insertion_helper(ll:LinkedList, num: int) -> LinkedList:
    if ll == None:
        return LLNode(num, None)
    else:
        if num <= ll.value:
            new_ll: LinkedList = LLNode(num, ll)
        else:
            rest_of_ll: LinkedList = ll.rest
            new_ll = LLNode(ll.value, insertion_helper(rest_of_ll,num))
    return new_ll

#sort numbers in linked list      
def insertion_sort(ll: LinkedList) -> LinkedList:
    if ll == None:
        return None
    else:
        return insertion_helper(insertion_sort(ll.rest), ll.value)
linked1 = LLNode( 10, LLNode(11, LLNode(12, LLNode(13, None))))
class Tests(unittest.TestCase):
    def test_range(self):
        self.assertEqual(range(4), LLNode(0,LLNode(1,LLNode(2,LLNode(3,None)))))
        self.assertEqual(range(0), None)
        self.assertEqual(range(1), LLNode(0,None))
        self.assertEqual(range(7), LLNode(0,LLNode(1,LLNode(2,LLNode(3,LLNode(4, LLNode(5, LLNode(6, None))))))))

    def test_occurs(self):
        self.assertEqual(occurs(linked1, 10), True)
        self.assertEqual(occurs(linked1, 9), False)
        self.assertEqual(occurs(linked1, 13), True)

    def test_has_dup(self):
        dup_ll = LLNode(1, LLNode(2, LLNode(5, LLNode(3, LLNode(4, LLNode(2, LLNode(5, None)))))))
        self.assertEqual(has_dup(dup_ll), True)

    def test_insertion_sort(self):
        test_ll = LLNode(1, LLNode(2, LLNode(5, LLNode(3, LLNode(4, LLNode(2, LLNode(5, None)))))))
        self.assertEqual(insertion_sort(test_ll), LLNode(1, LLNode(2, LLNode(2, LLNode(3, LLNode(4, LLNode(5, LLNode(5, None))))))))


if(__name__== '__main__'):
    unittest.main()