from datetime import datetime, timezone
from uuid import uuid4
from datetime import datetime

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
                "updated_at":self.updated_at.isoformat(),



# implementation for user input processing 

