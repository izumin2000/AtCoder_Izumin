a,b = map(int,input().split())
st_a,st_b = a,b
n_lis = [input().split() for i in range(50)]
p_lis = [list(map(int,input().split())) for j in range(50)]
ans_lis = []
perfect_lis = []
already_lis = []
already_lis.append(n_lis[a][b])
max_p = 0
p = 0
p += p_lis[a][b]

for k in range(1000):
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p
  
ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue  
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p

ans_lis = []
already_lis = []
a,b = st_a,st_b
already_lis.append(n_lis[a][b])
p = 0
p += p_lis[a][b]
for k in range(1000):
  if b != 0:
    if not n_lis[a][b-1] in already_lis:
      b -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("L")
      p += p_lis[a][b]
      continue
  if a != 49:
    if not n_lis[a+1][b] in already_lis:
      a += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("D")
      p += p_lis[a][b]
      continue
  if b != 49:
    if not n_lis[a][b+1] in already_lis:
      b += 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("R")
      p += p_lis[a][b]
      continue
  if a != 0:
    if not n_lis[a-1][b] in already_lis:
      a -= 1
      already_lis.append(n_lis[a][b])
      ans_lis.append("U")
      p += p_lis[a][b]
      continue
  break
  
if p > max_p:
  perfect_lis = ans_lis
  max_p = p


ans = "".join(perfect_lis)
print(ans)