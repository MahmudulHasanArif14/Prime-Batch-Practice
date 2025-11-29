#function structure for without default parameters
#def function_name(parameters): 
    #function body

# Example without default parameters
def add(a, b):
    return a + b
print(add(3, 5))  # Output: 8



# Example with default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, Guest!



#function structure for with default parameters
#def function_name(nondefault_parameters,parameters=default_value): 
    #function body
#Note:
# =>here nondefault_parameters are the parameters which do not have default values and parameters with default values are called default parameters nondefault_parameters should always come first 



#Example with both default and nondefault parameters
def introduce(name, age=18):
    print(f"My name is {name} and I am {age} years old.")

    
introduce("Bob", 25)  # Output: My name is Bob and I am 25 years old.
introduce("Charlie")   # Output: My name is Charlie and I am 18 years old.