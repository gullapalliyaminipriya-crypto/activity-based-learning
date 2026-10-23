import re

def validate_email(email):
    errors = []

    if "@" not in email:
        errors.append("Missing @ symbol")
    elif email.count("@") > 1:
        errors.append("Multiple @ symbols")

    if " " in email:
        errors.append("Spaces are not allowed")

    if "@" in email:
        parts = email.split("@")

        if not parts[0]:
            errors.append("Missing username")

        if len(parts) == 2:
            if not parts[1]:
                errors.append("Missing domain")
            elif "." not in parts[1]:
                errors.append("Missing domain separator")
            elif parts[1].startswith(".") or parts[1].endswith("."):
                errors.append("Invalid domain format")

    if not errors:
        return "Valid Email"

    return ", ".join(errors)


def validate_id(reg_id):
    pattern = r"^STU-\d{4}$"

    if re.fullmatch(pattern, reg_id):
        return "Valid Registration ID"

    errors = []

    if not reg_id:
        return "Missing registration ID"

    if not reg_id.startswith("STU-"):
        errors.append("Invalid identifier prefix")

    if "-" not in reg_id:
        errors.append("Missing separator")
    elif reg_id.count("-") > 1:
        errors.append("Malformed separators")

    digits = reg_id.split("-")[-1]

    if not digits.isdigit():
        errors.append("Invalid character group")
    elif len(digits) != 4:
        errors.append("Identifier must contain 4 digits")

    return ", ".join(errors) if errors else "Valid Registration ID"


email = input().strip()
reg_id = input().strip()

print("Email:", validate_email(email))
print("Registration ID:", validate_id(reg_id))