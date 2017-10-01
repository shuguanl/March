""" 
THis is an example

__doc__ could be defined in this section
"""
class classAnimal(object):
    """description of class"""
    def __init__(self, weight) :
        self.weight = weight

    def __add__(self, other) :
        return classAnimal(self.weight + other.weight)

    def __str__(self):
        return 'Animal (%d)'%self.weight

    def Name(self) :
        print("Hello")

dog = classAnimal(15)
dog.Name()

cat = classAnimal(10)
cat.Name()

print(dog+cat)
    

