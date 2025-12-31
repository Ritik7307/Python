a = input("Enter your name: ")
print("Hello, " + a + "!")  

# input() function always returns data as string type
# so if you want to take numeric input, you need to convert it explicitly

age = input("Enter your age: ")
age = int(age)  # converting string input to integer    
print("You will be " + str(age + 1) + " years old next year.")