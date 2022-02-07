# example1
def plus_ten(param):
    return param + 10

print(plus_ten(3))
# --> 13

# The variable param is the parameter of the function: plus_ten.
# 3 is the argument of this function.


# example2
print(plus_ten(1)) # 1 is a value.
# --> 11

arg = 21
print(plus_ten(arg)) # arg is a variable.
# --> 31

print(plus_ten(1 + 2)) # 1 + 2 is a expression.
# --> 13


# example3

def minus_ten(param):
    result = param - 10

# print(result)
'''
Traceback (most recent call last):
  File "week2.py", line 30, in <module>
    print(result)
NameError: name 'result' is not defined
'''

# The variable 'result' is defined inside the minus_ten function,
# so it says "name 'result' is not defined."


# example4
def multiply_ten(unique_name_param):
    return unique_name_param * 10
# print(unique_name_param)

'''
Traceback (most recent call last):
  File "week2.py", line 45, in <module>
    print(unique_name_param)
NameError: name 'unique_name_param' is not defined
'''
# unique_name_param is a variable which is defined inside the multiply_ten function
# so it says "name 'unique_name_param' is not defined."

print("----------------")
# example5
example5 = "outside of the function"
def print_five():
    example5 = "inside the function"
    print(example5)
    print(id(example5))

print_five()
print(example5)

print(id(example5))
# --> inside the function
# outside the function

# print_five() function assign string into example5, then print example5.
# 
# This means that when a variable defined outside a function has the same name
# as a local variable inside a function, python treat it as a different variable.
# I could make sure it by using id function and executing the program below.

example5 = "outside of the function"
def print_five():
    example5 = "inside the function"
    print(id(example5))

print_five()
print(id(example5))

# example -->
# 140672583984592
# 140672583983952
