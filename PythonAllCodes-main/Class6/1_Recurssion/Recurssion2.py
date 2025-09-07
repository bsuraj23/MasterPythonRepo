



# Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))






# Example of recursion with string reversal
def reverse_string(s):      
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])   
    
result = reverse_string("ricky")
print(result)  # Output: "olleh"