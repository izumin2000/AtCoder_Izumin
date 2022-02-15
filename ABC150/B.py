n = int(input())
s = input()
count = 0
t = s.replace("ABC", "a")
for i in t :
    if i == "a" :
        count += 1

print(count)