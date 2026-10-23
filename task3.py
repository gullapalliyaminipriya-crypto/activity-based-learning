
# Student Performance Trend Analysis

students = {
    "Ravi": {
        "Python": [60, 70, 80],
        "Maths": [45, 50, 55],
        "Web": [75, 70, 65]
    },
    "Priya": {
        "Python": [80, 85, 90],
        "Maths": [75, 80, 85],
        "Web": [85, 90, 95]
    },
    "Arun": {
        "Python": [40, 45, 35],
        "Maths": [35, 30, 25],
        "Web": [50, 45, 40]
    }
}

for name, subjects in students.items():
    print("\nStudent:", name)
    total = 0
    count = 0
    weak_subjects = []

    for subject, scores in subjects.items():
        improvement = scores[-1] - scores[0]
        total += sum(scores)
        count += len(scores)

        print(subject, "Scores:", scores)
        print("Improvement/Decline:", improvement)

        if sum(scores) / len(scores) < 40:
            weak_subjects.append(subject)

    average = total / count
    print("Overall Average:", round(average, 2))
    print("Weak Subjects:", weak_subjects if weak_subjects else "None")

    if average >= 75:
        category = "Excellent"
    elif average >= 60:
        category = "Good"
    elif average >= 40:
        category = "Average"
    else:
        category = "Needs Improvement"

    print("Performance Category:", category)
