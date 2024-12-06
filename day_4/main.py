import re

import np

WORD = "XMAS"

with open("input.txt", "r") as file:
    matrix = [list(line.strip()) for line in file if line.strip()]

def count_string_in_list(list_by_index, xmas_word):
    xmas_count = 0
    my_string = "".join(list_by_index)
    count = len(re.findall(xmas_word, my_string))
    xmas_count += count
    return xmas_count


def count_string_in_matrix(my_matrix, xmas_word):
    xmas_count = 0
    for i in my_matrix:
        count = count_string_in_list(i, xmas_word)
        xmas_count += count
    return xmas_count


horizontal_count_straight = count_string_in_matrix(matrix, WORD)
horizontal_count_backwards = count_string_in_matrix(matrix, WORD[::-1])
horizontal = horizontal_count_straight + horizontal_count_backwards
print(f"horizontal_count_straight: {horizontal_count_straight}")
print(f"horizontal_count_backwards: {horizontal_count_backwards}")

vertical_matrix = [["" for i in range(len(matrix))] for j in range(len(matrix))]

for first_index in range(len(matrix)):
    for second_index in range(len(matrix[first_index])):
        element = matrix[first_index][second_index]
        vertical_matrix[second_index][first_index] = element

vertical_count_straight = count_string_in_matrix(vertical_matrix, WORD)
vertical_count_backwards = count_string_in_matrix(vertical_matrix, WORD[::-1])
vertical = vertical_count_straight + vertical_count_backwards
print(f"vertical_count_straight: {vertical_count_straight}")
print(f"vertical_count_backwards: {vertical_count_backwards}")

left_matrix = []

count_left_straight = 0
count_left_backwards = 0
for i in range(-139, 140):
    left_diagonal = np.diag(matrix, i)
    new_left_diagonal = left_diagonal.tolist()
    count_left_straight += count_string_in_list(left_diagonal, WORD)
    count_left_backwards += count_string_in_list(left_diagonal, WORD[::-1])
    left_matrix.append(new_left_diagonal)

print(f"count_left_straight: {count_left_straight}")
print(f"count_left_backwards: {count_left_backwards}")
count_left = count_left_straight + count_left_backwards

right_matrix = []

count_right_straight = 0
count_right_backwards = 0
for i in range(-139, 140):
    right_diagonal = np.diag(np.fliplr(matrix), i)
    new_right_diagonal = right_diagonal.tolist()
    count_right_straight += count_string_in_list(right_diagonal, WORD)
    count_right_backwards += count_string_in_list(right_diagonal, WORD[::-1])
    right_matrix.append(new_right_diagonal)

print(f"count_right_straight: {count_right_straight}")
print(f"count_right_backwards: {count_right_backwards}")
count_right = count_right_straight + count_right_backwards

result = horizontal + vertical + count_left + count_right

print(f"Result #1: {result}")

count_of_xmases = 0
for i in left_matrix:
    diagonal_number = left_matrix.index(i)
    array_string = "".join(i)

    res = [i for i in range(len(array_string)) if array_string.startswith("MAS", i)
           or array_string.startswith("SAM", i)]

    if len(res) > 0:
        for i in res:
            n = len(matrix)
            k = diagonal_number
            p = i

            if k < n:
                row, col = n - 1 - k, 0
            else:
                row, col = 0, k - n + 1

            row += p
            col += p

            # print(f"Element index in initial matrix: ({row}, {col})")

            if (matrix[row][col + 2] == "M" and matrix[row + 2][col] == "S") and matrix[row+1][col + 1] == "A":
                count_of_xmases += 1
            if (matrix[row][col + 2] == "S" and matrix[row + 2][col] == "M") and matrix[row+1][col + 1] == "A":
                count_of_xmases += 1


print(f"Result #2: {count_of_xmases}")