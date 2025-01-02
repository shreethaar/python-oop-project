from datetime import datetime, timezone
from uuid import uuid4
from abc import ABC, abstractmethod

class Expense:
    def __init__(self,title,amount) -> None:
        self.id=str(uuid4())
        self.title=str(title)
        self.amount=float(amount)
        self.created_at=datetime.now(timezone.utc)
        self.update_at=self.created_at

    def update_expense(self,title=None,amount=None):
        if title is not None:
            print(f"Updating title to: {title}")
            self.title=title
        if amount is not None:
            print(f"Updating amount to: {amount}")
            self.amount=amount
        if title is None and amount is None:
            print("No updates were made.")
        self.update_at=datetime.now(timezone.utc)

    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "amount":self.amount,
            "created_at":self.created_at.isoformat(),
            "updated_at":self.updated_at.isoformat()
        }

class ExpenseDataBase:
    def __init__(self):
        self.expenses=[]

    def add_expense(self,expense):
        self.expenses.append(expense)
        print(f"Expense with ID {expense.id} added successfully")
        return expense

    def remove_expense(self,expense_id):
        self.expenses=[expense for expense in self.expenses if expense.id != expense_id]
        print(f"Expense with ID {expense_id} has been removed")
    
    def get_expense_by_id(self, expense_id):
        expense = [expense for expense in self.expenses if expense.id == expense_id]
        if len(expense) == 0:
            return None
        return expense[0]
    
    def get_expense_by_title(self, expense_title):
        similar_expenses = [expense for expense in self.expenses if expense.title == expense_title]
        return similar_expenses.copy() 

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]

class 


# implementation for user input processing 
    def main():
        print("$$Python Expense Tracker$$")
        user_name=input("Enter your name:")
        days_expense_track=int(input("Enter the number of days to record expenses:"))

        expense_db=ExpenseDataBase()



if __name__ == "__main__":

