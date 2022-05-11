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

  def get_nth_from_last(self, n):
    index = -1
    current = self.head

    while current != None:
      current = current.next
      index += 1

    current = self.head
    for i in range(index - n):
      current = current.next
    return current.val
      
      
llist = LinkedList()

llist.append(5)
llist.append(2)
llist.append(6)
llist.append(4)
llist.append(1)
llist.append(4)
llist.append(5)
llist.append(1)

print(llist.get_nth_from_last(0))
print(llist.get_nth_from_last(1))
print(llist.get_nth_from_last(2))
llist.print()
      
