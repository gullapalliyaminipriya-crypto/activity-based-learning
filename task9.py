
# Campus Event Seating and Entry Validation

rows = int(input("Enter number of seating rows: "))
cols = int(input("Enter seats per row: "))

# Create nested list for seating
seats = [[None for _ in range(cols)] for _ in range(rows)]

registrations = set()
entered = set()

n = int(input("Enter number of registrations: "))

for i in range(n):
    reg_id = input("Enter registration ID: ")
    if reg_id in registrations:
        print("Duplicate registration ID!")
    else:
        registrations.add(reg_id)

        # Assign the first available seat
        assigned = False
        for r in range(rows):
            for c in range(cols):
                if seats[r][c] is None:
                    seats[r][c] = reg_id
                    print(f"{reg_id} assigned to Row {r + 1}, Seat {c + 1}")
                    assigned = True
                    break
            if assigned:
                break

        if not assigned:
            print("No seats available!")

# Ticket entry validation
k = int(input("\nEnter number of ticket scans: "))

for i in range(k):
    ticket = input("Enter ticket registration ID: ")

    if ticket not in registrations:
        print("Invalid ticket!")
    elif ticket in entered:
        print("Duplicate entry detected!")
    else:
        entered.add(ticket)
        print("Entry allowed!")

# Seating capacity report
total_capacity = rows * cols
occupied = sum(
    1 for row in seats for seat in row if seat is not None
)
available = total_capacity - occupied

print("\n--- Seating Report ---")
print("Total Capacity:", total_capacity)
print("Occupied Seats:", occupied)
print("Available Seats:", available)
print("Successful Entries:", len(entered))
