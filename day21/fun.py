# Default Arguments:

def name(fname,mname = 'John', lname='Whatson'):
    print("Hello,",fname,mname,lname)
name("Amy")

def average(a =9,b =1):
    print("The average is ", (a+b)/2)
average(4,6)

# Keyword Arguments:

def name(fname,mname,lname):
    print("Hello",fname,mname,lname)
name(mname="Peter",lname="Wesker",fname="Jade")

# Required Arguments:

def name(fname,mname,lname):
    print("Hello",fname,mname,lname)
# name("Peter","Quill") #required hai


# Arbitary Arguments:

def name(*name):
    print("Hello",name[0],name[1],name[2])
name("James","Buchanan","Barnes")

def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum+i
    # print("Average is :",sum/len(numbers))
    return sum/len(numbers)


c = average(8,9, 92)
print(c)

# return Stateement: is used to return the value of the expressionbback to the calling function