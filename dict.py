studentData = {
    "age": 20,
    '1001': {'name': 'Alice', 'age': 20, 'major': 'Computer Science'},
    '1002': {'name': 'Bob', 'age': 22, 'major': 'Mathematics'},
    '1003': {'name': 'Charlie', 'age': 21, 'major': 'Physics'},
    '1004': {'name': 'David', 'age': 23, 'major': 'Chemistry'},
}

# Function to get student details by ID
std_Name=studentData['age'] #sometime this can cause error cause if the key is not present it will throw key error
print(std_Name)
# to avoid that we can use get method
std_Age=studentData.get("f")
print(std_Age)  # This will print None if the key "f" is not found