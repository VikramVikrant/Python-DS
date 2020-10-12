#Find value of k-th bit in binary representation
# Python 3 program to find
# k-th bit from right
def printKthBit(n, k):
    print(n & (1 << (k - 1)))


n = 13
k = 2
printKthBit(n, k)