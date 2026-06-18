class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the super() Function
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    #Add Properties
    self.graduationyear = 2019
