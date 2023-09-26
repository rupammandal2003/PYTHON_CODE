# Doc string can only be written under the function definition line otherwise it will not be evaluated

def square(n):
    '''it will take one input n and will give the output as the square of n'''  # this is doc-string
    return n**2

print(square(5))
print(square.__doc__)


# the underline code will give the Zen of python by Tim Peters 
# impot this