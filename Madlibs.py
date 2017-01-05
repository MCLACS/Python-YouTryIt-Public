import Epic

sentence = ("In the shadowy world of spies, a/an ADJ1 organization like the US "
            "Government uses spies to infiltrate ADJ2 groups for the purpose of "
            "obtaining top secret PLNOUN1.  A teacher, CELEB, or even the little "
            "old NOUN with a cane and fifteen pet PLNOUN2 could be a spy.")
            
adj1 = Epic.userString("Enter an adjective:")
adj2 = Epic.userString("Enter another adjective:")
plNoun1 = Epic.userString("Enter a plural noun:")
plNoun2 = Epic.userString("Enter another plural noun:")
celeb = Epic.userString("Enter a celebrity:")
noun = Epic.userString("Enter a noun:")
print
sentence = sentence.replace("ADJ1", adj1)
sentence = sentence.replace("ADJ2", adj2)
sentence = sentence.replace("PLNOUN1", plNoun1)
sentence = sentence.replace("PLNOUN2", plNoun2)
sentence = sentence.replace("CELEB", celeb)
sentence = sentence.replace("NOUN", noun)

print sentence