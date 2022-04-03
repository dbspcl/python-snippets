# Python program to demonstrate working of HashTable 
# There are 10 buckets in the hash table
# No chaining is done for collisions (values are replaced each time)
# The hash is to divide the key by a prime above N / 10
# 
class Node:
    # Creating a node - set next to None
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # showing a method to return the value (keeps knowledge of 'item' inside the class)
    def value(self):
        return self.item;

    def print(self):
        print("Key: " + str(self.key) + ", Value: " + self.value)


hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1


def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    if (hashTable[index] != []):
        print ("Collision at index " + str(index))
        # See if the existing entry is a key value pair (not a list Node). If so, make it a Node
        if (not isinstance(hashTable[index],Node)):
            hashTable[index] = Node(hashTable[index][0], hashTable[index][1])
            print("Converting value to Node")
            hashTable[index].print()
        current = Node(key, data)
        current.next = hashTable[index]
        hashTable[index] = current
    else:
        # No entry here currently. Put in the key value pair
        hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = []

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print ("Before collision")
print(hashTable)
print()
insertData(124, "collides-with-mango")
print()
print ("After inserting collides-with-mango")

# Print the hash table. It is now either key/value pairs or a linked list in each entry
for i in range(len(hashTable)):
    if (not isinstance(hashTable[i],Node)):
        print(hashTable[i])
    else:
        print ("Bucket " + str(i) + " is a linked list!")
        # Print the linked list item
        current = hashTable[i]
        while current != None:
            current.print()
            current = current.next

print()
insertData(135, "also-collides")
print()
print ("After inserting also-collides")

# Print the hash table. It is now either key/value pairs or a linked list in each entry
for i in range(len(hashTable)):
    if (not isinstance(hashTable[i],Node)):
        print(hashTable[i])
    else:
        print ("Bucket " + str(i) + " is a linked list!")
        # Print the linked list item
        current = hashTable[i]
        while current != None:
            current.print()
            current = current.next
