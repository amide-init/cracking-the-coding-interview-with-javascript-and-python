def stringCompression(s):
    st = ""
    count = 0
    lastcount = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count+=1
        else :
            lastcount = count+1
            count = 0
            st += s[i-1] +  str(lastcount)
    return s if len(st) > len(s) else st + s[len(s)-1] + str(lastcount)

print(stringCompression("aabbbbcd")) 
        
