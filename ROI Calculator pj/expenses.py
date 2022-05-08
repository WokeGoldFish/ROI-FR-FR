class Expenses():
    def __init__(self, expenses):
        self.expenses = {}

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
        if x not in self.expenses:
            print('Invalid input')
        else:
            del self.expenses[x]

    def totalExpenses(self):
        print(f'Your monthly net Expenses are ${sum(self.expenses.values())}')

    def myExpenses(self):
        choice = input('Add / Show / Remove or Quit')
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

            choice = input('Add / Show / Remove or Quit')
            choice = choice.lower()
        self.totalExpenses()
        return


c1 = Expenses(10)
c1.myExpenses()