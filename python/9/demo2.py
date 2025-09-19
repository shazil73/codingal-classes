class animal:

    def __init__ (self, name):
        print("This is an animal class")
        self.name = name

    def do_sum(self, a , b , c):
        self.shazil = a + b + c

a = animal('dog')
print(a)
print(a.do_sum(65 , 28 , 30))
print(a.shazil)

k = animal('cat')
print(k)
k.do_sum(37 , 28 , 30)
print(k.shazil)