a= input("Enter the number: ")
print(f"Multiplication table of {a} is:")

try:

    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    # print(e)
    print("Sorry some error occured")

print("Some imp lines of codes")
print("End of the program")