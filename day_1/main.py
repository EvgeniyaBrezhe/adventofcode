with open('input.csv', 'r') as file:
    lines = file.readlines()

left_column = []
right_column = []

for line in lines:
    left, right = map(int, line.split())
    left_column.append(left)
    right_column.append(right)

left_column.sort()
right_column.sort()

total_distance = 0
for i in range(len(right_column)):
    distance = abs(left_column[i] - right_column[i])
    total_distance += distance

print(f"Total Distance: {total_distance}")

similarity_score = 0
for i in left_column:
    individual_score = i * right_column.count(i)
    similarity_score += individual_score

print(f"Similarity Score: {similarity_score}")