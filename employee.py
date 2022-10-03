# can change the way the billie, charlie, renee, jan, robbie, and ariel objects are constructed
# can construct additional objects or objects or different types
# the total pay MUST be calculated from the parameters provided using the formulae explained
# can NOT add arguments to the get_pay and the __str__ methods


# ----------------------------------------------------   

class Employee:
    def __init__(self, name, commission_type = None, number_of_contracts = 0):
        self.name = name
        self.commissionType = commission_type #bonus/contract
		self.numberOfContracts = number_of_contracts # for contract commisions
        

# depends the type of contract they have and what they have done in the past month
    def get_pay(self):
        pass
    
# produce a string explaining how the pay has been calculated.
    def __str__(self):
        return self.name
 

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 300, )

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie')     

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel')

# ----------------------------------------------------   

class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(self, name)
        self.salary = salry
        
        
        
        # depends the type of contract they have and what they have done in the past month
        def get_pay(self):
			totalPay = salry
			if (commission_type != None && number_of_contracts != 0)
            	totalPay += 

        # produce a string explaining how the pay has been calculated.
        def __str__(self):
            return self.name
		
# ----------------------------------------------------   
        
class HourlyEmployee(Employee):
    def __init__(self, name, wage, hours):
        super().__init__(self, name)
        self.wage = wage
        
        
        # depends the type of contract they have and what they have done in the past month
        def get_pay(self):
            totalPay =  (self.wage * self.hours) + 

        # produce a string explaining how the pay has been calculated.
        def __str__(self):
            return self.name
        
