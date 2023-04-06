import time
#GDS = All housing payments per month / all income per month

def Income():
	print(f"\n\n APPLICANTS \n")
	Incomes = input(f"\nHow do you recieve your income?: (Jobs, SE, Pension) \n")
	
	global monthly_income
	global monthly_income2
	global Self_Emp
	global Pension
	
	monthly_income = 0
	monthly_income2 = 0
	Self_Emp = 0
	Pension = 0
	
	if Incomes == 'Jobs':
		Job_Amount = input(f"\nHow many jobs do you have?: \n")
		if Job_Amount == '1':
			salary = float(input(f"\nWhat is your salary from this job?: \n$"))
			monthly_income = salary/12
			Math()
		elif Job_Amount == '2':
			salary = float(input(f"\nWhat is your salary from your first job?: \n$"))
			salary2 = float(input(f"\nWhat is your salary from your second job?: \n$"))
			monthly_income = salary/12
			monthly_income2 = salary2/12
			Math()
		else:
			print("Sorry, I didn't understand")

	elif Incomes == 'SE':
		Self_Emp = float(input(f"\nHow much do you earn through self emplyment?: \n$"))
		Math()

	elif Incomes == 'Pension':
		Pension = float(input(f"\nHow much do you earn through your pension plan?: \n$"))
		Math()

	else:
		print("I didn't understand")
		time.sleep(1)
		pass


def Loans():
	global Liabilities
	Liabilities = 0
	
	car_loan = float(input(f"How much do you pay in Car Loans monthly?: \n$"))
	personal_loan = float(input(f"How much do you pay in Personal Loans monthly?: \n$"))
	other_loans = float(input(f"How much do you pay in other loans monthly?: \n$"))
	
	Liabilities = car_loan + personal_loan + other_loans
	
	Income()


def Primary():
	global All_Properties
	All_Properties = 0

	PandI = float(input(f"What is your principal + interest monthly on your residence?: \n$"))
	Tax = float(input(f"\nHow much tax do you pay on this residence?: \n$"))
	HeatingFees = float(input(f"\nHow much do you pay on heating and air conditioning monthly?: \n$"))
	CondoFees = float(input(f"\nHow much do you pay in condo fees monthly?: \n$"))
	Mortgage = float(input(f"\nHow much mortgage do you pay?: \n$"))
	
	All_Properties = PandI + Tax + HeatingFees + CondoFees + Mortgage
	
	ExProp = input(f"\nDo you own any extra properties? (y/n)\n")
	if ExProp == 'y':
		print(f"\n")
		pass
	elif ExProp == 'n':
		Loans()
	else:
		print("Sorry I didn't understand")


def Math():
	All_Income = monthly_income + monthly_income2 + Self_Emp + Pension
	
	GDS = round((All_Properties / All_Income) * 100, 2)
	print(f"\nThe GDS is {GDS}%")
	
	TDS = round(((All_Properties + Liabilities) / All_Income) * 100, 2)
	print(f"\nThe TDS is {TDS}%")


Primary()
