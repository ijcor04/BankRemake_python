import datetime
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class Account:
    def __init__(self, Accnum, type, name, bal):
        self._Accnum = Accnum
        self.type = type
        self.name = name
        self._bal = bal
        self.date_last_trans = datetime.date.today()
    
    def getAccnum(self): 
        return self._Accnum
    def get_type(self):
        return self.type
    def get_name(self):
        return self.name
    def get_accbal(self):
        return self._bal
    def get_date_last_trans(self):
        return self.date_last_trans
    
    def set_Accnum(self, x):
        self._Accnum = x
    def set_type(self, x):
        self.type = x
    def set_name(self, x):
        self.name = x
    def set_acc_bal(self, x):
        self._bal = x
    def set_date_last_trans(self, x):
        self.date_last_trans = x
    
    def __str__(self):
        return f"Account #{self._Accnum} | Type: {self.type} | Name: {self.name} | Balance: ${self._bal:.2f}"

class AccountManager:
    def __init__(self):
        self.accounts = []  # List to store accounts
    
    def add_account(self, account):
        self.accounts.append(account)
        return True
    
    def remove_account(self, account_number):
        for i, account in enumerate(self.accounts):
            if account.getAccnum() == account_number:
                del self.accounts[i]
                return True
        return False
    
    def find_account(self, account_number):
        for account in self.accounts:
            if account.getAccnum() == account_number:
                return account
        return None
    
    def get_all_accounts(self):
        return self.accounts

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.account_manager = AccountManager()
        
        self.title("Bank Account Management System")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.accounts_tab = ttk.Frame(self.notebook)
        self.transactions_tab = ttk.Frame(self.notebook)
        self.create_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.accounts_tab, text="Accounts")
        self.notebook.add(self.transactions_tab, text="Transactions")
        self.notebook.add(self.create_tab, text="Create Account")
        
        # Set up each tab
        self.setup_accounts_tab()
        self.setup_transactions_tab()
        self.setup_create_account_tab()
    
    def setup_accounts_tab(self):
        # Account list frame
        list_frame = ttk.LabelFrame(self.accounts_tab, text="Account List")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create Treeview for accounts
        columns = ("Account Number", "Type", "Name", "Balance", "Last Transaction")
        self.accounts_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        # Set column headings
        for col in columns:
            self.accounts_tree.heading(col, text=col)
            self.accounts_tree.column(col, width=150)
        
        self.accounts_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.accounts_tree.yview)
        self.accounts_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Buttons frame
        button_frame = ttk.Frame(self.accounts_tab)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Buttons
        ttk.Button(button_frame, text="Refresh", command=self.refresh_accounts).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Remove Account", command=self.remove_account).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="View Details", command=self.view_account_details).pack(side=tk.LEFT, padx=5)
    
    def setup_transactions_tab(self):
        # Transaction frame
        transaction_frame = ttk.LabelFrame(self.transactions_tab, text="Perform Transaction")
        transaction_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Account selection
        ttk.Label(transaction_frame, text="Account Number:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.account_var = tk.StringVar()
        self.account_combo = ttk.Combobox(transaction_frame, textvariable=self.account_var)
        self.account_combo.grid(row=0, column=1, padx=5, pady=5)
        
        # Transaction type
        ttk.Label(transaction_frame, text="Transaction Type:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.transaction_var = tk.StringVar(value="Deposit")
        ttk.Radiobutton(transaction_frame, text="Deposit", variable=self.transaction_var, value="Deposit").grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        ttk.Radiobutton(transaction_frame, text="Withdraw", variable=self.transaction_var, value="Withdraw").grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        
        # Amount
        ttk.Label(transaction_frame, text="Amount:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.amount_var = tk.StringVar()
        ttk.Entry(transaction_frame, textvariable=self.amount_var).grid(row=2, column=1, padx=5, pady=5)
        
        # Button
        ttk.Button(transaction_frame, text="Process Transaction", command=self.process_transaction).grid(row=3, column=1, padx=5, pady=15)
        
        # Transaction history frame
        history_frame = ttk.LabelFrame(self.transactions_tab, text="Transaction History")
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Simple text for now (could be enhanced with a transaction log)
        self.history_text = tk.Text(history_frame, height=8, width=60)
        self.history_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.history_text.insert(tk.END, "Transaction history will be displayed here.\n")
        self.history_text.config(state=tk.DISABLED)
    
    def setup_create_account_tab(self):
        # Create account frame
        create_frame = ttk.LabelFrame(self.create_tab, text="Create New Account")
        create_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Account Number
        ttk.Label(create_frame, text="Account Number:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.new_acc_num = tk.StringVar()
        ttk.Entry(create_frame, textvariable=self.new_acc_num).grid(row=0, column=1, padx=5, pady=5)
        
        # Account Type
        ttk.Label(create_frame, text="Account Type:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.new_acc_type = tk.StringVar()
        ttk.Combobox(create_frame, textvariable=self.new_acc_type, values=["Checking", "Savings", "Business"]).grid(row=1, column=1, padx=5, pady=5)
        
        # Account Name
        ttk.Label(create_frame, text="Account Name:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.new_acc_name = tk.StringVar()
        ttk.Entry(create_frame, textvariable=self.new_acc_name).grid(row=2, column=1, padx=5, pady=5)
        
        # Initial Balance
        ttk.Label(create_frame, text="Initial Balance:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.new_acc_bal = tk.StringVar()
        ttk.Entry(create_frame, textvariable=self.new_acc_bal).grid(row=3, column=1, padx=5, pady=5)
        
        # Create button
        ttk.Button(create_frame, text="Create Account", command=self.create_account).grid(row=4, column=0, columnspan=2, padx=5, pady=15)
    
    def refresh_accounts(self):
        # Clear the treeview
        for item in self.accounts_tree.get_children():
            self.accounts_tree.delete(item)
        
        # Update the account combo box
        account_numbers = []
        
        # Add accounts to the treeview
        for account in self.account_manager.get_all_accounts():
            self.accounts_tree.insert("", tk.END, values=(
                account.getAccnum(),
                account.get_type(),
                account.get_name(),
                f"${account.get_accbal():.2f}",
                account.get_date_last_trans()
            ))
            account_numbers.append(account.getAccnum())
        
        # Update the combobox values
        self.account_combo['values'] = account_numbers
    
    def create_account(self):
        try:
            acc_num = self.new_acc_num.get()
            acc_type = self.new_acc_type.get()
            acc_name = self.new_acc_name.get()
            acc_bal = float(self.new_acc_bal.get())
            
            # Validate input
            if not acc_num or not acc_type or not acc_name:
                messagebox.showerror("Error", "All fields are required!")
                return
            
            if acc_bal < 0:
                messagebox.showerror("Error", "Initial balance cannot be negative!")
                return
            
            # Check if account number already exists
            if self.account_manager.find_account(acc_num):
                messagebox.showerror("Error", "Account number already exists!")
                return
            
            # Create and add the account
            new_account = Account(acc_num, acc_type, acc_name, acc_bal)
            self.account_manager.add_account(new_account)
            
            # Clear the fields
            self.new_acc_num.set("")
            self.new_acc_type.set("")
            self.new_acc_name.set("")
            self.new_acc_bal.set("")
            
            messagebox.showinfo("Success", "Account created successfully!")
            
            # Refresh the accounts list
            self.refresh_accounts()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the balance!")
    
    def process_transaction(self):
        try:
            account_number = self.account_var.get()
            transaction_type = self.transaction_var.get()
            amount = float(self.amount_var.get())
            
            if amount <= 0:
                messagebox.showerror("Error", "Transaction amount must be positive!")
                return
            
            account = self.account_manager.find_account(account_number)
            if not account:
                messagebox.showerror("Error", "Account not found!")
                return
            
            if transaction_type == "Deposit":
                account.set_acc_bal(account.get_accbal() + amount)
                message = f"Deposited ${amount:.2f} to account {account_number}"
            else:  # Withdraw
                if amount > account.get_accbal():
                    messagebox.showerror("Error", "Insufficient balance!")
                    return
                account.set_acc_bal(account.get_accbal() - amount)
                message = f"Withdrew ${amount:.2f} from account {account_number}"
            
            account.set_date_last_trans(datetime.date.today())
            
            # Update transaction history
            self.history_text.config(state=tk.NORMAL)
            self.history_text.insert(tk.END, f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {message}\n")
            self.history_text.see(tk.END)
            self.history_text.config(state=tk.DISABLED)
            
            # Clear the amount field
            self.amount_var.set("")
            
            messagebox.showinfo("Success", f"{transaction_type} successful! New balance: ${account.get_accbal():.2f}")
            
            # Refresh the accounts list
            self.refresh_accounts()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the amount!")
    
    def remove_account(self):
        selected_items = self.accounts_tree.selection()
        if not selected_items:
            messagebox.showinfo("Info", "Please select an account to remove")
            return
        
        item = selected_items[0]
        account_number = self.accounts_tree.item(item, "values")[0]
        
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to remove account {account_number}?")
        if confirm:
            if self.account_manager.remove_account(account_number):
                messagebox.showinfo("Success", "Account removed successfully!")
                self.refresh_accounts()
            else:
                messagebox.showerror("Error", "Failed to remove account!")
    
    def view_account_details(self):
        selected_items = self.accounts_tree.selection()
        if not selected_items:
            messagebox.showinfo("Info", "Please select an account to view")
            return
        
        item = selected_items[0]
        account_number = self.accounts_tree.item(item, "values")[0]
        account = self.account_manager.find_account(account_number)
        
        if account:
            details = f"Account Number: {account.getAccnum()}\n"
            details += f"Account Type: {account.get_type()}\n"
            details += f"Account Name: {account.get_name()}\n"
            details += f"Balance: ${account.get_accbal():.2f}\n"
            details += f"Last Transaction Date: {account.get_date_last_trans()}"
            
            messagebox.showinfo("Account Details", details)

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()