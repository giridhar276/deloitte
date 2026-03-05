

def simple_decorator(fn):
    def wrapper():
        print("before")
        fn()
        print("after")
    return wrapper


@simple_decorator 
def hello():
    print("hello")


hello()


#before
#hello
#after