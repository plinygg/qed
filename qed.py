# Project Euler Problem #148:
# Find the number of entries which are not divisible by 7 in the first one billion (10^9) rows of Pascal's triangle.
# **n(rows) starts at 1, not 0**

# vars
num_rows = 10**9
base = 7


# functions

# This function converts number "n" into base "p".
def converting_bases(n, p):
    num_in_base_p = []
    while n != 0:
        n, k = n//p, n%p
        num_in_base_p.insert(0, k)
        # print(num_in_base_p)
    return num_in_base_p

def f(l, base):
    if not l: return 0
    r = l[0]
    if r == 0: return f(l[1:], base)
    if r < base: r * (r + 1) // 2
    s = base * (base + 1) // 2
    return r * (r + 1) // 2 * s **(len(l) - 1) + (r + 1) * f(l[1:], base)

# This function uses the triangular formula to find out the number of entries in the first n rows of Pascal’s triangle.
total_entries = []
def elements_n_rows(n):
    triangular = (n * (n+1)) / 2
#                    ^^^
#     Triangular formula
    total_entries.append(triangular)
    return triangular

# Checks the percentage of the number of entries not divisible by base in num_rows and adds them to a list
elements_n_rows(num_rows)
percentage = []
def check_percentage(num_nondivisors):
    percentage.append(nondivisors / total_entries[0])

# more vars
nondivisors = f(converting_bases(num_rows, base), base)
ez_nums = ("{:,}".format(num_rows))
ez_nondivisors = ("{:,}".format(nondivisors))
# ("{:,}".format(nondivisors/num_rows)) is from stackoverflow.com; allows the number listed to have a comma every 3 digits for easier readability 

# running code
check_percentage(nondivisors)
percentage_rounded = [round(percentage[0], 5) * 100]
# Prints the percentage of the number of entries not divisible by num_rows and the rounded version of the percentage
print("Number of entries which are not divisible by " + str(base) + " in the first " + str(ez_nums) + " rows of Pascal's triangle: " + str(ez_nondivisors))
print("Percentage of numbers within the first " + str(ez_nums) + " rows that are not divisble by " + str(base) + "(rounded): " + str((percentage_rounded)[0]) + "%")
