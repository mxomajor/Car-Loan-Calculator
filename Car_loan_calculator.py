def car_finance_calculator():
    print("Welcome to the Car Finance Calculator!")
    
    # Gather user details and inputs
    user_name = input("Please enter your name: ")
    loan_amount = float(input("Hi, {}! Enter the total loan amount (in your currency): ".format(user_name)))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    loan_term_years = int(input("Enter the loan term (in years): "))
    
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    
    # Calculate the total number of payments (months)
    total_payments = loan_term_years * 12
    
    # Calculate the monthly payment using the formula
    # M = P[r(1+r)^n] / [(1+r)^n - 1]
    if monthly_interest_rate == 0:  # Handle zero-interest loans
        monthly_payment = loan_amount / total_payments
    else:
        numerator = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments
        denominator = (1 + monthly_interest_rate) ** total_payments - 1
        monthly_payment = numerator / denominator
    
    # Display the result
    print(f"\nThank you, {user_name}. Here are your loan details:")
    print(f"Loan Amount: {loan_amount:.2f}")
    print(f"Annual Interest Rate: {annual_interest_rate:.2f}%")
    print(f"Loan Term: {loan_term_years} years")
    print(f"Your monthly payment will be: {monthly_payment:.2f}")
    
    # Optional: Total payment and interest
    total_payment = monthly_payment * total_payments
    total_interest = total_payment - loan_amount
    print(f"Total payment over the loan period: {total_payment:.2f}")
    print(f"Total interest paid: {total_interest:.2f}")

# Run the calculator
car_finance_calculator()

