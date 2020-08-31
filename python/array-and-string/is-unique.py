def  isUnique(str):
    ar = [0]*128
    for i in range(len(str)):
        if ar[ord(str[i])] > 0 :
            return False
        ar[ord(str[i])] += 1
    return True

print(isUnique("apple"))

