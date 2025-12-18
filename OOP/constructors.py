class Student:
    college_name = "ABC University"  # Class variable/Attribute shared by all instances

    # Constructor to initialize the attributes of the Student class
    #self is the instance being created 
    def __init__(self, name, age, grade):
        self.name = name # Instance variable unique to each instance Instance Attribute
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
# Example usage:
student1 = Student("Alice", 20, "A")
print(student1.get_info())  # Output: Name: Alice, Age: 20, Grade: A


student2 = Student("Bob", 22, "B")
print(student2.name) #instance variable only can be accessed using instance object name # Output: Bob


# both are allowed to access class variable
print(Student.college_name)  # Accessing class variable using class name # Output: ABC University
print(student2.college_name)  # Accessing class variable using instance object name # Output