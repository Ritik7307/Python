# Joining Sets
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
cities.intersection_update(cities2)
print(cities)
# cities4 = cities.symmetric_difference(cities2)
# cities4 = cities.difference(cities2)
# print(cities4)

# isdisjoint() // if items of given sets present setpresent in anothere set.Ths method return false if items are present, else it return True

# print(cities.isdisjoint(cities2)) #False

#issuperset()
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Seoul","Kabul"}
print(cities.issuperset(cities2))
cities3= {"Seoul","Madrid","Kabul"}
cities3= {"Tokyo","Madrid","Delhi"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

cities.add("Helsinki")
cities.remove("Tokyo")
cities.discard("Tokyo2") # will not throw error
cities.pop()
print(cities)

# del : del is not a method, rather it is a keyword which deletes the set entirely 

k = {"Hi","Raghav"}
del k
# print(k) #this will throw an error coz already deleted