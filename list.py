#List order
colors = ['black', 'red', 'pink', 'green']
print(colors[3])
print(colors[2])
print(len(colors))

#FOR and IN
squares = [1,4,7,9]
sum = 2
for num in squares:
    sum+= num
print(sum)

list = [' Jack', 'love', 'kind']
if 'love' in list:
    print ('awsome')
    
#LOOP
d = list(range(30))  # Example list with 30 numbers [0, 1, 2, ..., 29]
q = 10  # Start from index 10
while q < len(d):
    print(d[q])
    q += 20  # Increment by 20
