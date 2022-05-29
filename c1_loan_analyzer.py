# coding: utf-8
# csv and Path imports
import csv
from pathlib import Path

# Part 1: Automate the Calculations
loan_costs = [500, 600, 200, 1000, 450]

# Number of loans in the list
loan_costs_length = len(loan_costs)

print(f"There are {loan_costs_length} loans total")

# Sum of the loan costs in the list
loan_costs_total = sum(loan_costs)

print(f"The sum of all the loan prices is ${loan_costs_total:.2f}.")

# Average loan amount based on the list
average_loan_costs = loan_costs_total / loan_costs_length

print(f"The average loan price is ${average_loan_costs:.2f}.")
print()


# Part 2: Analyze Loan Data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Variables from loan dictionary
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

print(f"The future value of the loan is ${future_value:.2f}.")
print(f"There are {remaining_months} months remaining for the loan.")

# Present value formula
discount_rate = 0.20

present_value_1 = future_value / (1 + discount_rate / 12) ** remaining_months

print(f"The present value of the loan is ${present_value_1:.2f},")

# Loan cost and if-else decision making
loan_cost = loan.get("loan_price")

print(f"and the price of the loan is ${loan_cost:.2f}.")

if present_value_1 >= loan_cost:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expenive and not worth the price.")
print()


# Part 3: Perform Financial Calculations
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Function for calculating present value
def present_value_calculator(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
    return present_value

# Present value calculation
annual_discount_rate = 0.20

present_value = present_value_calculator(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)

print(f"The present value of the loan is ${present_value:.2f}.")
print()



# Part 4: Conditionally filter lists of loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# List to be filled
inexpensive_loans = []

# Loop and append anything less than or equal 500 to inexpensive_loans
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan["loan_price"])

# Print results
print(f"{inexpensive_loans} are all the loans costing $500 or less.")



# Part 5: Save the results
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Open file and create writer to write headers and contents of inexpenive_loans
with open("inexpensive_loans.csv", "w", newline="") as inexpensive_loans_csv:
    writer = csv.writer(inexpensive_loans_csv)
    writer.writerow(header)
    for row in inexpensive_loans:
        writer.writerow(loan.values())