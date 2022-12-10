base = 7

def converting_bases(n, p):
    num_in_base_p = []
    while n != 0:
        n, k = n//p, n%p
        num_in_base_p.insert(0, k)
    return num_in_base_p


# finds the number of entries not divisible in row n in base p
def numnotdivisible(rownumbase):
    product = 1
    for digit in rownumbase:
        product = product * (digit + 1)
    return product

# print(numnotdivisible([2]))


def sumrownotdivisible(num_rows):
    sum = 0
    for row in list(range(0, num_rows + 1)):
        # print(row)
        numinbasep = converting_bases(row, base)
        numnotdivis = numnotdivisible(numinbasep)
        sum = sum + numnotdivis
        # print(sum)
    
    return sum

print(sumrownotdivisible(6))
