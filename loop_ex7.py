
star = []
space = [0,4]
x=0
y=0
for num in range (9):
    if (num % 2) == 1:
        star.append(num)

for num in star:
    x += 1
    space.append(4-x)

for num in star:
    y += 1
    print (space[y] * " ") + (num * "*")
