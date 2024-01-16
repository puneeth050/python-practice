# # The above class defines a metaclass that sets a class attribute to 100 and creates a class using
# # that metaclass.
# class Meta(type):
#     def __new__(cls, name, bases, dct):
#         x = super().__new__(cls, name, bases, dct)
#         x.attr = 100
#         return x

# class MyClass(metaclass=Meta):
#     pass

# print(MyClass.attr)

# def foo(v):
#     while True:
#         v = (yield v)

# bar = foo(1)
# print(next(bar))
# print(next(bar))
# print(bar.send(2))

def dec1(func):
    def wrapper(*args, **kwargs) :
        print("tEntering decl")
        result = func(*args, **kwargs)
        print("ttExiting decltt")
        return result
    return wrapper

def dec2(func) :
    def wrapper(*args, **kwargs) :
        print("ttEntering dec2")
        result = func(*args, **kwargs)
        print("ttExiting dec2tt")
        return result
    return wrapper

@dec1
@dec2
def greet (message) :
    print (message)

greet("World")
