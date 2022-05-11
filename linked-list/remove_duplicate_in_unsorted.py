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

  def print(self):
    current = self.head
    while current:
      print(current.val, end="-")
      current = current.next 

  def remove_duplicates(self):
    pointer1 = self.head
    pointer2 = None
    
    while pointer1 != None and pointer1.next != None:
      pointer2 = pointer1
      while pointer2.next != None:
        if pointer1.val == pointer2.next.val:
          pointer2.next = pointer2.next.next
        else:
          pointer2 = pointer2.next
      pointer1 = pointer1.next
      
llist = LinkedList()

llist.append(5)
llist.append(2)
llist.append(6)
llist.append(4)
llist.append(1)
llist.append(4)
llist.append(4)
llist.append(1)

llist.remove_duplicates()
llist.print()
      
