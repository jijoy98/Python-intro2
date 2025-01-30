def checkdays():
    days =("Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
    print (days[0], days[6])
    if "Wed" in days:
        print ("Wed is a day of of the week. ")
    else:
        print("Wed i not in the list of days. ")
checkdays()

def sorting():
    numbers = (2,1,3)
    numberlist= list(numbers)
    numberlist.sort()
    numbers = tuple (numberlist)
    print (numbers)
    
sorting()