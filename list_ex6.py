list_of_nums = [34, 9000, 50, 80, 99]
list_of_nums_2 = [5, 6, 10, 50, 43]
list_range = range (len(list_of_nums))
products = []
for i in list_range:
    products.append(list_of_nums[i] * list_of_nums_2[i])
print products



#listy = list(str)

#listy[0] = str[0].upper()
#cap = ''.join(listy)
#print cap
