## Finally Clause:
The finally code block is also a part of exception handeling. When we handle exception using the try and except block , we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

## Syntax:

try:
    # statements which could generate
    # exception
except:
    # solution of generated exception
finally:
    #block of code which is going to execute in any situation