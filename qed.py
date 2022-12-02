Project Euler Problem #148:
# Find the number of entries which are not divisible by 7 in the first one billion (10^9) rows of Pascal's triangle.

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
    first_val = l[0]
    if first_val == 0: return f(l[1:], base)
    if first_val < base: first_val * (first_val+1) // 2
    s = base * (base+1) // 2
    return first_val * (first_val+1) // 2 * s **(len(l)-1) + (first_val+1) * f(l[1:], base)

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
    # print(percentage[0])
    # print(round(percentage[0], 0))

# dependent vars
nondivisors = f(converting_bases(num_rows, base), base)
ez_nums = ("{:,}".format(num_rows))
ez_nondivisors = ("{:,}".format(nondivisors))
# ("{:,}".format(nondivisors/num_rows)) is from stackoverflow.com; allows the number listed to have a comma every 3 digits for easier readability 

# running code
check_percentage(nondivisors)
print(f(converting_bases(num_rows, base), base))
print(total_entries)
print(percentage)
print(round(percentage[0], 3))

# Prints the percentage of the number of entries not divisible by num_rows and the rounded version of the percentage
# how do you find the total number of entries in the first num_rows rows?
print("Percentage of numbers within the first " + str(ez_nums) + " rows that are not divisble by " + str(base) + "(rounded): " + str(round(percentage[0], 3)) + "%")
print("Number of entries which are not divisible by " + str(base) + " in the first " + str(ez_nums) + " rows of Pascal's triangle: " + str(ez_nondivisors))

# print("total entries: " + str(total_entries))

# p = 12
# # p, r = p+2, p+4
# # print(p)
# # print(r)

# p = p+2
# r=p+4
# print(p)
# print(r)
