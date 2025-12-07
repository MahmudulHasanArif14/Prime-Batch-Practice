userInput=input("Enter a string to check if it's a palindrome: ")


def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    # s[::-1] gives the reversed string
    # Return True if palindrome, else False
    # A palindrome reads the same forwards and backwards
    return s == s[::-1]


if is_palindrome(userInput):
    print(f'"{userInput}" is a palindrome.')
else:
    print(f'"{userInput}" is not a palindrome.')