class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, title, description, amount):
        expense = {
            'date': date,
            'title': title,
            'description': description,
            'amount': amount
        }
        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses
