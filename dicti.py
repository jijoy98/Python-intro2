dicti ={'Matt': 20, 'Sally': 30, 'Billy': 20, 'Ben': 80
        
def add(key, value):
        dicti[key] = value
def remove(name):
    del dicti[name]
def average(dicti):
    print(sum(dicti.values()) / len(dicti)
def Hight(dicti):
    print(max(dicti, key =dicti.get))
def score80(dicti):
    above = [name for name, score in dicti.items() if score >80]
     print(above)
              
print(dicti)
add('Bill', 45)
print(dicti)
remove('Matt')
print(dicti)
average(dicti)

dict2= {'Bill': 85, 'John' :100, 'Gabe' : 80, 'Jack' : 0
highest(dict2)
score80(dict2)