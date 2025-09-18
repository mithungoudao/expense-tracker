import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date
from app.expense import Expense, ExpenseTracker

st.set_page_config(page_title="Expense Tracker", layout="wide")

tracker = ExpenseTracker(db_path="expenses.db")

st.title("💰 Expense Tracker")
st.markdown("Use the sidebar to add expenses. Update and delete using the controls below.")

# -----------------
# Sidebar: CREATE
# -----------------
st.sidebar.header("➕ Add New Expense")
with st.sidebar.form(key="add_expense_form"):
    d = st.date_input("Date", value=date.today())
    category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
    amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
    description = st.text_input("Description")
    submit = st.form_submit_button("Add Expense")

    if submit:
        exp = Expense(id=None, date=str(d), category=category, amount=float(amount), description=description)
        row_id = tracker.add_expense(exp)
        st.sidebar.success(f"Expense added (id={row_id})")

# -----------------
# READ: show table
# -----------------
st.subheader("📋 All Expenses")
expenses = tracker.list_expenses()
if expenses:
    df = pd.DataFrame([e.to_dict() for e in expenses])
    df = df[["id", "date", "category", "amount", "description"]]
    st.dataframe(df)

    # Totals by category
    st.subheader("📊 Total by Category")
    totals = tracker.totals_by_category()
    if totals:
        total_df = pd.DataFrame(list(totals.items()), columns=["Category", "Total (₹)"])
        st.table(total_df)

else:
    st.info("No expenses recorded yet.")

# -----------------
# UPDATE
# -----------------
st.subheader("✏️ Update Expense")
if expenses:
    ids = [e.id for e in expenses]
    selected_id = st.selectbox("Select Expense ID to update", ids)
    selected_row = next((e for e in expenses if e.id == selected_id), None)
    if selected_row:
        with st.form(key="update_form"):
            new_date = st.date_input("Date", value=pd.to_datetime(selected_row.date).date())
            new_category = st.selectbox(
                "Category",
                ["Food", "Travel", "Shopping", "Bills", "Other"],
                index=["Food", "Travel", "Shopping", "Bills", "Other"].index(selected_row.category)
                if selected_row.category in ["Food", "Travel", "Shopping", "Bills", "Other"]
                else 0,
            )
            new_amount = st.number_input("Amount (₹)", min_value=0.0, value=float(selected_row.amount), format="%.2f")
            new_description = st.text_input("Description", value=selected_row.description)
            update_btn = st.form_submit_button("Update")

            if update_btn:
                new_exp = Expense(id=None, date=str(new_date), category=new_category, amount=float(new_amount), description=new_description)
                ok = tracker.update_expense(selected_id, new_exp)
                if ok:
                    st.success("Expense updated successfully")
                else:
                    st.error("Update failed")

# -----------------
# DELETE
# -----------------
st.subheader("❌ Delete Expense")
if expenses:
    delete_id = st.selectbox("Select Expense ID to delete", [e.id for e in expenses], key="delete_select")
    if st.button("Delete"):
        ok = tracker.delete_expense(delete_id)
        if ok:
            st.success(f"Deleted expense id={delete_id}")
        else:
            st.error("Delete failed")

# Note
st.caption("Note: Streamlit reruns this script on each action; table refreshes after operations.")