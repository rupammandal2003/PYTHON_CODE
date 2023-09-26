# Global variables are those variables which are outside the function and these remains forever
# Local variables are those variables which are inside the function and these destroy after the run of the function

x=4
print(f"the value of global x is {x}")

def hello():
    global x    # 'global' keyword allows the coder to change the global value inside a function
    x=3
    print(f"the value of local x is {x}")
    print("Hello man!")
    y=5
    print(y)
    
hello()
print(f"the value of global x is {x}")
# print(y)   # But we cannot call a local variable outside the function
