# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

#Calculate the total number of loans in the list.
total_number_of_loans = len(loan_costs)
# Print the number of loans from the list
print(f"The total number of loans in the list: {total_number_of_loans}")


#Calculate the total of loans in the list.
total_value_of_loans = sum(loan_costs)
# Print the sum of all loans from the list
print(f"The sum of all loans in the list: ${total_value_of_loans}")


#define function the calculate the average of two numbers
def calculate_average(number_one, number_two):
    return number_one/number_two

#Calculate the average loan amount
average_loan_amount = calculate_average(total_value_of_loans,total_number_of_loans)
# Print the average loan amount of all loans from the list
print(f"The average loan amount of loans in the list: ${average_loan_amount}")


"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!
#get the value of 'future_value'from the dictionary. Return 0 if trhe value is not there
future_value = loan.get("future_value",0)
#print the value of future_value
print(f"The fair value of the loan: ${future_value}")

#get the value of 'remaining_months'from the dictionary. Return 0 if trhe value is not there
remaining_months = loan.get("remaining_months",0)
#print the value of remaining_months
print(f"The remaining months on the loan: {remaining_months} months")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
# YOUR CODE HERE!

#define gloabl varaible for the discount
discount_rate = .20

#define a generic function to calculate the preent value of a loan based on the values of passed into the
#function including the value of the discountrate parameter.
def calculate_present_value(futureValue,remainingMonths,discountRate):
    return futureValue / (1 + discountRate) ** remainingMonths

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

#Adjust the discount rate to force the use the use of the **monthly** version of the present value formula.
fair_value_discount_rate = discount_rate /12

fair_value = calculate_present_value(future_value,remaining_months, fair_value_discount_rate)
print (f"The fair value of the loan is: ${fair_value:.2f}")
#if present_value >= 

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

#define the annual discount rate and assign it to the value of the global discount_rate valiable .20
annual_discount_rate = discount_rate

"""
# call the previouly defined function for "calculate_present_value" passing in values from the remaining_months and future_value on the new_loan dictionary. 
# Using the # global value for the present value give us a calulation on an annual based discount_rate
"""
# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!
annual_discount_rate = discount_rate
present_value = calculate_present_value(new_loan.get("future_value"),new_loan.get("remaining_months"),annual_discount_rate)
print(f"The present value of the loan is: {present_value:.2f}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""


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

#Create an empty list called that will contain the inexpensive loans
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

# loop through the list of loans
for loan in loans:
    #check each loan in the list and see if the loan price is less than or equal to $500
    #if so add that loan to the inexpensive loan list
    if loan["loan_price"] <=500:
        inexpensive_loans.append(loan)

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!
print(f"The following loans have been added to the inexpensive loans list {inexpensive_loans}")


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
