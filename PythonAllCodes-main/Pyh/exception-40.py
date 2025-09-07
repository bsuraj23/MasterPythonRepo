def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry

    return input(question) - 1

# running the function
# remember what the backslash does
answer = menu(['A','B','C','D','E','F','H','I'],\
'Which letter is your favourite? ')

print 'You picked answer ' + (answer + 1)

def menu1(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry
    try:
        return input(question) - 1
    except NameError:
        print "Enter a correct number"


 # from when we finish defining the function
answer = menu(['A','B','C','D','E','F','H','I'],\
'Which letter is your favourite? ')
try:
    print 'You picked answer', (answer + 1)
    # you can put stuff after a comma in the 'print' statement,
    # and it will continue as if you had typed in 'print' again
except:
    print '\nincorrect answer.'
    # the '\n' is for formatting reasons. Try without it and see.
