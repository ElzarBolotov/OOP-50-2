def simple_dec(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

@simple_dec
def print_text():
    print("text")

print_text()


# def greeting_dec(func):
#     def wrapper(name):
#         print("Hello", name)
#         func(name)
#         print("Goodbye", name)
#     return wrapper
#
# @greeting_dec
# def say_hello(*, **):
#     print("Hello", name)
#
# say_hello("John")

