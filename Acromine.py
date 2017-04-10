import Epic
import json
import urllib2


abbr = Epic.userString("Please enter a abbreviation:")
url = 'http://www.nactem.ac.uk/software/acromine/dictionary.py?sf=' + abbr
jsonTxt = urllib2.urlopen(url).read()
acromine = json.loads(jsonTxt)

if len(acromine) == 0:
    print "No results"
else:    
    print acromine[0]['sf']
    for ans in acromine[0]['lfs']:
        print ans['lf']
