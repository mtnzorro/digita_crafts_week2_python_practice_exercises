sstr = raw_input("Provide text for long-long vowel test: ")
listy = list(sstr)
longed = []

for letter in listy:
    if letter.upper() == "AA":
        longed.append("aaaaa")
    elif letter.upper() == "EE":
        longed.append("eeeee")
    elif letter.upper() == "II":
        longed.append("iiiii")
    elif letter.upper() == "OO":
        longed.append("ooooo")
    elif letter.upper() == "UU":
        longed.append("uuuuu")

    else:
        longed.append(letter)
longed = "".join(longed)
print longed



#listy = list(str)

#listy[0] = str[0].upper()
#cap = ''.join(listy)
#print cap
