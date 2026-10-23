
# University Admission Decision Engine

n = int(input())
applicants = []

for i in range(n):
    name = input()
    marks = list(map(int, input().split()))
    course = input()

    aggregate = sum(marks) / len(marks)

    if course == "CSE":
        cutoff = 80
        subject_eligible = marks[0] >= 75
    elif course == "ECE":
        cutoff = 70
        subject_eligible = marks[1] >= 60
    else:
        cutoff = 60
        subject_eligible = True

    if subject_eligible and aggregate >= cutoff:
        applicants.append((name, aggregate, course))

# Rank by aggregate marks, then name alphabetically
applicants.sort(key=lambda x: (-x[1], x[0]))

print("Eligible Applicants:")
for rank, applicant in enumerate(applicants, start=1):
    print(rank, applicant[0], f"{applicant[1]:.2f}", applicant[2])
