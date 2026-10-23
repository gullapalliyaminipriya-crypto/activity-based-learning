
# Student Timetable Conflict Detection

# Course schedules represented as strings
courses = {
    "Python": ("Monday", 9, 10, "R101"),
    "Web": ("Monday", 10, 11, "R102"),
    "AI": ("Monday", 9, 10, "R101"),
    "Maths": ("Tuesday", 9, 10, "R103")
}

# Unavailable rooms
unavailable_rooms = ["R103"]

conflicts = []

# Check room availability and timetable conflicts
for course, schedule in courses.items():
    day, start, end, room = schedule

    if room in unavailable_rooms:
        conflicts.append(
            f"{course}: Room {room} is unavailable"
        )

    # Compare with other courses
    for other, other_schedule in courses.items():
        if course >= other:
            continue

        d, s, e, r = other_schedule

        if day == d and start < e and s < end:
            conflicts.append(
                f"{course} and {other}: Time conflict"
            )

# Display results
print("Timetable Conflict Report")

if conflicts:
    for conflict in conflicts:
        print(conflict)
    print("Timetable is INVALID")
else:
    print("No conflicts found")
    print("Timetable is VALID")
