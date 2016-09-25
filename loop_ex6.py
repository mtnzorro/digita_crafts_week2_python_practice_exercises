width = int(raw_input("Width: "))
height = int(raw_input("Height: "))
width_line = "*" * width
height_line = "*" + ((width - 2) * " ") + "*"
ranger = height - 2
print width_line

for num in range(ranger):
    print height_line

print width_line
