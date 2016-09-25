start = int(raw_input("Height: "))
space = start
star = []
x=0
y=0
for number in range (start+1):
    star.append(number)

for num in star:
    print ((space - y) * " ") + ((num + x) * "*")
    x += 2
    y += 1
