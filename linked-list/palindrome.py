class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList():
  def __init__(self):
    self.head = None

  def append(self, new_node):
    if self.head == None:
      self.head = Node(new_node)
      return

    current = self.head
    while current.next != None:
      current = current.next

    current.next = Node(new_node)

  def print(self):
    current = self.head
    while current:
      print(current.val, end="-")
      current = current.next
    print('\n')

  def isPalindrome(self):
    current = self.head
    stack = []

    while current:
      stack.append(current.val)
      current = current.next

    while self.head:
      if self.head.val != stack.pop():
        return False
      self.head = self.head.next
    return True
llist = LinkedList()
llist.append("a")
llist.append("p")
llist.append("p")
llist.append("l")
llist.append("e")
llist.print()
print(llist.isPalindrome())

llist2 = LinkedList()
llist2.append("a")
llist2.append("p")
llist2.append("p")
llist2.append("l")
llist2.append("p")
llist2.append("p")
llist2.append("a")
llist2.print()
print(llist2.isPalindrome())
