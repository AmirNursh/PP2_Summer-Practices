# Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

# Example
# One-line if/else that prints a value:

a = 2
b = 330
print("A") if a > b else print("B") # prints "B" because a is not greater than b


# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:

# Example
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger) # prints "Bigger is 20" because a is not greater than b


# Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable:

# Example
# One line, three outcomes:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") # prints "=" because a is equal to b


# Practical Examples
# Ternary operators are particularly useful for simple assignments and return statements.

# Example
# Finding the maximum of two numbers:

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value) # prints "Maximum value: 20" because y is greater than x


# Example
# Setting a default value:

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name) # prints "Welcome, Guest" because username is an empty string
