# When the ring buffer is full, but we need to add a new element...
# The oldest element in the ring buffer is overwritten with the newest element. 
# This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.
# FIFO: First item added will be the first item removed when needed 

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  # Adds elements to the buffer 
  def append(self, item):
    # Check if capacity has been hit 
      # Probably check by seeing if current is pointing to capacity 
    if self.current == self.capacity: 
      # Add the item to the beginning of the list[0]
      self.storage[0] = item 
      # Reset self.current to 1 
      self.current = 1
    
    # If capacity has not been hit 
    else: 
      # Set the spot at the current index to the item 
      self.storage[self.current] = item
      # Increment the current place along by 1
      self.current += 1 

  # Returns all elements in their given order, but should not return None values 
  def get(self):
    # List keyword, built-in filter, anonymous lambda function 
    return list(filter(lambda item: item is not None, self.storage))