# Given two string, 
# write a method to decide if one is permutation of the other

# method 1 [by sorting the string]
# Time complexity O(nlogn) space O(1)

def checkPermutation(str1, str2):
     s1 = sorted(str1)
     s2 = sorted(str2)
     if s1 == s2:
         return True
     return False


# method 2 [by using hashTable]
# Time complexity O(n) and space O(n)

def checkPermutationUsingHashTable(str1, str2):
    if len(str1) != len(str2):
     return False
    hash = {}
    for c in str1:
        if hash.get(c) == None:
            hash[c] = 1
        else:
            hash[c] += 1
    
    for c in str2:
        if hash.get(c) == None or hash.get(c) <=0:
            return False
        hash[c] -= 1
        
    return True












