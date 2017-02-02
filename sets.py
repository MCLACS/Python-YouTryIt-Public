
# --------------------------------------------------
# returns True if the item (item) is
# in the list (l).
# NOTE: matches should be case insensitive
# --------------------------------------------------
def containsNoCase(item, l):
    yes = False
    for x in l:
        if item.upper() == x.upper():
            yes = True
            break
    return yes

# --------------------------------------------------
# Returns the intersection of set1 and set2
# NOTE: matches should be case insensitive
# --------------------------------------------------
def intersection(set1, set2):
    result = []
    for i in set1:
        if containsNoCase(i, set2):
            result.append(i)
    return result
    
# --------------------------------------------------    
# Returns the union of set1 and set2
# NOTE: matches should be case insensitive
# --------------------------------------------------
def union(set1, set2):
    result = []
    
    for i1 in set1:
        if not containsNoCase(i1, result):
            result.append(i1)

    for i2 in set2:
        if not containsNoCase(i2, result):
            result.append(i2)
            
    return result
    
# -------------------------------------------------------
# Reads the studens in the specified file (filename) 
# and returns them in a list.
# -------------------------------------------------------
def readStudents(filename):
    l = []
    file = open(filename)
    for student in file:
        l.append(student.strip())
    return l    

# -------------------------------------------------------    
# Read in the class enrollment files and
# produce a report this shows:
#     students in both calculus and physics
#     students in either calculus or physics
# -------------------------------------------------------
def main():
    calc = readStudents("calc-students.txt")
    phys = readStudents("physics-students.txt")
    bothClasses = intersection(calc, phys)
    eitherClass = union(calc, phys)
    print "%s are in both calculus and phyics" % bothClasses
    print "%s are in either calculus or phyics" % eitherClass
   
# don't forget to call main! 
main()