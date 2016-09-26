start = int(raw_input("Height: "))
space = range(1,start+1)

x=1
y=1

for num in space:
    v = start - y
    print (v * " ") + (x * "*")
    x += 2
    y += 1
