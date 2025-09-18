from dataclasses import dataclass
from typing import List, Optional
from .db_handler import DBHandler


@dataclass
class Expense:
    id: Optional[int]
    date: str
    category: str
    amount: float
    description: str = ""

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
        }


class ExpenseTracker:
    def __init__(self, db_path: str = "expenses.db"):
        self.db = DBHandler(db_path)
        self.db.create_table()

    # Create
    def add_expense(self, expense: Expense) -> int:
        return self.db.insert_expense(expense)

    # Read
    def list_expenses(self) -> List[Expense]:
        rows = self.db.fetch_all()
        return [Expense(id=row["id"], date=row["date"], category=row["category"], amount=row["amount"], description=row["description"]) for row in rows]

    # Update
    def update_expense(self, expense_id: int, new_expense: Expense) -> bool:
        return self.db.update_expense(expense_id, new_expense)

    # Delete
    def delete_expense(self, expense_id: int) -> bool:
        return self.db.delete_expense(expense_id)

    # Aggregation
    def totals_by_category(self):
        return self.db.totals_by_category()