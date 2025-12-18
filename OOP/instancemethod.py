class Laptop:
    storage_type = "SSD"  # Class variable/attribute shared by all instances

    def __init__(self, brand, model, ram_size):
        self.brand = brand          # Instance variable/attribute unique to each instance
        self.model = model          # Instance variable/attribute unique to each instance
        self.ram_size = ram_size    # Instance variable/attribute unique to each instance

    def display_specs(self):
        """Instance method to display the specifications of the laptop."""
        specs = (f"Brand: {self.brand}, Model: {self.model}, "
                 f"RAM Size: {self.ram_size}GB, Storage Type: {self.storage_type}")#instance method accessing both instance and class variables
        print(Laptop.storage_type);#instance method accessing class variable
        return specs    
    


l1 = Laptop("Dell", "XPS 13", 16)
l2 = Laptop("Apple", "MacBook Pro", 32)
print(l1.display_specs())  # Output: "Brand: Dell, Model: XPS 13, RAM Size: 16GB, Storage Type: SSD"
print(l2.display_specs())  # Output: "Brand: Apple, Model: MacBook Pro, RAM Size: 32GB, Storage Type: SSD"        return specs 