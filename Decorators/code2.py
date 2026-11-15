def decorator(func):
    def wrapper():
        print("Transaction initiated")
        func()
        print("Transaction completed")
    return wrapper

@decorator
def hello():
    print("...Executing all steps")

# @decorator
# def hell():
#     print("...Code2")

hello()
# print()
# hell()