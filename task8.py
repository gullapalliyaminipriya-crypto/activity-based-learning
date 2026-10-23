
# Student Marks Matrix Analysis

n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    row = list(map(int, input().split()))
    marks.append(row)

# Row-wise statistics
print("\nStudent Statistics:")
averages = []

for i in range(n):
    total = sum(marks[i])
    avg = total / m
    averages.append(avg)
    print(f"Student {i + 1}: Total = {total}, Average = {avg:.2f}")

# Column-wise statistics
subject_averages = []

print("\nSubject Statistics:")
for j in range(m):
    total = sum(marks[i][j] for i in range(n))
    avg = total / n
    subject_averages.append(avg)
    print(f"Subject {j + 1}: Average = {avg:.2f}")

# Top performer
top = averages.index(max(averages))
print(f"\nTop Performer: Student {top + 1}")
print(f"Highest Average: {averages[top]:.2f}")

# Subjects with low average performance
threshold = 40
print("\nSubjects with Low Average Performance:")
found = False

for j in range(m):
    if subject_averages[j] < threshold:
        print(f"Subject {j + 1}")
        found = True

if not found:
    print("No subjects have an average below 40.")
