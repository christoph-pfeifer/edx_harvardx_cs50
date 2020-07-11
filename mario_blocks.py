block, space, lines = "#", " ", 10

for i in range (lines):
    print((lines-i-1)*space + (i+1)*block + 3*space + (i+1)*block + (lines-i-1)*space)
