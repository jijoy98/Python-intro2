# Find and print the union of the two sets.  
set1 = {1,3,6,7,9}
set2 = {2,4,5,6,8}
union_set = set1|set2
print (union_set)

# Find and print the intersection of the two sets
set1 = {1,3,6,7,9}
set2 = {2,4,5,6,8}
intersection_set = set1 & set2
print(intersection_set)

# Find and print the difference between the two sets.
set1 = {1,3,6,7,9}
set2 = {2,4,5,6,8}
difference_set = set1.difference(set2)
print(difference_set)

# Add a new word to the set.
set1 = {1,3,6,7,9}
set2 = {2,4,5,6,8}
set1.add(4)
print("After adding:", set1)

# Remove a word from the set.
set1 = {1,3,6,7,9}
set2 = {2,4,5,6,8}
set2.remove(4)
print("After removing:", set2)