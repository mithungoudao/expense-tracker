💰 Expense Tracker (OOP + SQLite + Streamlit)
📌 Overview

This is a simple Expense Tracker web app built in Python.
The goal is to demonstrate:

Object-Oriented Programming (OOP) concepts in Python

CRUD operations (Create, Read, Update, Delete)

Use of SQLite for persistent storage

A clean Streamlit UI for interaction

⚙️ Features

➕ Add new expenses with date, category, amount, and description

📋 View all expenses in a table

✏️ Update existing expenses

❌ Delete expenses

📊 View total expenses by category

Persistent storage using SQLite database (expenses.db)

🧑‍💻 OOP Concepts Used

Encapsulation → Expense details are bundled inside the Expense class

Abstraction → Database logic is hidden in the DBHandler class

Inheritance (extendable) → DBHandler can be swapped with another storage handler (e.g., PostgreSQL)

Polymorphism → The same methods (add_expense, update_expense) work regardless of input details

📂 Project Structure
expense-tracker/
│── app/
│   │── __init__.py
│   │── expense.py        # Expense & ExpenseTracker classes
│   │── db_handler.py     # Handles SQLite database operations
│
│── streamlit_app.py      # Streamlit UI (all CRUD in single page)
│── expenses.db           # SQLite database (auto-created)
│── requirements.txt      # Dependencies
│── README.md             # Project explanation

🚀 How to Run
1️⃣ Clone the repo
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run streamlit_app.py

📊 Example Workflow

Add Expense → 2025-09-19 | Food | 250 | Lunch

Add Expense → 2025-09-19 | Travel | 100 | Auto fare

Table View → Shows both expenses with IDs

Update → Change “250” to “300” for Food

Delete → Remove Travel expense

Totals by Category → Food: ₹300

🔮 Future Improvements

User authentication (multi-user expense tracking)

Advanced reports (monthly charts, category trends)

Export reports to Excel/PDF

Switch storage from SQLite to PostgreSQL/MySQL for scalability

📝 Notes

This project is designed for interview demonstration.

It highlights Python OOP concepts, database handling, and UI integration.

Focus is on clarity, simplicity, and explanation rather than production-scale features.