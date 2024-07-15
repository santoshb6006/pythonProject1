# Lamda Expression
# You can use lambda expressions to create anonymous functions.
# That is, functions that don't have a name.
# They are helpful for creating quick functions that don't need to be reused.
# Here's an example of how you might use a lambda expression to square a number:
# Used to do the task in one line
def double_sal(sal):
    return sal * 2

new_salary= double_sal(1000)
print(new_salary)


new_salary=lambda sal:sal*2
print(new_salary(4000))
# Using lambda
new_salary= (lambda sal: sal * 2)(51300)
print(new_salary)