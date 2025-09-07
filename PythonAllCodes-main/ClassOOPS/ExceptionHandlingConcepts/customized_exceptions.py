# How to Define and Raise Customized Exceptions
class MyError(Exception):
    pass
try:
    raise MyError("Custom error occurred")
except MyError as e:
    print(e)
