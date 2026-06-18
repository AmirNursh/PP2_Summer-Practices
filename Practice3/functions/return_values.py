#Return values
def my_function(x, y):
  return x + y #return the result sum of arguments

result = my_function(5, 3)
print(result)

#Returning Different Data Types
def my_function2():
  return ["apple", "banana", "cherry"]

fruits = my_function2()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function3():
  return (10, 20)

x, y = my_function3()
print("x:", x)
print("y:", y)