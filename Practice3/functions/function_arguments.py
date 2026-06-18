#Arguments in Function
def my_function(fname): #fname is parameter
  print(fname + " Refsnes")

my_function("Emil") #Emil-(argument) Refnes
my_function("Tobias") #Tobias-(argument) Refnes
my_function("Linus") #Linus-(argument) Refnes

def my_function2(fname, lname): # 2 parameters
  print(fname + " " + lname)

my_function2("Emil", "Refsnes") # 2 arguments

def my_function3(name = "friend"): #if haven't an argument you use default parameter
  print("Hello", name)

my_function3("Emil")
my_function3("Tobias")
my_function3()
my_function3("Linus")

#Keyword arguments
def my_function4(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function4(animal = "dog", name = "Buddy")

my_function4(name = "Buddy", animal = "dog")

#Positional Arguments
def my_function5(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function5("dog", "Buddy")

#Mixing Positional and Keyword Arguments
def my_function6(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function6("dog", name = "Buddy", age = 5)

#Passing Different Data Types
def my_function7(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function7(my_fruits)

def my_function8(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function8(my_person)

