# constructor and destructor
# class of birds
class birds:
#this is a constructor 
    def __init__(self, name, size):
        print("This is a birds class")
        self.name = name
        self.size = size
# this is a method
    def color(self):
        print('This is a color of bird')
# this is a destructor
    def __del__ (self):
        print('Destructor called, birds deleted.')
# object of class
a = birds('parrot', 'green')
# object of class
b = birds('peacock', 'blue')
# deleting object
del b
# calling method
a.color()
# b.color()
