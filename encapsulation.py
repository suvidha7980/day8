# public members & public access modifier
class pub_mod:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Age(self):

        print("Age: ", self.age)

obj = pub_mod("Suvidha", 20)
print("Name: ", obj.name)
obj.Age()

########################################################################################################################

# Get and Set method to access private variables
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display(self):
        print(self.name)
        print(self.__age)

    def getAge(self):
        print(self.__age)

    def setAge(self, age):
        self.__age = age


person = Person("Suvidha", 12)
person.display()
person.setAge(20)
person.getAge()