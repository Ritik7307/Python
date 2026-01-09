# Manipulating Tuple

countries = ("Spain","Itlay","India","England","Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries= tuple(temp)
print(countries)

tup1 = (0,0,1,3,4,5,2,3,5,7,9,56,4,3,21,1,2,3)
res = tup1.count(3)
print("Count of 3 in tup1 is:", res)