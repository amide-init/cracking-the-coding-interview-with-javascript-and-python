def isPelindromePermuation(st):
    hash = {}
    for c in st:
        if hash.get(c) == None:
            hash[c] = 1
        else:
            hash[c] += 1
    count = 0
    for i in hash: 
        if hash.get(i)%2 == 1:
            count+=1
        if count > 1:
            return False
    return True
    



print(isPelindromePermuation("ambbllba"))