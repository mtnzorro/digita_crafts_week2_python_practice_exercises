sstr = raw_input("Provide text for transalation to leatspeak: ")
listy = list(sstr)
leeted = []

for letter in listy:
    if letter.upper() == "A":
        leeted.append("4")
    elif letter.upper() == "E":
        leeted.append("3")
    elif letter.upper() == "G":
        leeted.append("6")
    elif letter.upper() == "I":
        leeted.append("1")
    elif letter.upper() == "O":
        leeted.append("0")
    elif letter.upper() == "S":
        leeted.append("5")
    elif letter.upper() == "t":
        leeted.append("7")
    else:
        leeted.append(letter)
leeted = "".join(leeted)
print leeted



#listy = list(str)

#listy[0] = str[0].upper()
#cap = ''.join(listy)
#print cap
