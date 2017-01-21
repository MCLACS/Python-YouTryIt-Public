import Epic

band = Epic.userString("Enter the band you want to follow:")
file = open('concerts.txt')

for line in file:
    if band in line:
        print line,

print "\nHave fun and wear your ear plugs!"
