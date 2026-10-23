
import re

def analyze_id(reg_id):
    pattern = r"^(\d{2})([A-Z]{2})(\d{2})(\d{3})$"
    match = re.fullmatch(pattern, reg_id)

    if not match:
        return "Invalid Registration ID"

    year_code, branch, admission_year, number = match.groups()

    branches = {
        "CS": "Computer Science",
        "EC": "Electronics",
        "ME": "Mechanical",
        "EE": "Electrical"
    }

    if branch not in branches:
        return "Invalid Branch Code"

    return (
        "Valid Registration ID\n"
        f"Campus Code: {year_code}\n"
        f"Branch: {branches[branch]}\n"
        f"Admission Year: 20{admission_year}\n"
        f"Student Number: {number}"
    )


reg_id = input().strip()
print(analyze_id(reg_id))
