# ...existing code...
from tkinter import *
from tkinter import messagebox
from member_module import *
from account_module import *
from loan_module import *


mainWindow = Tk()
mainWindow.title("Administrator's Panel")
mainWindow.geometry("500x500")
mainWindow.config(
        bg="#C4956A",
)

# --- ADDED: in-memory storage for created objects
members = {}   # key: member_id -> Member instance
accounts = {}  # key: account_no -> Account instance
loans = {}     # key: loan_id -> Loan instance
# ...existing code...

def display_main():
    window2 = Toplevel(mainWindow, bg="#B2A67C")
    window2.title("SACCO Management System")
    window2.geometry("500x500")


    Button(window2, text="Member Registration", width=20, pady=5, command=lambda:member_reg_win(window2)).pack(pady=10)
    Button(window2, text="Account Registration", width=20, pady=5, command=lambda:account_reg_win(window2)).pack(pady=10)
    Button(window2, text="Loan Registration", width=20, pady=5, command=lambda:loan_reg_win(window2)).pack(pady=10)

    # --- ADDED: Account operations entry in main menu
    Button(window2, text="Account Operations", width=20, pady=5, command=lambda:account_ops_win(window2)).pack(pady=10)

    def member_reg_win(parent):
        mem_window = Toplevel(parent, bg="#b8f69d")
        mem_window.title("Member Registration Panel")
        mem_window.geometry("400x500")

        Label(mem_window, text="Member_ID", bg="#b8f69d").pack(pady=5)
        mem_id_ent = Entry(mem_window)
        mem_id_ent.pack()

        Label(mem_window, text="First Name", bg="#b8f69d").pack(pady=5)
        f_name_ent = Entry(mem_window)
        f_name_ent.pack()

        Label(mem_window, text="Last Name", bg="#b8f69d").pack(pady=5)
        l_name_ent = Entry(mem_window)
        l_name_ent.pack()

        Label(mem_window, text="Gender", bg="#b8f69d").pack(pady=5)
        gender_ent = Entry(mem_window)
        gender_ent.pack()

        Label(mem_window, text="Contact", bg="#b8f69d").pack(pady=5)
        contact_ent = Entry(mem_window)
        contact_ent.pack()

        Label(mem_window, text="Address", bg="#b8f69d").pack(pady=5)
        add_ent = Entry(mem_window)
        add_ent.pack()

        def register_member():
            member_id = mem_id_ent.get().strip()
            first_name = f_name_ent.get().strip()
            last_name = l_name_ent.get().strip()
            gender = gender_ent.get().strip()
            contact = contact_ent.get().strip()
            address = add_ent.get().strip()
            
            if not member_id or not first_name or not last_name or not gender or not contact or not address:
                messagebox.showerror("Missing Fields", "All fields must be filled up")
                return

            if member_id in members:
                messagebox.showerror("Duplicate Member", f"Member ID '{member_id}' already exists.")
                return
            
            member_inst = Member(
                member_id,
                first_name,
                last_name,
                gender,
                contact,
                address
            )
            
            # store member for later composition with Account/Loan
            members[member_id] = member_inst

            result = member_inst.Register()

            messagebox.showinfo("Member Registered", result)
            
        Button(mem_window, text= "REGISTER MEMBER".center(30,"-") ,command=register_member).pack(pady=10)


    # --- ADDED: Account Registration window
    def account_reg_win(parent):
        acc_window = Toplevel(parent, bg="#e0f7ff")
        acc_window.title("Account Registration Panel")
        acc_window.geometry("400x350")

        Label(acc_window, text="Account Number", bg="#e0f7ff").pack(pady=6)
        acc_no_ent = Entry(acc_window)
        acc_no_ent.pack()

        Label(acc_window, text="Account Type (e.g. Savings)", bg="#e0f7ff").pack(pady=6)
        acc_type_ent = Entry(acc_window)
        acc_type_ent.pack()

        Label(acc_window, text="Member ID (owner)", bg="#e0f7ff").pack(pady=6)
        acc_member_ent = Entry(acc_window)
        acc_member_ent.pack()

        def create_account():
            acc_no = acc_no_ent.get().strip()
            acc_type = acc_type_ent.get().strip()
            member_id = acc_member_ent.get().strip()

            if not acc_no or not acc_type or not member_id:
                messagebox.showerror("Missing Fields", "All fields must be filled up")
                return

            if acc_no in accounts:
                messagebox.showerror("Duplicate Account", f"Account '{acc_no}' already exists.")
                return

            member_obj = members.get(member_id)
            if not member_obj:
                messagebox.showerror("Member Not Found", f"No member with ID '{member_id}' registered.")
                return

            account_inst = Account(acc_no, member_obj, acc_type)
            accounts[acc_no] = account_inst

            summary = f'''Account Number: {acc_no}
Account Holder: {member_obj.first_name} {member_obj.last_name}
Account Type: {acc_type}
'''

            messagebox.showinfo("Account Created", summary)
        
        Button(acc_window, text="CREATE ACCOUNT".center(30, "-"), command=create_account).pack(pady=12)


    # --- ADDED: Loan Registration window
    def loan_reg_win(parent):
        loan_window = Toplevel(parent, bg="#f9cb9a")
        loan_window.title("Loan Registration Panel")
        loan_window.geometry("400x350")

        Label(loan_window, text="Loan ID", bg="#f9cb9a").pack(pady=6)
        loan_id_ent = Entry(loan_window)
        loan_id_ent.pack()

        Label(loan_window, text="Member ID (applicant)", bg="#f9cb9a").pack(pady=6)
        loan_member_ent = Entry(loan_window)
        loan_member_ent.pack()

        Label(loan_window, text="Loan Amount (numeric)", bg="#f9cb9a").pack(pady=6)
        loan_amount_ent = Entry(loan_window)
        loan_amount_ent.pack()

        Label(loan_window, text="Payment Period (months, integer)", bg="#f9cb9a").pack(pady=6)
        payment_period_ent = Entry(loan_window)
        payment_period_ent.pack()

        def create_loan():
            loan_id = loan_id_ent.get().strip()
            member_id = loan_member_ent.get().strip()
            loan_amount = loan_amount_ent.get().strip()
            payment_period = payment_period_ent.get().strip()

            if not loan_id or not member_id or not loan_amount or not payment_period:
                messagebox.showerror("Missing Fields", "All fields must be filled up")
                return

            if loan_id in loans:
                messagebox.showerror("Duplicate Loan", f"Loan ID '{loan_id}' already exists.")
                return

            member_obj = members.get(member_id)
            if not member_obj:
                messagebox.showerror("Member Not Found", f"No member with ID '{member_id}' registered.")
                return

            try:
                loan_amount_val = int(loan_amount)
                payment_period_val = int(payment_period)
                if loan_amount_val <= 0 or payment_period_val <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Invalid Input", "Loan amount and payment period must be positive integers.")
                return

            loan_inst = Loan(loan_id, member_obj, loan_amount_val, payment_period_val)
            loan_inst.set_payment_amount()
            loans[loan_id] = loan_inst


            summary = loan_inst.Approve_Loan()

            messagebox.showinfo("Loan Created", summary)

        Button(loan_window, text="CREATE & SET PAYMENT".center(30, "-"), command=create_loan).pack(pady=12)

    # --- ADDED: Account operations window + deposit/withdraw/balance actions
    def account_ops_win(parent):
        ops_win = Toplevel(parent, bg="#dfe7d7")
        ops_win.title("Account Operations")
        ops_win.geometry("420x300")

        Label(ops_win, text="Choose Operation", bg="#dfe7d7", font=("Arial", 12, "bold")).pack(pady=8)

        Button(ops_win, text="Deposit to Account", width=25, command=lambda:deposit_win(ops_win)).pack(pady=6)
        Button(ops_win, text="Withdraw from Account", width=25, command=lambda:withdraw_win(ops_win)).pack(pady=6)
        Button(ops_win, text="Get Account Balance", width=25, command=lambda:balance_win(ops_win)).pack(pady=6)

    def deposit_win(parent):
        dwin = Toplevel(parent, bg="#eef7ee")
        dwin.title("Deposit")
        dwin.geometry("380x220")

        Label(dwin, text="Account Number", bg="#eef7ee").pack(pady=6)
        acc_no_ent = Entry(dwin)
        acc_no_ent.pack()

        Label(dwin, text="Amount to Deposit", bg="#eef7ee").pack(pady=6)
        amount_ent = Entry(dwin)
        amount_ent.pack()

        def do_deposit():
            acc_no = acc_no_ent.get().strip()
            amt = amount_ent.get().strip()
            if not acc_no or not amt:
                messagebox.showerror("Missing Fields", "Account number and amount are required.")
                return
            acc_obj = accounts.get(acc_no)
            if not acc_obj:
                messagebox.showerror("Account Not Found", f"No account with number '{acc_no}' found.")
                return
            try:
                val = int(amt)
            except ValueError:
                messagebox.showerror("Invalid Amount", "Enter a valid integer amount.")
                return
            res = acc_obj.Credit(val)
            messagebox.showinfo("Deposit Result", res)

        Button(dwin, text="DEPOSIT", command=do_deposit).pack(pady=12)

    def withdraw_win(parent):
        wwin = Toplevel(parent, bg="#fff0f0")
        wwin.title("Withdraw")
        wwin.geometry("380x220")

        Label(wwin, text="Account Number", bg="#fff0f0").pack(pady=6)
        acc_no_ent = Entry(wwin)
        acc_no_ent.pack()

        Label(wwin, text="Amount to Withdraw", bg="#fff0f0").pack(pady=6)
        amount_ent = Entry(wwin)
        amount_ent.pack()

        def do_withdraw():
            acc_no = acc_no_ent.get().strip()
            amt = amount_ent.get().strip()
            if not acc_no or not amt:
                messagebox.showerror("Missing Fields", "Account number and amount are required.")
                return
            acc_obj = accounts.get(acc_no)
            if not acc_obj:
                messagebox.showerror("Account Not Found", f"No account with number '{acc_no}' found.")
                return
            try:
                val = int(amt)
            except ValueError:
                messagebox.showerror("Invalid Amount", "Enter a valid integer amount.")
                return
            res = acc_obj.Debit(val)
            messagebox.showinfo("Withdraw Result", res)

        Button(wwin, text="WITHDRAW", command=do_withdraw).pack(pady=12)

    def balance_win(parent):
        bwin = Toplevel(parent, bg="#f0f7ff")
        bwin.title("Account Balance")
        bwin.geometry("380x180")

        Label(bwin, text="Account Number", bg="#f0f7ff").pack(pady=6)
        acc_no_ent = Entry(bwin)
        acc_no_ent.pack()

        def show_balance():
            acc_no = acc_no_ent.get().strip()
            if not acc_no:
                messagebox.showerror("Missing Field", "Account number is required.")
                return
            acc_obj = accounts.get(acc_no)
            if not acc_obj:
                messagebox.showerror("Account Not Found", f"No account with number '{acc_no}' found.")
                return
            bal = acc_obj.Get_Balance()
            messagebox.showinfo("Account Balance", f"Balance for {acc_no}: UGX. {bal}")

        Button(bwin, text="GET BALANCE", command=show_balance).pack(pady=12)
# ...existing code...

Label(mainWindow, text="---SACCO Management System---", font=("ALGERIAN", 14, "bold", "italic"), bg="#C4956A").pack(pady=30)

Label(mainWindow, text="Username", font=("Constantia", 12), bg="#C4956A").pack()
username_ent = Entry(mainWindow, width=30)
username_ent.pack()

Label(mainWindow, text="Password", font=("Constantia", 12), bg="#C4956A").pack()
password_ent = Entry(mainWindow, show="•", width=30)
password_ent.pack()

def login_accept():
    username = username_ent.get().strip()
    password = password_ent.get().strip()

    if not username or not password:
        messagebox.showerror("Login Error", "All fields must be field")
        return
    
    if username == "1" and password == "1":
        messagebox.showinfo("Access Granted", "You have logged in successfully")
        mainWindow.withdraw()
        display_main()
    else:
        messagebox.showerror("Access Denied", "Wrong USERNAME or PASSWORD")
    
Button(mainWindow, text="LOGIN", width=10, command=login_accept).pack(pady=20)

mainWindow.mainloop()
# ...existing code...