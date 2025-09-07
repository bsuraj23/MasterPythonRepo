import mathwewe

# try:
#     print(math.sqrt(-1))
# except ValueError:
#     print("Math domain error")

try:
    import non_existing_module
except ModuleNotFoundError:
    print("Module not found")
