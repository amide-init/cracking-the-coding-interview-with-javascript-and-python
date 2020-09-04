# implement an algorithms to determine if a string has all unique characters.
# what if you cannot use additional data structure ?

def  isUnique(str):
    ar = [0]*128
    for i in range(len(str)):
        if ar[ord(str[i])] > 0 :
            return False
        ar[ord(str[i])] += 1
    return True

print(isUnique("apple"))

