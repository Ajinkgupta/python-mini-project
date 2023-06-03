import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from functions import ExpenseTracker
from ttkbootstrap import Style


class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("800x400")

        style = Style(theme="darkly")
        self.root.style = style

        self.tracker = ExpenseTracker()

        self.sidebar = ttk.Frame(root, width=240, padding="20 10")
        self.sidebar.pack(side="left", fill="y")

        self.main_frame = ttk.Frame(root, padding="20 10")
        self.main_frame.pack(side="left", fill="both", expand=True)

        self.date_label = ttk.Label(self.sidebar, text="Date:")
        self.date_label.pack()

        self.date_entry = ttk.Entry(self.sidebar, font=("Helvetica", 12))
        self.date_entry.pack()

        self.title_label = ttk.Label(self.sidebar, text="Title:")
        self.title_label.pack()

        self.title_entry = ttk.Entry(self.sidebar, font=("Helvetica", 12))
        self.title_entry.pack()

        self.description_label = ttk.Label(self.sidebar, text="Description:")
        self.description_label.pack()

        self.description_entry = ttk.Entry(self.sidebar, font=("Helvetica", 12))
        self.description_entry.pack()

        self.amount_label = ttk.Label(self.sidebar, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = ttk.Entry(self.sidebar, font=("Helvetica", 12))
        self.amount_entry.pack()

        button_frame = ttk.Frame(self.sidebar)
        button_frame.pack(pady=10)

        self.add_button = ttk.Button(button_frame, text="Add Expense", command=self.add_expense, style="primary.TButton")
        self.add_button.pack(side="left", padx=5, pady=5)

        self.view_button = ttk.Button(button_frame, text="View Expenses", command=self.view_expenses, style="success.TButton")
        self.view_button.pack(side="left", padx=5, pady=5)

        self.style = ttk.Style()
        self.style.configure("primary.TButton", borderwidth=0, borderradius=20)
        self.style.configure("success.TButton", borderwidth=0, borderradius=20)

        self.treeview = ttk.Treeview(self.main_frame, show="headings", selectmode="browse")
        self.treeview["columns"] = ("Date", "Title", "Description", "Amount")
        self.treeview.heading("Date", text="Date")
        self.treeview.heading("Title", text="Title")
        self.treeview.heading("Description", text="Description")
        self.treeview.heading("Amount", text="Amount")

        self.treeview.column("Date", width=100, anchor="center")
        self.treeview.column("Title", width=200, anchor="w")
        self.treeview.column("Description", width=300, anchor="w")
        self.treeview.column("Amount", width=100, anchor="center")

        self.treeview.pack(fill="both", expand=True)

        # Configure the style for the treeview
        self.style.configure("Treeview", font=("Helvetica", 12), borderwidth=1)
        self.style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

    def add_expense(self):
        date = self.date_entry.get()
        title = self.title_entry.get()
        description = self.description_entry.get()
        amount = float(self.amount_entry.get())

        self.tracker.add_expense(date, title, description, amount)

        self.date_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

        messagebox.showinfo("Expense Tracker", "Expense added successfully!")

    def view_expenses(self):
        expenses = self.tracker.get_expenses()

        self.treeview.delete(*self.treeview.get_children())
        for expense in expenses:
            self.treeview.insert("", "end", values=(expense['date'], expense['title'], expense['description'], expense['amount']))


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
