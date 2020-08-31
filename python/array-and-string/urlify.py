# Write a method to replace all spaces in  a string with %20.

# input : "hello  world "
# output : "hello%20world"

def urlify(str):
    ar = list(str)
    s = ''
    isSpace = False
    for c in ar:
        if ord(c) == 32:
            isSpace = True
        elif isSpace == True:
            isSpace =  False
            s += "%20" + c
        else :
            s += c

    return s
