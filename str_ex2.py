str = raw_input("Provide a string: ")
listy = list(str)
listy[0] = str[0].upper()
cap = ''.join(listy)
print cap
