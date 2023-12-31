from time import sleep
from tabulate import tabulate

class Roi_Calculator:

    def __init__(self, income=0, expenses=0, monthly_cash_flow=0, annual_cash_flow=0, total_investment=0, roi=0 ):
        self.income = income
        self.expenses = expenses
        self.monthly_cash_flow = monthly_cash_flow
        self.annual_cash_flow = annual_cash_flow
        self.total_investment = total_investment
        self.roi = roi
        self.box_char = '='
        self.table = None


    def add_income(self):
        # Ask user to provide all of their income sources. Calculate and print total.
        while True:
            rental_input = input("\nWhat is your Monthly Rental Income?\n\t")
            try:
                rental = int(rental_input)
                break # Break the loop if conversion to int is successful
            except ValueError:
                print('\nPlease only enter a number. \n\t')
        other_income = input("\nDo you receive any Monthly Income from Laundry, Storage or Miscellaneous? (yes or no)\n\t").lower()
        laundry, storage, misc = 0, 0, 0
        while other_income not in ['yes', 'no']:
            other_income = input('\nPlease only type "yes" or "no"\n\t').lower()
        if other_income == 'yes':
            while True:
                laundry_input = input('\nWhat is your Monthly Laundry Income?\n\t')
                storage_input = input('\nWhat is your Monthly Storage Income?\n\t')
                misc_input = input('\nWhat is your Monthly Miscellaneous Income?\n\t')
                try:
                    laundry = int(laundry_input)
                    storage = int(storage_input)
                    misc = int(misc_input)
                    break # Break the loop if conversion to int is successful
                except ValueError:
                    print('\nPlease only enter a number for each question.')

        self.income = sum([rental, laundry, storage, misc])
        total_income_string = f"Total Income: ${self.income}"
        print(self.box_char*(len(total_income_string)+4))
        print(total_income_string)
        print(self.box_char*(len(total_income_string)+4))
        sleep(2)

    def add_expenses(self):
        # Ask user to provide all expenses. Calculate and print total.
        while True:
            taxes_input = input("\nWhat are your Monthly Tax Expenses?\n\t")
            insurance_input = input("\nWhat are your Monthly Insurance Expenses?\n\t")
            try:
                taxes = int(taxes_input)
                insurance = int(insurance_input)
                break
            except ValueError:
                print('\nPlease only enter a number for each question.')
        utilities_expenses = input("\nDo you have Utilities Expenses? (yes or no)\n\t").lower()
        electric, water, sewage, garbage, gas = 0, 0, 0, 0, 0
        while utilities_expenses not in ['yes', 'no']:
            utilities_expenses = input('\nPlease only type "yes" or "no"\n\t').lower()
        if utilities_expenses == 'yes':
            while True:
                electric_input = input('\nWhat is your Monthly Electric Expense?:\n\t')
                water_input = input('\nWhat is your Monthly Water Expense?:\n\t')
                sewage_input = input('\nWhat is your Monthly Sewage Expense?:\n\t')
                garbage_input = input('\nWhat is your Monthly Garbage Expense?:\n\t')
                gas_input = input('\nWhat is your Monthly Gas Expense?:\n\t')
                try:
                    electric = int(electric_input)
                    water = int(water_input)
                    sewage = int(sewage_input)
                    garbage = int(garbage_input)
                    gas = int(gas_input)
                    break # Break the loop if conversion to int is successful
                except ValueError:
                    print('\nPlease only enter a number for each question.')
        
        utilites = sum([electric, water, sewage, garbage, gas])
        
        misc_expenses = input("\nDo you have Monthly HOA, Lawn/Snow, or Vacancy Expenses? (yes or no)\n\t").lower()
        hoa, lawn_or_snow, vacancy = 0, 0, 0
        while misc_expenses not in ['yes', 'no']:
            misc_expenses = input('\nPlease only type "yes" or "no"\n\t').lower()
        if misc_expenses == 'yes':
            while True:
                hoa_input = input('\nWhat is your Monthly HOA Expense?:\n\t')
                lawn_or_snow_input = input('\nWhat is your Monthly Lawn/Snow Maintenance Expense?:\n\t')
                vacancy_input = input('\nWhat is your Monthly Vacancy Expense?:\n\t')
                try:
                    hoa = int(hoa_input)
                    lawn_or_snow = int(lawn_or_snow_input)
                    vacancy = int(vacancy_input)
                    break # Break the loop if conversion to int is successful
                except ValueError:
                    print('\nPlease only enter a number for each question.')
        
        misc = sum([hoa, lawn_or_snow, vacancy])
        
        general_expenses = input("\nDo you have Monthly Repair, Capital, or Property Management Expenditures? (yes or no)\n\t").lower()
        repairs, cap_ex, property_mgmt = 0, 0, 0
        while general_expenses not in ['yes', 'no']:
            general_expenses = input('\nPlease only type "yes" or "no"\n\t').lower()
        if general_expenses == 'yes':
            while True:
                repairs_input = input('\nWhat is your Monthly Repairs Expense?:\n\t')
                cap_ex_input = input('\nWhat are your Monthly Capital Expenditures?:\n\t')
                property_mgmt_input = input('\nWhat is your Monthly Property Management Expense?:\n\t')
                try:
                    repairs = int(repairs_input)
                    cap_ex = int(cap_ex_input)
                    property_mgmt = int(property_mgmt_input)
                    break # Break the loop if conversion to int is successful
                except ValueError:
                    print('\nPlease only enter a number for each question.')
        
        general = sum([repairs, cap_ex, property_mgmt])
        
        mortgage = input("\nDo you have a Mortgage on this property? (yes or no)\n\t")
        mortgage_pmt = 0
        while mortgage not in ['yes', 'no']:
            mortgage = input('\nPlease only type "yes" or "no" \n\t').lower()
        if mortgage == 'yes':
            while True:
                mortgage_input = input('\nHow much is your Monthly Morgage?:\n\t')
                try:
                    mortgage_pmt = int(mortgage_input)
                    break # Break the loop if conversion to int is successful
                except ValueError:
                    print('\nPlease only enter a number for each question')
        
        self.expenses = sum([taxes, insurance, utilites, misc, general, mortgage_pmt])
        total_expenses_string = f"Total Expenses: ${self.expenses}"
        print(self.box_char*(len(total_expenses_string)+4))
        print(total_expenses_string)
        print(self.box_char*(len(total_expenses_string)+4))
        sleep(2)

    def cash_flow(self):
        self.monthly_cash_flow = self.income - self.expenses
        self.annual_cash_flow = self.monthly_cash_flow * 12
        cash_flow_string = f"Monthly Cash Flow: ${self.monthly_cash_flow} Annual Cash Flow: ${self.annual_cash_flow}"
        print(self.box_char*(len(cash_flow_string)+4))
        print(cash_flow_string)
        print(self.box_char*(len(cash_flow_string)+4))
        sleep(2)

    def add_investments(self):
        while True:
            down_payment_input = input("\nHow much was your Down Payment for this property?:\n\t")
            try:
                down_payment = int(down_payment_input)
                break
            except ValueError:
                print('\nPlease only enter a number.')
        while True:
            closing_costs_input = input("\nWhat were your Closing Costs?:\n\t")
            try:
                closing_costs = int(closing_costs_input)
                break
            except ValueError:
                print('\nPlease only enter a number.')
        while True:
            rehab_input = input("\nHow much was your Rehabilitation Budget?:\n\t")
            try:
                rehab = int(rehab_input)
                break
            except ValueError:
                print('\nPlease only enter a number.')
        while True:
            misc_input = input("\nAnd finally, how much were your Miscellaneous Investments?:\n\t")
            try:
                misc = int(misc_input)
                break
            except ValueError:
                print('\nPlease only enter a number.')
        
        self.total_investment = sum([down_payment, closing_costs, rehab, misc])
        total_investment_string = f"Total Investments: ${self.total_investment}"
        print(self.box_char*(len(total_investment_string)+4))
        print(total_investment_string)
        print(self.box_char*(len(total_investment_string)+4))
        sleep(2)

    def view_all(self):
        self.table = [["Total Income:",f"${self.income}"], ["Total Expenses:",f"${self.expenses}"], ["Total Investments:",f"${self.total_investment}"], ["Monthly Cash Flow:",f"${self.monthly_cash_flow}"], ["Annual Cash Flow:",f"${self.annual_cash_flow}"]]
        print(tabulate(self.table))
        print(self.roi_string)
        print(self.box_char*(len(self.roi_string)+4))
        print(self.box_char*(len(self.roi_string)+4))

    def calculate_roi(self):
        self.roi = self.annual_cash_flow / self.total_investment
        self.roi_string = f"Total Cash-on-Cash ROI: {round(self.roi * 100, 2)}%"
        self.view_all()

    def edit_answers(self, choice):
        if choice == 'income':
            self.add_income()
            self.cash_flow_update()
        elif choice == 'expenses':
            self.add_expenses()
            self.cash_flow_update()
        elif choice == 'investments':
            self.add_investments()
        self.calculate_roi()

    def cash_flow_update(self):
        self.monthly_cash_flow = self.income - self.expenses
        self.annual_cash_flow = self.monthly_cash_flow * 12

def run_calc():
    roi = Roi_Calculator()
    welc = "Hello There!\nWith this ROI Calculator, you can determine the Cash-On-Cash ROI of your Rental Properties."
    welc2 = "\nFor Starters, we'll need to calculate your Monthly Income."
    print(roi.box_char*(len(welc)+4))
    print( welc)
    print(roi.box_char*(len(welc)+4))
    sleep(4)
    print(welc2)
    roi.add_income()
    print("\nGreat! Now that we have your Income, we'll need to determine your total Monthly Expenditures.\n")
    sleep(2)
    roi.add_expenses()
    roi.cash_flow()
    print("\nNow let's take a look at your total investment in this property.\n")
    sleep(2)
    roi.add_investments()
    roi.calculate_roi()
    ending_answers = ['edit', 'view', 'quit']
    while True:
        ending_input = input("\nWhat would you like to do now? (Edit / View / Quit)\n\t").lower()
        
        while ending_input not in ending_answers:
            ending_input = input('Please only type in "Edit", "View" or "Quit"\n\t').lower()
        if ending_input == 'quit':
            print(roi.box_char*51)
            sleep(0.75)
            print("\nThanks for using our Cash-on-Cash ROI Calculator!")
            break
        elif ending_input == 'edit':
            edit_answers = ['income', 'expenses', 'investments']
            edit_input = input('What would you like to edit? (Income / Expenses / Investments)\n\t').lower()
            while edit_input not in edit_answers:
                edit_input = input('Please only type in "Income", "Expenses", or "Investments"\n\t').lower()
            roi.edit_answers(edit_input)
        elif ending_input == 'view':
            roi.view_all()


run_calc()

















# Income Sources: - Box 1
# Rental Income, Laundry Income (laundry machine), Storage income, Misc Income
# Rental income is the primary source of income with rental properties

# EX Income Breakdown:
# Rental Income = $2,000 per month
# Laundry = $0
# Storage = $0
# Misc = $0

# Total Monthly Income = $2,000


# Expenses: - Box 2
# Taxes, Insurance, Utilities (electric, water, sewer, garbage, gas),
# HOA fees, Lawn/Snow Care, Vacancy, Repairs, CapEx (Capital Expenditures), 
# Property Management Fees, Mortgage

# EX Expenses Breakdown:
# Taxes = $150 per month
# Insurance = $100 per month
# Utilites = $0
# HOA = $0
# Lawn/snow removal = $0
# Vacancy = $100 per month
# Repairs = $100 per month
# CapEx = $100 per month
# Property Manage = $200 per month
# Mortgage = $860 per month

# Total Monthly Expenses = $1610


# Cash Flow - Box 3
# Income - Expenses

# EX Cash Flow Breakdown:
# $2,000 per month in Income - $1,610 in Expenses

# Total Monthly Cash Flow = $390


# Cash on Cash ROI - Box 4
# Return on your cash flow

# Start by adding up all the money we put into this:
# Down payment, closing costs, rehab budget, misc/other

# EX Cash on Cash ROI breakdown:
# Down payment: $40,000
# Closing Costs: $3,000
# Rehab budget: $7,000
# Misc other: $0

# Total Investment: $50,000

# Now, find Annual Cash Flow:
# $390 * 12 = $4,680
# Annual Cash Flow / Total Investment

# $4,680 / $50,000 = 9.36%

# Cash on Cash ROI = 9.36%