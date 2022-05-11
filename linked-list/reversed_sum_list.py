"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7- > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912. 
"""


class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList():
  def __init__(self):
    self.head = None
    self.reversed = []

  def append(self, new_val):
    new_node = Node(new_val)
    if self.head == None:
      self.head = new_node
      return
      
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  def print(self):
    current = self.head
    while current:
      print(current.val, end="-")
      current = current.next 

  def get_reversed_sum(self):
    sum = 0
    multiplier = 1
    current = self.head
    while(current != None):
      sum += current.val * multiplier
      multiplier *= 10
      current = current.next
    return sum


llist = LinkedList()
llist2 = LinkedList()

llist.append(7)
llist.append(1)
llist.append(6)

llist2.append(5)
llist2.append(9)
llist2.append(2)

first_reversed = llist.get_reversed_sum()
second_reversed = llist2.get_reversed_sum()
reversed_total = first_reversed + second_reversed

ans_llist = LinkedList()
while reversed_total > 0:
  ans_llist.append(reversed_total % 10)
  reversed_total //= 10

ans_llist.print()

      



      

