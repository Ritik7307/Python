# Python allows else keyword to be used with the for and while loops too. The else block appears after the body of the loop.The statement in te else block will be executed after all iterations are completed.The program exits the loop only after the else block is executed

# Syntax
'''
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block
'''

for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("Sorry, no i")


i=0
while i<7:

    print(i)
    i=i+1 
else:
    print("Sorry, no i")