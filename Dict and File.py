#Creating a Dict
student = {  
    "Name": "Jijoy",  
    "age": 35,  
    "grade": "A+"
}

print(student["Name"]) 

# Dict Formatting
k = {}
k['word'] = 'mango'
k['count'] = 42

J = 'I want %(count)d copies of %(word)s' % k  
print(J)

J = 'I want {count:d} copies of {word}'.format(**k)
print(J)

#vDel
var = 6
del var  

list = ['a', 'b', 'c', 'd']
del list[0]    
del list[-2:]   
print(list)      

dict = {'a':1, 'b':2, 'c':3}
del dict['b']  
print(dict)    