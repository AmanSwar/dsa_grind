"""
Stack
- insert (on the back)
- pop (from the top)
- top()
- size

"""

from typing import List , Any

def stack_insert(array : List , element : Any)-> List:
  array.append(element)
  return array

def stack_pop(array : List)-> List:

  array.pop()
  return array

def stack_top(array : List) -> int:
  return array[-1]

def stack_size(array : List)-> int:
  return len(array)


class Stack:

  def __init__(self):
    self.array : List
    

  def insert(self,x):
    self.array = stack_insert(self.array , x)
    
  def pop(self):
    self.array = stack_pop(self.array)

  def top(self):
    return stack_top(self.array)

  def size(self):
    return stack_size(self.array)
  

  



  