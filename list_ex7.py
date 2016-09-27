list_of_mat1 = [[1, 2, 3], [3, 4, 5]]
list_of_mat2 = [[5,6, 7], [7,8, 9]]
sub_list1 = list_of_mat1.pop()
sub_list2 = list_of_mat2.pop()
list_of_mat1 = list_of_mat1.pop()
list_of_mat2 = list_of_mat2.pop()
list_range = range (len(sub_list1))
sums1 = []
sums2 = []
final_sums = []
for i in list_range:
    sums1.append(list_of_mat1[i] + list_of_mat2[i])
    sums2.append(sub_list1[i] + sub_list2[i])
final_sums.append(sums1)
final_sums.append(sums2)
print final_sums



#listy = list(str)

#listy[0] = str[0].upper()
#cap = ''.join(listy)
#print cap
