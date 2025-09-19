class fruit:
    height = '12ft'
    def __init__(self, color):
        print("This is a fruit class")
        self.color = color

    def do_sum(self, a , b , c):
        self.shazil = a + b + c


a = fruit('green')

print(a)
print(a.do_sum(65 , 28 , 30))
print(a.shazil)

k = fruit('yellow')
k.do_sum(37 , 28 , 30)
print(k.shazil)
