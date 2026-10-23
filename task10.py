
# University Academic Progression Audit

n = int(input("Enter number of subjects: "))

subjects = []
marks = []
prerequisites = []

for i in range(n):
    subject = input("Enter subject name: ")
    mark = float(input("Enter marks: "))
    prerequisite = input(
        "Is prerequisite completed? (yes/no): "
    ).lower()

    subjects.append(subject)
    marks.append(mark)
    prerequisites.append(prerequisite == "yes")

attendance = float(input("Enter attendance percentage: "))

pass_mark = 40
attendance_required = 75

failed_subjects = []
incomplete_prerequisites = []

for i in range(n):
    if marks[i] < pass_mark:
        failed_subjects.append(subjects[i])

    if not prerequisites[i]:
        incomplete_prerequisites.append(subjects[i])

print("\n--- Academic Progression Audit ---")

if failed_subjects:
    print("Failed Subjects:", ", ".join(failed_subjects))
else:
    print("All subjects passed.")

if attendance < attendance_required:
    print("Attendance requirement not met.")
else:
    print("Attendance requirement satisfied.")

if incomplete_prerequisites:
    print("Incomplete Prerequisites:",
          ", ".join(incomplete_prerequisites))
else:
    print("All prerequisites completed.")

# Determine progression eligibility
if (not failed_subjects
        and attendance >= attendance_required
        and not incomplete_prerequisites):
    print("Progression Status: ELIGIBLE")
else:
    print("Progression Status: NOT ELIGIBLE")

# Outstanding requirements
print("\n--- Outstanding Requirements ---")
if not failed_subjects and attendance >= attendance_required \
        and not incomplete_prerequisites:
    print("None")
else:
    for subject in failed_subjects:
        print("Pass requirement pending:", subject)

    if attendance < attendance_required:
        print("Attendance requirement pending.")

    for subject in incomplete_prerequisites:
        print("Prerequisite completion pending:", subject)
