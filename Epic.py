def userInt(prompt):
    print prompt,
    num = int(raw_input())
    return num
    
def userString(prompt):
    print prompt,
    s = raw_input()
    return s

def kmToMi(km):
    return 0.62 * km