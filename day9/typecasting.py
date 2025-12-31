a = '1'
b = '2'
print(a + b)

# Explicit conversion - type casting
c= int(a) + int(b)
print(c)

# Implicit conversion - done by python interpreter
d = 2 + 3.5
print(d)
print(type(d))  
# here integer 2 is implicitly converted to float 2.0 before addition
