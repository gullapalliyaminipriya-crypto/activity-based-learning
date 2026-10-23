
# Salary Statement Generator

basic_pay = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))
incentives = float(input("Enter incentives: "))

# Calculate gross salary
gross_salary = basic_pay + allowances + overtime + incentives

# Progressive deductions
if gross_salary <= 10000:
    deduction = gross_salary * 0.05
elif gross_salary <= 20000:
    deduction = (10000 * 0.05) + ((gross_salary - 10000) * 0.10)
else:
    deduction = (10000 * 0.05) + (10000 * 0.10) + ((gross_salary - 20000) * 0.15)

# Calculate net salary
net_salary = gross_salary - deduction

# Formatted salary statement
print("\n========== SALARY STATEMENT ==========")
print(f"Basic Pay       : Rs. {basic_pay:.2f}")
print(f"Allowances      : Rs. {allowances:.2f}")
print(f"Overtime        : Rs. {overtime:.2f}")
print(f"Incentives      : Rs. {incentives:.2f}")
print("--------------------------------------")
print(f"Gross Salary    : Rs. {gross_salary:.2f}")
print(f"Total Deductions: Rs. {deduction:.2f}")
print("--------------------------------------")
print(f"Net Salary      : Rs. {net_salary:.2f}")
print("======================================")
