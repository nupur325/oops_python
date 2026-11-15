def greet(func):
    def mgreet(*args,**kwargs):
        #if a function passes arguments..args kwargs should be defined in decorator
        print("Before decorator")
        func(*args,**kwargs) 
        print("After decorator")
    return mgreet #always return sub func

@greet
def hello():
    print("Hello world")

@greet
def add(a,b):
    print(a+b)
    #here we are taking arguments so decorator function should define args kwargs

hello()
# greet(hello)() //another way to call function
add(3,2)