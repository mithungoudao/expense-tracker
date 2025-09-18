import sqlite3
from typing import List, Dict


class DBHandler:
    def __init__(self, db_path: str = "expenses.db"):
        self.db_path = db_path
        self._ensure_connection()

    def _ensure_connection(self):
        # connection per operation is safe for simple apps; keep helper method
        pass

    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        description TEXT
        );
        """
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        finally:
            conn.close()    

    def insert_expense(self, expense) -> int:
        query = "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?);"
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(query, (expense.date, expense.category, expense.amount, expense.description))
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()

    def fetch_all(self) -> List[Dict]:
        query = "SELECT id, date, category, amount, description FROM expenses ORDER BY id DESC;"
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return [dict(row) for row in rows]
        finally:
            conn.close()

    def update_expense(self, expense_id: int, expense) -> bool:
        query = "UPDATE expenses SET date = ?, category = ?, amount = ?, description = ? WHERE id = ?;"
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(query, (expense.date, expense.category, expense.amount, expense.description, expense_id))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()

    def delete_expense(self, expense_id: int) -> bool:
        query = "DELETE FROM expenses WHERE id = ?;"
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(query, (expense_id,))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()

    def totals_by_category(self):
        query = "SELECT category, SUM(amount) as total FROM expenses GROUP BY category;"
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            return {row["category"]: row["total"] for row in rows}
        finally:
            conn.close()