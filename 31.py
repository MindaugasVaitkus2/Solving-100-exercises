#  Why is there an error in the code and how would you fix it?

# def foo(a=1, b=2):
#     return a + b
 
# x = foo - 1

# how I fixed
def foo(a=1, b=2):
    return a + b
 
x = foo() - 1
#print x

# this error occurs because the function was not called with parenthesis