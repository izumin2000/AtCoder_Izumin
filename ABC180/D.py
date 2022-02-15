a = 4
b = 2
c = 3
d = 127
ip = a*(256**3) + b*(256**2) + c*256 + d

aa = ip//(256**3)
bb = (ip - aa * (256**3))//(256**2)
cc = (ip - aa * (256**3) - bb * (256**2))//256
dd = ip%256

print(aa)
print(bb)
print(cc)
print(dd)