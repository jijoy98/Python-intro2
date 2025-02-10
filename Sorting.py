#using Sorted()
j= [9,8,4,1,2,3]
print (sorted(j))
print(j)

# Sorting using (=)
words = ["Apple", "Orange", "Banana", "Grapes", "Kiwi"]
sorted_words = sorted(words, key=len)
print(sorted_words)

#Sorting in Reverse order
alph = ["m", "n", "b", "v", "c", "x", "z", "a", "s", "d", "f", "g", "h", "j", "k", "l"]
sorted_alph = sorted(alph, reverse=True)
print(sorted_alph)
