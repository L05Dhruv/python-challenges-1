# Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
# The function should return a list containing all values of the nodes in the linked list.

# Do not edit the following 'Node' class
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None



def linked_list_values(head):
  pass # todo






# Test Case

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]