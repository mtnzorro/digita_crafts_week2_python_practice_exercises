import math
num = int(raw_input("Provide a number: "))
top = int(math.ceil(math.sqrt(num)))
total_range = range(1,top+1)
factors = []

for mult in total_range:
    if mult == num:
        factors.append(mult)
    if num % mult == 0:
        a = num/mult
        factors.append(mult)
        factors.append(a)
    else:
        pass
print factors
