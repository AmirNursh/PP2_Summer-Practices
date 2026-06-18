# Here is an example using different arithmetic operators:

x = 15
y = 4

# Print the result of x + y

print(x + y) # 19

# Print the result of x - y

print(x - y) # 11

# Print the result of x * y

print(x * y) # 60

# Print the result of x / y

print(x / y) # 3.75

# Print the result of x % y

print(x % y) # 3

# Print the result of x ** y

print(x ** y) # 50625

# Print the result of x // y

print(x // y) # 3

# Operators can be used on variables and values:

# =

x = 5 # same as x = 5

# +=	

x += 3	# same as x = x + 3

# -=

x -= 3	# same as x = x - 3

# *=

x *= 3	# same as x = x * 3

# /=	

x /= 3	# same as x = x / 3

# %=

x %= 3	# same as x = x % 3

# **=

x **= 3	# same as x = x ** 3

# //=	

x //= 3	# same as x = x // 3

# &=

x &= 3	# same as x = x & 3

# |=	

x |= 3	# same as x = x | 3

# ^=	

x ^= 3	# same as x = x ^ 3

# >>=	

x >>= 3	# same as x = x >> 3

# <<=	

x <<= 3	# same as x = x << 3


# :=

print(x := 3)	# same as 	x = 3 print(x)


# Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

# The count variable is assigned in the if statement, and given the value 5:

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")



# The Ternary Operator

# The ternary operator allows you to assign one value if a condition is true, and another if it is false:

# Assign a value to x:

# Assign the value "WEEKEND!" if the number is higher than 5, otherwise "Workday":

num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

# Instead of Elif:

# The ternary operator can be used instead of elif in longer if statements:

# Assign:

# - "Fri" if num is 5
# - "Sat" if num is 6
# - "Sun" if num is 7
# - otherwise assign "weekday":

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)


# Comparison Operators

# Comparison operators are used to compare two values:


#==	Equal	
x == y	

#!=	Not equal	
x != y	

#>	Greater than	
x > y

#<	Less than	
x < y	

#>=	Greater than or equal to	
x >= y	

#<=	Less than or equal to	
x <= y	


# Logical Operators

# Logical operators are used to combine conditional statements:

# and 	Returns True if both statements are true	
x < 5 and  x < 10	

# or	Returns True if one of the statements is true	
x < 5 or x < 4	

#not	Reverse the result, returns False if the result is true	
not(x < 5 and x < 10)	


x = 5

print(x > 0 and x < 10) # True

x = 5

print(x < 5 or x > 10) # False

x = 5

print(not(x > 3 and x < 10)) # False


# Identity Operators

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is 	Returns True if both variables are the same object	
x is y	

# is not	Returns True if both variables are not the same object	
x is not y	


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # True, because z is the same object as x
print(x is y) # False, because x and y are different objects, even if they have the same content
print(x == y) # True, because x and y have the same content, even if they are different objects

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y) # True, because x and y are different objects, even if they have the same content

# Membership Operators

# Membership operators are used to test if a sequence is presented in an object:

# in 	Returns True if a sequence with the specified value is present in the object	
x in y	

# not in	Returns True if a sequence with the specified value is not present in the object	
x not in y

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits) # True

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits) # True

# Membership in Strings

# The membership operators also work with strings:

text = "Hello World"

print("H" in text) # True
print("hello" in text) # False
print("z" not in text) # True


# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

# & 	AND	Sets each bit to 1 if both bits are 1	
x & y	

# |	OR	Sets each bit to 1 if one of two bits is 1	
x | y	

# ^	XOR	Sets each bit to 1 if only one of two bits is 1	
x ^ y	

# ~	NOT	Inverts all the bits	
~x	

# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	
x << 2	

# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	
x >> 2


#Example

#The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

print(6 & 3)

#The binary representation of 6 is 0110
#The binary representation of 3 is 0011

#Then the & operator compares the bits and returns 0010, which is 2 in decimal.

#Example

#The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

print(6 | 3)

#The binary representation of 6 is 0110
#The binary representation of 3 is 0011

#Then the | operator compares the bits and returns 0111, which is 7 in decimal.

#Example

#The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

print(6 ^ 3)

#The binary representation of 6 is 0110
#The binary representation of 3 is 0011

#Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.

#Operator Precedence
#Operator precedence describes the order in which operations are performed.

#Example
#Get your own Python Server
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))
#Example
#Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:

print(100 + 5 * 3)
#Precedence Order
#The precedence order is described in the table below, starting with the highest precedence at the top:


()	#Parentheses	
**	#Exponentiation	
+x  -x  ~x	#Unary plus, unary minus, and bitwise NOT	
*  /  //  %	#Multiplication, division, floor division, and modulus	
+  -	#Addition and subtraction	
<<  >>	#Bitwise left and right shifts	
&	#Bitwise AND	
^	#Bitwise XOR	
|	#Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	#Logical NOT	
and	#AND
or	#OR


#Left-to-Right Evaluation
#If two operators have the same precedence, the expression is evaluated from left to right.

#Example
#Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)

# Create variables
a = 15
b = 4

# Print modulus
print(a % b) # 3

# Print floor division
print(a // b)  # 3

# Print power
print(a ** b) # 50625

# Add 10 to a
a += 10
print(a) # 25
