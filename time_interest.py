def months_to_reach_savings(target_savings, monthly_deposit, annual_interest_rate):
    # Initial savings balance
    savings = 0
    months = 0
    
    # Monthly interest rate (annual interest rate divided by 12)
    monthly_interest_rate = annual_interest_rate / 12
    
    while savings < target_savings:
        # Add monthly deposit
        savings += monthly_deposit
        # Apply compound interest for the month
        savings *= (1 + monthly_interest_rate)
        # Increment the month count
        months += 1
    
    return months

# Given values
annual_salary = 9600000
monthly_salary = annual_salary / 12
monthly_deposit = monthly_salary * 0.15
annual_interest_rate = 0.06
house_price = 80000000
target_savings = house_price * 0.25

# Calculate the number of months to reach the target savings
months_needed = months_to_reach_savings(target_savings, monthly_deposit, annual_interest_rate)

# Output the result
print(f"It will take {months_needed} months to accumulate {target_savings} RWF in savings.")