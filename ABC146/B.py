n = int(input())
s = input()

result = ""
for i in s :
    result += chr(((ord(i) + n - 65) % 26) +65)

print(result)