str = raw_input("Provide a string: ")
str_lis = list(str)
listy = []
for let in str:
    i = str_lis.pop()
    listy.append(i)
rev = ''.join(listy)
print rev

#listy = list(str)

#listy[0] = str[0].upper()
#cap = ''.join(listy)
#print cap
