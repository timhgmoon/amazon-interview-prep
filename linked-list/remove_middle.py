class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList():
  def __init__(self):
    self.head = None

  def append(self, new_val):
    new_node = Node(new_val)
    if self.head == None:
      self.head = new_node
      return
      
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node

  #removes node from around the middle
  #Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
  #the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
  #that node
  def remove_middle(self):
    index = 0
    current = self.head

    while current != None:
      current = current.next
      index += 1

    if index <= 2:
      return
      
    current = self.head
    for i in range(index//2):
      prev = current
      current = current.next
    prev.next = current.next

  def print(self):
    current = self.head
    while current:
      print(current.val, end="-")
      current = current.next 
    print('\n')

      
llist = LinkedList()

llist.append(5)
llist.append(2)
llist.append(6)
llist.append(1)
llist.append(3)
llist.append(10)


llist.print()
llist.remove_middle()
llist.print()
      
