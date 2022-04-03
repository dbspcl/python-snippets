# Insertion sort in Python ("playing-cards hand")
# Implemented using an array
# Loop through each element in array (index step)
#  set key = value at current step
#  Starting with element on left, as long as element are greater than step value (and we haven't hit the beginning) (index j)
#   Move element on left into current spot
#  set value at index j+1 to key (since value at j was just smaller than it)
#

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
print('Unsorted Array:')
print(data)
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)