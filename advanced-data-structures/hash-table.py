# Python program to demonstrate working of HashTable 
# There are 10 buckets in the hash table
# No chaining is done for collisions (values are replaced each time)
# The hash is to divide the key by a prime above N / 10
# 

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
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = []

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print ("After inserting 4 key/value pairs into the 10 buckets")
print(hashTable)

removeData(123)

print ("After removing the one with key 123")
print(hashTable)

print ("Create a collision with mango - will replace")
insertData(124, "collides-with-mango")
print(hashTable)

