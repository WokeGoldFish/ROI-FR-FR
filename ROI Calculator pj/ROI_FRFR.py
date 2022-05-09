class CashOnCash():
    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.investment = {}

    def addIncome(self):
        source = input('Income Source:')
        amount = int(input('Enter Amount:'))
        if source not in self.income:
            self.income[source] = amount

    def showIncome(self):
        print('Here is your income sources from this property:')
        for x in self.income:
            print(x, self.income[x])

    def removeIncome(self):
        x = input('What income source would you like to remove?')
        x = x.lower()
        if x not in self.income:
            print('Invalid input')
        else:
            del self.income[x]

    def totalIncome(self):
        total = sum(self.income.values())
        
        return total

    def myIncome(self):
        choice = input('Income - Add / Show / Remove or Quit')
        choice = choice.lower()

        while choice != 'quit':
            
            if choice == 'add':
                self.addIncome()
            elif choice == 'show':
                self.showIncome()
            elif choice == 'remove':
                self.removeIncome()
            elif choice != 'quit':
                print('Invalid input !!!')
                
            choice = input('Add / Show / Remove or Quit')
            choice = choice.lower()
        total = self.totalIncome()
        print(f'Your monthly net income is ${total}')
        return
## expenses
    def addExpenses(self):
        source = input('Expenses:')
        amount = int(input('Enter Amount:'))
        if source not in self.expenses:
            self.expenses[source] = amount

    def showExpenses(self):
        print('Here is your income sources from this property:')
        for x in self.expenses:
            print(x, self.expenses[x])

    def removeExpenses(self):
        x = input('What expense source would you like to remove?')
        x = x.lower()
        if x not in self.expenses:
            print('Invalid input')
        else:
            del self.expenses[x]

    def totalExpenses(self):
        total =  sum(self.expenses.values())
        return total 
        
    def myExpenses(self):
        choice = input('Expenses -- Add / Show / Remove or Quit:')
        choice = choice.lower()

        while choice != 'quit':

            if choice == 'add':
                self.addExpenses()
            elif choice == 'show':
                self.showExpenses()
            elif choice == 'remove':
                self.removeExpenses()
            elif choice != 'quit':
                print('Invalid input !!!')

            choice = input('Add / Show / Remove or Quit:')
            choice = choice.lower()
        total = self.totalExpenses()
        print(f'Your monthly net Expenses are ${total}')
        return

## investment

    def addInvestment(self):
        source = input('Investment:')
        amount = int(input('Enter Amount:'))
        if source not in self.investment:
            self.investment[source] = amount
            
    def showInvestment(self):
        print('Investment into property:')
        for x in self.investment:
            print(x, self.investment[x])
            
    def removeInvestment(self):
        x = input('What invesment sink would you like to remove?')
        x = x.lower()
        if x not in self.investment:
            print('Invalid input')
        else:
            del self.investment[x]
            
    def totalInvestment(self):
        total =  sum(self.investment.values())
        return total
    
    def myInvestment(self):
        choice = input('Investment -- Add / Show / Remove or Quit:')
        choice = choice.lower()

        while choice != 'quit':

            if choice == 'add':
                self.addInvestment()
            elif choice == 'show':
                self.showInvestment()
            elif choice == 'remove':
                self.removeInvestment()
            elif choice != 'quit':
                print('Invalid input !!!')

            choice = input('Add / Show / Remove or Quit:')
            choice = choice.lower()
        total = self.totalInvestment()
        print(f'Total investment is ${total}')
        return
    
    
    
    
    
    def cashFlow(self):
        netProfit = self.totalIncome() - self.totalExpenses()
        print(f'Your cashflow is ${netProfit} per month')
        print(f'${netProfit*12} per year')
        return netProfit
        
    
    def ROI(self):
        myROI = self.cashFlow()*12/self.totalInvestment() * 100
        print(f'Cash on Cash ROI for this property is {myROI}%')
        return myROI
        
        
    
    
    
    
c1 = CashOnCash()
c1.myIncome()
c1.myExpenses()
c1.myInvestment()
c1.cashFlow()
c1.ROI()
