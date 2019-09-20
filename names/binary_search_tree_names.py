## How and why can a binary search tree help me? 
# A tree starts with a node, which splits into right side (greater than), and left side (less than).
# Each of those subsequent nodes can have an additional two children, keeping the R and L structure. 
# Binary search tree cuts the number of things we're searching through in half each time, since you move either right or left. 

class BinarySearchTree: 
    def __init__(self, value): 
        self.value = value 
        self.right = None
        self.left = None 
    
    # Method to add values, which we'll use for duplicates data structure 
    def insert(self, item): 
        
        # Right side 
        if self.value < item: 
            # If you can't move to the right any more, you're done, insert the item 
            if self.right is None: 
                self.right = BinarySearchTree(item)
            # Item to insert is greater than current, so keep moving to right, recursively call function 
            else: 
                self.right = insert(item)

        # Left side 
        else: 
            # If you can't move to the left any more, you're done, insert the item 
            if self.left is None: 
                self.left = BinarySearchTree(item)
            # Item to insert is less than the current, so keep moving to left 
            else: 
                self.left = insert(item)

    # Method to search, which we'll use to search through names 