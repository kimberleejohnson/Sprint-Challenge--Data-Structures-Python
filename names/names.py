## Original runtime complexity: 
# Big O(n^2), because...
# I see a for loop within a for loop! Which immediately clues me into the fact that this code is inefficient. Then, as I learned when I got this wrong on the Sprint Challenge last week, I should look at what each iteration in the for loop is actually doing. The first for loop checks every name in name_1, so the speed of that depends on n, the number of names in the list. The next for loop also checks for every name in names_2, so depends on the number of names in the list, also n. So, we have n*n complexity, or n^2. 

# Importing time library to track time 
import time
# Import binary tree structure
from binary_search_tree_names import BinarySearchTree

# Starting time tracker 
start_time = time.time()

# Reading the names file 
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# Reading names file 
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Create a binary search tree, initialized with first value in names_1
name_check_tree = BinarySearchTree(names_1[0])
# Create empty duplicates data structure 
duplicates = []
# Run through every item in names_1 after initialized value, adding to tree 
for name in names_1[1:]: 
    name_check_tree.insert(name)
# Call the contains method on tree, checking if tree contains name_2 in names_2 
for name in names_2: 
    if name_check_tree.search(name): 
        # If it does, then we will append to duplicates array
        duplicates.append(name)


# Ending time tracker 
end_time = time.time()

# Print statements 
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

## Original code 
#Empty duplicates data structure 
#duplicates = []
# For every name in first list 
#for name_1 in names_1:
    # And also every name in second list 
    #for name_2 in names_2:
        # If the name in the first list is the one we're iterating over in the second list 
        #if name_1 == name_2:
            # Add it to the empty duplicates data structure 
            #duplicates.append(name_1)