str = raw_input("Provide a string: ")
aph_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
decrypt = []
enc_list = list(str)
for n in str:
    if n == " ":
        decrypt.append(n)
    else:
        place = aph_list.index(n);
        idx = place + 13
        if idx > 25:
            idx = idx - 26
        decrypt.append(aph_list[idx])

decryp = ''.join(decrypt)
print decryp


#listy = list(str)

#listy[0] = str[0].upper()
#cap = ''.join(listy)
#print cap
