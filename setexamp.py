# Set is changeable. Items inside must not be changeable.
myset = {"apple", "banana", "cherry"}
print(myset)
myset.add("orange")  # Adding an item
print(myset)
myset.remove("banana")  # Removing an item
print(myset)
# Demonstrating that sets do not allow duplicate items
myset.add("apple")  # Trying to add a duplicate item
print(myset)  # "apple" will not be added again
# Demonstrating that sets do not maintain order
another_set = {"cherry", "banana", "apple"}
print(another_set)  # The order of items may differ from myset

"""A set can change, but its items cannot change.
Think like this:

The set is a bag → you can put things in or take things out. (mutable)

But the things you put inside the bag must be solid stones, not soft clay.
Because if the items can change shape, the bag won’t recognize them anymore.

In Python:

Set = changeable (add/remove items)

Items inside set = must NOT be changeable (must be fixed)

✔ Allowed items (cannot change)

numbers → 1, 2.5
string → "hello"
tuple → (1, 2, 3)

❌ Not allowed (can change)

list → [1, 2, 3]
dict → {"a": 1}
another set → {1, 2}
"""