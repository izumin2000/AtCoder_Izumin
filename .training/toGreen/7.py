al = list(map(int, input().split()))

def ref(n) :
    return al[n]

n = ref(0)
n = ref(n)
n = ref(n)
print(n)
