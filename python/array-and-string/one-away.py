def isOneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1 :
        return False
    count = 0
    #insert
    if len(s1) < len(s2):
        count = 0
        m, n = 0, 0
        for i in range(len(s1)):
            if s1[m] != s2[n]:
              count +=1
              n+=1
            else:
                m+=1
                n+=1
            if count > 0:
              return False
    #remove
    elif len(s1) > len(s2) :
        count = 0
        m, n = 0, 0
        for i in range(len(s2)):
            if s1[m] != s2[n]:
              count +=1
              m+=1
            else:
                m+=1
                n+=1
            if count > 0:
              return False
    #replace
    else:
        count =0
        for i in range(len(s2)):
            if s1[i] != s2[i]:
              count +=1
            if count > 1:
                return False
    return True


              




print(isOneAway("abple", "apble"))

# Time complexity O(n)
# Space complexity O(1)

# can you do three check in single pass ?