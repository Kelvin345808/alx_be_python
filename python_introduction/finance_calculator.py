# prompt the user for their monthly income 
monthly_income = float(input("enter your monthly income:")) 

#prompt the user for their total monthly expenses 
monthly_expenses = float(input("enter your total monthly expenses:")) 

# calculate monthly savings 
monthly_savings = monthly_income - monthly_expenses 

# project annual savings with a 5% interest rate 
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) 

# output results 
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")