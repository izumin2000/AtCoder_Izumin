s = input()
if s in ["SSS"] :
    print(0)
elif s in ["RSS", "SRS", "SSR", "RSR"] :
    print(1)
elif s in ["RRS", "SRR"] :
    print(2)
else :
    print(3)