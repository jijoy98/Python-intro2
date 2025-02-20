#Function Definition:

# A function that calculates the square of a number.

def square(num):
    return num ** 2

# Example usage
print(square(5))  # Output: 25

# A function that checks if a string is a palindrome.

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Compare with its reverse

# Example usage
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("A man a plan a canal Panama"))  # Output: True

#A function that converts a given number of seconds into hours, minutes, and seconds.

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

# Example usage
print(convert_seconds(3661))  # Output: (1, 1, 1)

#Function Call:

#Call the defined function with appropriate arguments.
#Print the result of the function call. 
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

# Function call with example argument
result = convert_seconds(3661)

# Print the result
print(f"{result[0]} hours, {result[1]} minutes, {result[2]} seconds")


