student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
for val in student_heights:
  total += val

count = 0
for element in student_heights:
  count += 1

avg_height = round(total / count)

print(avg_height)