def calculate_simple_interest(principal,rate,time):
    interest=(principal*rate*time)/100
    return interest
def calculate_compound_interest(principal,rate,time,compounds_per_year):
    amount=principal*(1+rate/(compounds_per_year*100))**(compounds_per_year*time)
    interest = amount-principal
    return interest
def main():
    principal_amount=float(input("Enter the principal amount: "))
    interest_rate = float(input("Enter the annual interest rate (in percentage): "))
    time_period = float(input("Enter the number of times interest is compunded per year: "))
    compounds_per_year = int(input("Enter the number of times interest is compunded per year: "))
    simple_interest = calculate_simple_interest(principal_amount,interest_rate,time_period)
    compound_interest = calculate_compound_interest(principal_amount,interest_rate,time_period,compounds_per_year)
    print("\nSimple Interest: ",round(simple_interest,2))
    print("Compound Interest: ",round(compound_interest,2))
if __name__ == "__main__":
    main()