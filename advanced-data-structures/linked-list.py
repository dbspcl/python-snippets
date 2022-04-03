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
        if (not isinstance(hashTable[index],Node)):
            hashTable[index] = Node(key, data)
            hashTable[index].print()
        else:
            current = hashTable[index]
            while (current.next != None):
                current = current.next
            next = Node(key, data)
            current.next = next
    else:
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
insertData(124, "collides-with-mango")
print ("After inserting collides-with-mango")
for i in range(len(hashTable)):
    if (not isinstance(hashTable[i],Node)):
        print(hashTable[i])
    else:
        print ("Bucket " + str(i) + " is a linked list!")
        # Print the linked list item
        current = hashTable[i]
        while current != None:
            print(str(current.key) + ": '" + current.value + "'")
            current = current.next
insertData(135, "also-collides")
print ("After inserting also-collides")
for i in range(len(hashTable)):
    if (not isinstance(hashTable[i],Node)):
        print(hashTable[i])
    else:
        print ("Bucket " + str(i) + " is a linked list!")
        # Print the linked list item
        current = hashTable[i]
        while current != None:
            print(str(current.key) + ": '" + current.value + "'")
            current = current.next
