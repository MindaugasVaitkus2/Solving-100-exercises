# Why is there an error in the code and how would you fix it?

# def foo(a, b):
#     print(a + b)
 
# x = foo(2, 3) * 10

def foo(a, b):
    return(a + b)
 
x = foo(2, 3) * 10
print x

# return will returns the value, while print only prints it on the screen. So for us to have the value and multiply 10 to it we need to use return and then print. 

# The other option would be to do the multiplication inside the function, assuming we will always want to multiply by 10. 
def foo(a, b):
    return(a + b) *10
 
x = foo(2, 3) 
print x

# Or we could add another variable to the function and the user could choose the number we are multiplying by
def foo(a, b, mult):
    return(a + b) * mult
 
x = foo(2, 3, 10) 
print x

# his answer
#Line 4 throws a TypeError because Python cannot multiply a None type object with an integer. The function output is what produces a None object because the function definition is not returning anything. Fix it by using return  instead of print :

# def foo(a, b):
#     return a + b
 
# x = foo(2, 3) * 10