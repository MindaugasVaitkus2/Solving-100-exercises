# Why do you get an error and how would you fix it?

# def foo(a=2, b):
#     return a + b

# The error happens because non-default argument (b) is following default argument (a = 2). The order of defining parameter in function are: non-default argument (b in this example); default parameter (a = 2, in this example) then keyword only parameter (*args) and then var keyword parameter(**kwargs)

# how I would fix it:
def foo(b, a=2):
    return a + b