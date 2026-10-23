
# ATM Transaction Sequence Simulation

balance = float(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))

deposits = 0
withdrawals = 0
rejected = 0
withdrawal_limit = 10000

for i in range(n):
    transaction = input().split()
    transaction_type = transaction[0].upper()
    amount = float(transaction[1])

    if amount <= 0:
        print("Invalid transaction")
        rejected += 1

    elif transaction_type == "DEPOSIT":
        balance += amount
        deposits += 1
        print("Deposit successful")

    elif transaction_type == "WITHDRAW":
        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded")
            rejected += 1
        elif amount > balance:
            print("Insufficient balance")
            rejected += 1
        else:
            balance -= amount
            withdrawals += 1
            print("Withdrawal successful")

    else:
        print("Invalid transaction")
        rejected += 1

print("\n----- ATM TRANSACTION SUMMARY -----")
print(f"Final Balance: {balance:.2f}")
print(f"Successful Deposits: {deposits}")
print(f"Successful Withdrawals: {withdrawals}")
print(f"Rejected Transactions: {rejected}")
