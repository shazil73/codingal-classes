# this is a tuple
shazil = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# print shazil elements
print(shazil[0])
print(shazil[3])
print(shazil[1])
# we cannot change tuple elements
# shazil[0] = 100
# print(shazil)

for i in range(0, len(shazil)):
    print(shazil[i])

print(shazil[2:5])

# SETS
shazil2 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
yash2 = {50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150}
# print sets
print(shazil2)
print(yash2)
# add element to set
shazil2.add(110)
yash2.add(40)
# print sets
print(shazil2)
print(yash2)
# lets intersect two sets
print(shazil2.intersection(yash2))
# lets union two sets
print(shazil2.union(yash2))
# difference of two sets
print(shazil2.difference(yash2))
# symmetric difference of two sets
print(shazil2.symmetric_difference(yash2))