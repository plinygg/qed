#Find the number of entries which are not divisible by 7 in the first one billion (10^9) rows of Pascal's triangle.

# vars
num_rows = 4

# functions
def int2(n, base):
    ret = []
    while n != 0:
        n, k = n//base, n%base
        ret.insert(0, k)
    return ret

def f(l, base):
    if not l: return 0
    r = l[0]
    if r == 0: return f(l[1:], base)
    if r < base: r * (r+1) // 2
    s = base * (base+1) // 2
    return r * (r+1) // 2 * s **(len(l)-1) + (r+1) * f(l[1:], base)


# prints
# 
print(f(int2(num_rows, 7), 7))