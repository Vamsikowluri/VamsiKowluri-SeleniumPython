# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i, n):
#         print('*', end=' ')
#     print()
#
from operator import index

# Var = ['Cognine', 'Hyderabad']
# Var.insert(1, "Madhapur")
# print(Var)

# Pattern concepts
# Arrays

def reverse_pyramid_no_spaces(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

rows = 5
reverse_pyramid_no_spaces(rows)
