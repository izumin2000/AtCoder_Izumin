x = int(input())
gohyaku = x//500
amari = x - gohyaku * 500
go = amari // 5

print(gohyaku * 1000 + go * 5)