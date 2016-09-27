list_of_strings = ['big', 'toot', 'red', 'car', 'big', 'toot']
de_dup = []
for word in list_of_strings:
    if de_dup.index(word) < 0:
        de_dup.append(word)

print de_dup



#listy = list(str)

#listy[0] = str[0].upper()
#cap = ''.join(listy)
#print cap
