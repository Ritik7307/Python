# List Methods: 

# list.sort() => this method sort list in ascending order

num = [4,5,6,7,9,7,5,2,1,0,4,3,7]
num.append(8)
# num.sort()
num.sort(reverse=True)
print(num)
num.reverse()

print(num.index(1))
print(num.count(7))

m = num.copy()
m[0] = 0
print(num)
num.insert(2,0)

p=[900,800,700]
num.extend(p)
print(num)