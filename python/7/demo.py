# List
l = ['laptop', 10, 200, 'tablet']

print(l[0])
print(l[3])
print(l[1])
print(l[2]) 

l.append('smartphone')
print(l)
# POP
l.pop()
print(l)
# LENGTH
print(len(l))

print(l[0:3])

print(type(l))
# REVERSE
l.reverse()
print(l)

l.clear()
print(l)

# Dictionary

b = {'NAME' : 'John', 'AGE': 25, 'CITY': 'New York'}
print(b['NAME'])
print(b['AGE'])
print(b['CITY'])


print(b.get('NAME',0))

# POP
b.pop('AGE')
print(b)
# TYPE
print(type(b))
# CLEAR
b.clear()
print(b)

