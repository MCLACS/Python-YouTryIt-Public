def main():
    d = {}
    for line in open("CourseList.txt"):
        lst = line.split(",")
        semester = lst[0].strip()
        cls = lst[1].strip()
        if semester in d:
            d[semester].append(cls)
        else:
            d[semester] = [cls]
    
    for key in d.keys():
        print "%s: %s" % (key, d[key])
        
main()