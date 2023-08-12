b = bin(int(input()))[2:]
b = b.replace('0', "B").replace('1', "AB")
print(b[:-1])