print("Welcome to Izifin Technology,We are here to help you calculate your ATR with just few informations")
years_of_experience = int(input("Enter your years of experiience please:"))
age = int(input("Enter your age please:"))

if  years_of_experience > 25 and age >= 55:
     Annual_tax_revenue = 5600000
elif years_of_experience > 20 and age >= 45:
    Annual_tax_revenue = 4480000

elif years_of_experience >10 and age >=35:
    Annual_tax_revenue = 1500000
else: 
     Annual_tax_revenue = 550000
print(f"staff with {years_of_experience} years of experience and is {age} years of age has N{Annual_tax_revenue} Annual tax revenue")