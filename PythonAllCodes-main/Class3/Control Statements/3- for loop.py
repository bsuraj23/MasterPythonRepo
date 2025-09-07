#!/usr/bin/python





 # Measure some strings:
names  = ['mohan', 'sunil', 'uday','ttttt']
for temp in names:
     print(temp)

#cat 3
#window 6
#defenestrate 12



#range([start], stop[, step])
1,2,3,4,5,6,7,8,9
for i in range(1,10,2):
    print(i)

#loop with else block  
# # ...existing code...

# loop with else block
for name in names:
    print(name)
else:
    print("All names have been printed.")

# Example with break and else
for i in range(1, 10):
    if i == 5:
        print("Found 5, breaking loop.")
        break
    print(i)
else:
    print("Loop completed without break.")   

# If the loop finishes all iterations, the else block runs.
# If the loop is exited early with break, the else block is skipped.



