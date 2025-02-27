class Student:
    school = "Shiz University"
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_info(self):
        return f"{self.name} is {self.age} in grade {self.grade} at {self.school}"
    
student1 = Student("Alice", 22, "senior")
student2 = Student("Mathew", 20, "junior")
student3 = Student("Grace", 18, "sophomore")
student4 = Student("Adam", 16, "freshman")
    
print(student1.get_info())
print(student2.get_info())
print(student3.get_info())
print(student4.get_info())
