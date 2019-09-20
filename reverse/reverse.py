## What do I know about linked lists? 
# Useful data structure if will be adding or deleting things a lot
# Terrible at finding specific items
# BaseCS analogy: like if we're putting things in boxes in a house, vs. in drawers all next to each other 
# Each item points to the next value, but NOT the past value...that would be a doubly linked list 
# Tail points to none 
# Per before hours, I should think about *pointing*, not about *moving* 
# This means I can probably think about changing pointers in reverse, like: 
  # 1 -> 2 -> 3 -> 4 becomes just 1 <- 2 <- 3 <-4  

class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  # 1 -> 2 -> 3 -> 4 becomes just 1 <- 2 <- 3 <-4  
  def reverse_list(self):
    # Variable to store previous node 
    prev_node = None
    # Start at the head 
    current_node = self.head 
    
    # While the current node is not None 
    # Until we iterate through the whole list 
    while current_node is not None: 
      # Store a variable for what the current node _used_ to point to 
      temp_next = current_node.next_node 
      # Reset the current_node.next to point to the previous node 
      current_node.next_node = prev_node 
      # Set the previous node to the current_node 
      prev_node = current_node
      # Reset the current_node to the next node in the list that was stored as a temp variable
      current_node = temp_next 
    # When you're done with the list, reset the head 
    self.head = prev_node 
    
