marks = [3,5,7,"Dustin",True]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-3])
print(marks[len(marks)-3])

if 7 in marks:
    print("Yes")
else:
    print("No")

if "arry" in "Harry":
    print("Yes")
else:
    print("No")

print(marks[:])
print(marks[1:-1]) # 1:4
print(marks[1:4:2])

#  List Comprehension
names = ["Milo", "Sarah","Bruno","Anastesia","Rosa"]
namesWith_o= [item for item in names if "o" in item]
print(namesWith_o)

# lst = [ i*i for i in range(4)]
lst = [ i*i for i in range(10) if i%2==0]
print(lst)