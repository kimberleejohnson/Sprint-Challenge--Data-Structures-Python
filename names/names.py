## Original runtime complexity: 
# Big O(n^2), because...
# I see a for loop within a for loop! Which immediately clues me into the fact that this code is inefficient. Then, as I learned when I got this wrong on the Sprint Challenge last week, I should look at what each iteration in the for loop is actually doing. The first for loop checks every name in name_1, so the speed of that depends on n, the number of names in the list. The next for loop also checks for every name in names_2, so depends on the number of names in the list, also n. So, we have n*n complexity, or n^2. 

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

