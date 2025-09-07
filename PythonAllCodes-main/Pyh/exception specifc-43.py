
print 'Subtraction program, v0.0.3 (beta)'
loop = 1
while loop == 1:
    try:
        a = input('Enter a number to subtract from > ')
        b = input('Enter the number to subtract > ')
    except NameError:
        print "\nYou cannot subtract a letter"
	continue
    except SyntaxError:
        print "\nPlease enter a number only."
	continue
    print a - b
    try:
        loop = input('Press 1 to try again > ')
    except (NameError,SyntaxError):
        loop = 0




while True:
    try:
        n = raw_input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print "Great, you successfully entered an integer!"

try:
    x = float(raw_input("Your number: "))
    inverse = 1.0 / x
finally:
    print("There may or may not have been an exception.")
print "The inverse: ", inverse
