class ROI():
    '''
    This is for when you know the exact Yearly income and expenses for your properties
    
    '''
    def __init__(self, income, expense, investment):
        self.income = income
        self.expense = expense
        self.investment = investment
    
    def myROI(self):
        x = self.income
        y = self.expense
        z = self.investment
        
        totalROI = (x-y)*12/z * 100
        print(f'The ROI for this property is {totalROI}%')\
    
    
c2 = ROI(2000, 1610, 50000)
c2.myROI()
        
        