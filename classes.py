import math
import os
import time
class roiProperty():

    inputs_exp = ('Property Tax', 'Property Insurance', 'Vacancy Costs', 'Prop Repairs', 'Capex', 'Prop Managment', 'Mortgage Payment')


    def __init__(self,name, cost_prop, expenses):
        self.name = name
        self.cost_prop = cost_prop
        self.expenses = expenses

    
    def valueProp(self):
        os.system('clear')
        print(f'\n{self.name}, you said your propert costs $ {self.cost_prop:,.2f}\n\n')
        print(f'I will ask you about your downpayment later on....\n\n')
        time.sleep(3)
        # property_cost = float(input('\n\nPlease enter the listing price of the porperty\n--> '))
        # self.property_cost = property_cost
        roiProperty.rentalIncome(self)
        time.sleep(1)





    def rentalIncome(self):
        os.system('clear')
        print(f"\n\nLet's start with your Icome from the property !!\n\n".center(150))
        rent_income = float(input('\n\nPlease enter the total rental income for the porperty\n--> '))
        print(f'\nYou said your rental income is $ {rent_income:,.2f}\n')
        self.rent_income = rent_income
        time.sleep(3)
        roiProperty.totExpenses(self)
        


    def totExpenses(self):
        os.system('clear')
        prop_dict = dict.fromkeys(roiProperty.inputs_exp)
        print(f"\n\nNow let's look into your expenses.... \n\n".center(150))
        prop_tax = round(((0.01 * self.cost_prop) / 12), 2)
        prop_dict['Property Tax'] = prop_tax
        time.sleep(2)
        os.system('clear')
        print(f'\n\nProperty tax is 1% of your home value, which in this case monthly is :\n\n Tax : {prop_tax:.2f}')
        prop_ins = 100.00
        prop_dict['Property Insurance'] = prop_ins
        time.sleep(4)
        os.system('clear')
        print(f'\n\nProperty insurance on an monthly basis is aprox $ {prop_ins:,.2f}')
        vacancy = round((self.rent_income * 0.05), 2)
        round(vacancy, 2)
        prop_dict['Vacancy Costs'] = vacancy
        time.sleep(4)
        os.system('clear')
        print(f'\n\nProperty vacancy cost  is aprox 5% of your the rent monthly: $ {vacancy:,.2f}')
        repairs = 100.00 
        prop_dict['Prop Repairs'] = repairs
        time.sleep(4)
        os.system('clear')
        print(f'\n\nProperty repairs on an monthly basis is aprox $ {repairs:,.2f}')
        capex = 100.00
        prop_dict['Capex'] = capex
        time.sleep(4)
        os.system('clear')
        print(f'\n\nProperty Capex on an monthly basis is aprox $ {capex:,.2f}')
        prop_mang = round((self.rent_income * 0.10), 2)
        round(prop_mang, 2)
        prop_dict['Prop Managment'] = prop_mang
        time.sleep(4)
        os.system('clear')
        print(f'\n\nProperty managment costs on an monthly basis is aprox 10% of your monthly rental income = $ {prop_mang:,.2f}')
        time.sleep(4)
        os.system('clear')
        mortg_paym = float(input(f'\n\nWhat is your aprox mortgage payment ? \n --> '))
        print(f'{self.name}, you said your mortgage alone is $ {mortg_paym:,.2f}')
        round(mortg_paym, 2)
        prop_dict['Mortgage Payment'] = mortg_paym
        time.sleep(4)
        os.system('clear')
        print(f"\n\nAs for expenses, this is what you entered : \n\n")
        for x, y in prop_dict.items():
            print(x, y)
        time.sleep(6)
        print('\n\n\n')
        total_sum_exp = sum(prop_dict.values())
        print(f"\nAnd the total monthly expenses for your property is : {total_sum_exp}")
        self.total_sum_exp = total_sum_exp
        time.sleep(3)
        roiProperty.cashFlow(self)

    
    def cashFlow(self):
        os.system('clear')
        print(f"\n\nLet's look at your cash flow....\n\n".center(150))
        print(f"Your monthly income is : $ {self.rent_income} \n")
        print(f"\n\nYour monthly expenses are : $ {self.total_sum_exp} \n")
        cash_flow = self.rent_income - self.total_sum_exp
        print(f"\n\n\nYour current cash flow is : $ {cash_flow:,.2f}")
        self.cash_flow = cash_flow
        time.sleep(4)
        roiProperty.cocRoi(self)

    
    def cocRoi(self):
        os.system('clear')
        down_pay = float(input('\n\nHow much is the downpayment in this property ? \n\n --> '))
        closing = float(input(f"What are the closing costs in this property ? \n\n -->"))
        rep_budg = float(input(f"What ids the repair budget for this property ? \n\n -->"))
        misc = float(input(f"What are the miscellaneous exepenses for this property ? \n\n -->"))
        time.sleep(2)
        os.system('clear')
        tot_invs = down_pay + closing + rep_budg + misc
        print(f"\n\nYour Total Investment for the property is : $ {tot_invs:,.2f}".center(150))
        print('\n\n\n')
        ann_cash_flow = ((self.cash_flow * 12) / tot_invs) * 100
        time.sleep(3)
        os.system('clear')
        print(f'\n\nYOUR RETURN-ON-INVESTMENT FOR THIS PROPERTY IS : {ann_cash_flow:.2f}%')
        time.sleep(4)
        print(f'\n\n\n\n\n\n GOOOOOOOD BYE!!!!!!!!!'.center(150))
        quit()

        
        