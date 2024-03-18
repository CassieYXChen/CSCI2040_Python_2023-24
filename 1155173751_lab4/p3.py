class Node(object):
  def __init__(self, v, n):
    self.value = v
    self.next = n
    
class LinkedList(object):
  def __init__(self):
    self.firstLink = None
  def add(self, value):
    # add will insert at the begining of the list
    self.firstLink = Node(value, self.firstLink)

  
  def test(self, value):
    x = self.firstLink
    while x is not None:
      if x.value == value:
        return True
      else:
        x = x.next
    return False

  
  def remove(self, value):
    target = self.firstLink
    prev = None
    while target is not None:
      #target.next: succ
      if target.value == value:
        if prev is None:
          self.firstLink = target.next
        else:
          #prev -> succ
          prev.next = target.next
        return True
      else:
        prev = target
        target = target.next
    return False

  
  def len(self): # return size of linked list
    size = 0
    x = self.firstLink
    while x is not None:
      size += 1
      x = x.next
    return size

  
  def Lprint(self):
    x = self.firstLink
    linked_list = "Current linked list: "

    while x is not None:
        linked_list += str(x.value)
        if x.next is not None:
          linked_list += "-->"
        x = x.next

    linked_list += "-->none"
    print(linked_list)
    return 0
