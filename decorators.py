def greet(fx):
    def mfx(*args,**kwargs):
        print("Good morning!")
        fx(*args,**kwargs)
        print("Thanks for using this function.")
    return mfx

@greet
def hello():
    print("hello sir how are you?")

# @greet
# def add(a,b):
#     print(a+b)
    
# add(12,25)

hello()