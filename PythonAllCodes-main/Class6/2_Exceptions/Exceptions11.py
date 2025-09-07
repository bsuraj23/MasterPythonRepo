#check for version context of else on except part 


try:
    num = 10
except:
    print("Error occurred")
else:
    print("No exception, num is", num)
finally:
    print("Execution completed")
