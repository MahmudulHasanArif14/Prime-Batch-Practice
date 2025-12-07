#Python strings are immutable sequences of Unicode characters.
#This means that once a string is created, it cannot be modified.
#Any operation that modifies a string will create a new string instead.
#Here are some examples of string operations in Python:
# Creating a string
s = "Hello, World!"
# Accessing characters
first_char = s[0]  # 'H'
last_char = s[-1]  # '!'
# Slicing strings
substring = s[7:12]  # 'World'
# Concatenation
new_string = s + " How are you?"  # 'Hello, World! How are you?'
# Repetition
repeated_string = s * 3  # 'Hello, World!Hello, World!Hello, World!'
# String methods
upper_s = s.upper()  # 'HELLO, WORLD!'
lower_s = s.lower()  # 'hello, world!'
split_s = s.split(", ")  # ['Hello', 'World!']
# Joining strings
joined_s = " ".join(["Hello", "there"])  # 'Hello there'
# Finding substrings
index_of_world = s.find("World")  # 7
# Replacing substrings
replaced_s = s.replace("World", "Python")  # 'Hello, Python!'
# Checking membership
contains_hello = "Hello" in s  # True


print("First character:", first_char)
print("Last character:", last_char)




#string formating 2 ways format() fun using and f-strings using


 
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 30 years old.
# Using format() method
formatted_string_format = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string_format)  # Output: My name is Alice and I am 30 years old.


#index based string formatting
a=10
b=20
sum=a+b
result="The sum of {1} and {0} is {2}".format(a,b,sum)
print(result)  # Output: The sum of 20 and 10 is 30



#value based string formatting
result_value="The sum of {c} and {d} is {sum}".format(c=8,d=10,sum=8+10)
print(result_value)  # Output: The sum of 8 and 10 is 18
