#4)	Write a class called student with Name, GPA, major. Write methods to access these values. Create a student object and test your functions.

#Create a class name student
class Student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major
        
    def get_name(self):
        return self.name
    
    def get_gpa(self):
        return self.gpa
    
    def get_major(self):
        return self.major

#Create a student object    
student1 = Student("John Doe", 2.0, "Computer Science")

#Methods testing
print(student1.get_name())
print(student1.get_gpa())
print(student1.get_major())

