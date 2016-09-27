number = int(raw_input("Enter a positive number: "))

while number > 0:
    number -= 2
    if number == 2:
        result = "even"
    elif number == 1:
        result = "odd"
    else:
        pass
print "Your number is %s!" % result
