# count = 0
# while count < 5:
#     print(count)
#     count += 1

# Use a nested for loop to iterate over a matrix (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
