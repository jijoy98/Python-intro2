class Animal:
    def __init__(self, name):  # Fixed typo here, changed _inti_ to __init__
        self.name = name
        
    def speak(self):
        pass

class Unicorn(Animal):
    def speak(self):
        return f"{self.name} says: Neigh!"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Lion(Animal):
    def speak(self):
        return f"{self.name} says Roaring!"

class Tiger(Animal):
    def speak(self):
        return f"{self.name} says Growling!"

class Dragon(Animal):  # Fixed typo here, changed Dragron to Dragon
    def speak(self):
        return f"{self.name} says Hisses!"
        
u = Unicorn("Sparkle")
d = Dog("Buddy")
l = Lion("Simba")
t = Tiger("Sher Khan")
dragon = Dragon("Fury")

print(u.speak())
print(d.speak())
print(l.speak())
print(t.speak())
print(dragon.speak())
