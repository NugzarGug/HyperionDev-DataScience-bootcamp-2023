import math
#Asks user about the type of calculation he needs
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

choise = input("""\nEnter either "investment" or "bond" from the menu above to proceed:""")
#Asks user about data for calculation investment
choise = choise.lower()
if choise == "investment":
    amount_money = float(input("Please enter amount of the money in xx.xx format: \n"))
    interest_rate = float(input("Please enter the interest rate: \n"))
    interest_rate = interest_rate / 100
    number_of_years = int(input("Please enter numbers of the years: \n"))
    #Asks user about simple or compound interest rate he needs
    interest = input("""\nPlease enter "simple" or "compound" interest rate ? \n""")
    interest = interest.lower()
    #Calculates and displays simple interest rate
    if interest == "simple":
        simple_interest = amount_money*(1+(interest_rate*number_of_years))
        simple_interest = round(simple_interest)
        print("Full amount with simple interest will be: ",simple_interest)
    #Calculates and displays compound interest rate
    elif interest == "compound":
        compound_interest = amount_money*math.pow((1+interest_rate),number_of_years)
        compound_interest = round(compound_interest)
        print("Full amount with compound interest rate will be: ",compound_interest)
    #Prints the message if user enter wrong choice
    else:
        print("You entered the wrong choice !!!")
    #Asks user about data for bond calculations
elif choise == "bond":
    house_value = int(input("Please enter the value of the house: \n"))
    house_rate = float(input("Please enter interest rate: \n"))
    number_of_months = int(input("Plese enter number of months you plan to take to repay bond: \n"))
    #Calculates and displays bond repayment amount for each month
    house_rate = house_rate / 100 /12
    repayment = (house_rate*house_value)/(1-(1+house_rate)**(-number_of_months))
    repayment = round(repayment)
    print("Each month you will need to repay: ",repayment)
#Prints the message if user enter wrong choice
else:
    print("You entered the wrong choice !!!")
