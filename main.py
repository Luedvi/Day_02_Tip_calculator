#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill_input=input("What was the total bill? $")
tip_input=input("How much tip would you like to give? 10, 12, or 15? ")
split_input=input("How many people to split the bill? ")

bill=float(bill_input)
tip=int(tip_input)/100
split=int(split_input)
individual_amount=bill*(1+tip)/split

print("Each person should pay: $"+format(individual_amount,".2f"))

#bill=float(input("What was the total bill? $"))
#tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
#split=int(input("How many people to split the bill? "))
