# First method to create a 1 D array - initialized with 0's
N = 5
arr = [0]*N
print(arr)
# Print an array - another way
for i in range(N):
    print("%d" % arr[i],end=" ")
# or this, second method to create a 1 D array - initialized with 0's
N = 5
arr = [0 for i in range(N)]
print(arr)
# Note python syntax for setting these 2 variables
rows, cols = (5, 5)
# OR
rows = 5
cols = 5
# Extend this to 2 D array - initialized with 0's
# First way creates a "shallow list" - not what we want (e.g., arr[1][1] = xx will update first column in ALL rows)
# range function goes from 0 to the stop specified
arr = [[0]*cols]*rows
# set one cell
arr[1][1] = 47
print ("Note that this has multiple values set to 47 due to 'shallow list'")
print (arr)
# Correct way for a 2 D array - creates "separate list objects" for each column
arr = [[0 for i in range(cols)] for j in range(rows)]
# set one cell
arr[1][1] = 47
print ("This has the one element set to 47 as expected")
print (arr)
