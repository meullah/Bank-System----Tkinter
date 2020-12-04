import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext 

from pylab import plot, show, xlabel, ylabel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from bankaccount import BankAccount

win = tk.Tk()
# Set window size here to '440x640' pixels
win.geometry('440x640')

# Set window title here to 'FedUni Banking'
win.title('FedUni Banking')

# The account number entry and associated variable
account_number_var = tk.StringVar()
# account_number_entry = tk.Entry(win, textvariable=account_number_var)
# account_number_entry.focus_set()

# The pin number entry and associated variable.
# Note: Modify this to 'show' PIN numbers as asterisks (i.e. **** not 1234)
pin_number_var = tk.StringVar()
# account_pin_entry = tk.Entry(win, text='PIN Number', textvariable=pin_number_var)

# The balance label and associated variable
balance_var = tk.StringVar()
balance_var.set('Balance: $0.00')
balance_label = tk.Label(win, textvariable=balance_var)

# The Entry widget to accept a numerical value to deposit or withdraw
amount_entry = tk.Entry(win)

# The transaction text widget holds text of the accounts transactions
transaction_text_widget = tk.Text(win, height=10, width=48)

# The bank account object we will work with
account = BankAccount()

# ---------- Button Handlers for Login Screen ----------

def clear_pin_entry(event):
    '''Function to clear the PIN number entry when the Clear / Cancel button is clicked.'''
    global pin_number_var
    number = ""
    pin_number_var.set(number)
    # Clear the pin number entry here

def handle_pin_button(event):
    '''Function to add the number of the button clicked to the PIN number entry via its associated variable.'''    

    global pin_number_var
    if len(pin_number_var.get()) <4:
        number = pin_number_var.get() + str(event)
        pin_number_var.set(number)
        # print(event,pin_number_var.get())
    # Limit to 4 chars in length

    # Set the new pin number on the pin_number_var
    

def log_in(event):
    '''Function to log in to the banking system using a known account number and PIN.'''
    global account
    global pin_number_var
    global account_number_var

    acc_no = account_number_var.get()
    # print(account_number_var.get() + "   ", pin_number_var.get())
    if account.signIn(account_number_var.get(),pin_number_var.get()) : 
        remove_all_widgets()
        popupmsg("login Sccessfull")
        create_account_screen(acc_no)
    else:
        popupmsg("login Failed")
   

def save_and_log_out():
    '''Function  to overwrite the account file with the current state of
       the account object (i.e. including any new transactions), remove
       all widgets and display the login screen.'''
    global account

    # Save the account with any new transactions
    
    # Reset the bank acount object

    # Reset the account number and pin to blank

    # Remove all widgets and display the login screen again
    

def perform_deposit(acc_no, ammount):
    '''Function to add a deposit for the amount in the amount entry to the
       account's transaction list.'''
   
    # print(acc_no , ammount)
    account.deposit(acc_no,ammount)
    message = "${} sccessfully added".format(ammount) 
    messagebox.showinfo(title='Operation Sucessfull', message=message)
   
def perform_withdrawal(acc_no, ammount):
    '''Function to withdraw the amount in the amount entry from the account balance and add an entry to the transaction list.'''
    if account.withdraw(acc_no,ammount):
        message = "${} withdrawn scucessfully".format(ammount) 
        messagebox.showinfo(title='Operation Sucessfull', message=message)

    else:
        messagebox.showerror(title='Operation Failed', message="insufficient Balance")


# ---------- Utility functions ----------

def remove_all_widgets():
    '''Function to remove all the widgets from the window.'''

    print('here')
    global win
    win.destroy()
    # for widget in win.winfo_children():
    #     widget.destory()


def plot_interest_graph(window):
    '''Function to plot the cumulative interest for the next 12 months here.'''

    # YOUR CODE to generate the x and y lists here which will be plotted
    
    # This code to add the plots to the window is a little bit fiddly so you are provided with it.
    # Just make sure you generate a list called 'x' and a list called 'y' and the graph will be plotted correctly.
    figure = Figure(figsize=(5,2), dpi=100)
    figure.suptitle('Cumulative Interest 12 Months')
    a = figure.add_subplot(111)
    x = [1,2,3,4,5,6,7,8,9,10,11,12]
    y = [1,3,5,6,7,6,7,8,9,10,11,12]
    a.plot(x, y, marker='o')
    a.grid()
    
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    graph_widget = canvas.get_tk_widget()
    # graph_widget.grid(row=4, column=0, columnspan=5, sticky='nsew')
    graph_widget.pack(fill='both')


# ---------- UI Screen Drawing Functions ----------

def create_login_screen():
    '''Function to create the login screen.'''    
    
    mainFrame = tk.Frame(win,bg='red')
    mainFrame.pack(fill='both', expand = True)


    verticalFrame = tk.Frame(mainFrame)
    verticalFrame.pack(fill='both')
    # ----- Row 0 -----
    # 'FedUni Banking' label here. Font size is 32.
    label = tk.Label( verticalFrame, text="FedUni Banking", font = 'Arial 32 bold', bg='white')
    label.pack(fill='both', padx = 40, pady=40)
    # label.place(height=150, width=460)
    # ----- Row 1 -----

    _horizontalFrame = tk.Frame(mainFrame)
    _horizontalFrame.pack(fill = 'both')

    # Acount Number / Pin label here
    _ = tk.Label(_horizontalFrame, text="Acount Number / Pin ",padx = 25, pady=25)
    _.grid(row = 0, column  = 0)
    # Account number entry here
    _ = tk.Entry(_horizontalFrame, textvariable  = account_number_var)
    _.grid(row = 0, column  = 1,ipady=25, sticky='nesw')
    # Account pin entry here
    _ = tk.Entry(_horizontalFrame, text='PIN Number', textvariable=pin_number_var,show='*')
    _.grid(row = 0, column  = 2,ipady=25, sticky='nesw')


    # ----- Row 2 -----

    # Buttons 1, 2 and 3 here. Buttons are bound to 'handle_pin_button' function via '<Button-1>' event.
    
    horizontalFrame = tk.Frame(mainFrame, bg = 'blue')
    horizontalFrame.pack(fill = 'both')

    tk.Button(horizontalFrame, text=' 1 ', 
                command=lambda: handle_pin_button(1), 
                height=1, width=15, padx = 18, pady=18).grid(row = 1, column  = 0,ipady=25, sticky='nesw')

    tk.Button(horizontalFrame, text=' 2 ', 
                command=lambda: handle_pin_button(2), 
                height=1, width=15, padx = 18, pady=18).grid(row = 1, column  = 1,ipady=25, sticky='nesw')

    tk.Button(horizontalFrame, text=' 3 ', 
                command=lambda: handle_pin_button(3), 
                height=1, width=15, padx = 18, pady=18).grid(row = 1, column  = 2,ipady=25, sticky='nesw')  

    # ----- Row 3 -----

    # Buttons 4, 5 and 6 here. Buttons are bound to 'handle_pin_button' function via '<Button-1>' event.
    tk.Button(horizontalFrame, text=' 4 ', 
                command=lambda: handle_pin_button(4), 
                height=1, width=15, padx = 18, pady=18).grid(row = 2, column  = 0,ipady=25, sticky='nesw')

    tk.Button(horizontalFrame, text=' 5 ', 
                command=lambda: handle_pin_button(5), 
                height=1, width=15, padx = 18, pady=18).grid(row = 2, column  = 1,ipady=25, sticky='nesw')

    tk.Button(horizontalFrame, text=' 6 ', 
                command=lambda: handle_pin_button(6), 
                height=1, width=15, padx = 18, pady=18).grid(row = 2, column  = 2,ipady=25, sticky='nesw')  

    # ----- Row 4 -----

    # Buttons 7, 8 and 9 here. Buttons are bound to 'handle_pin_button' function via '<Button-1>' event.
    tk.Button(horizontalFrame, text=' 7 ', 
                command=lambda: handle_pin_button(7), 
                height=1, width=15, padx = 18, pady=18).grid(row = 3, column  = 0,ipady=25, sticky='nesw')

    tk.Button(horizontalFrame, text=' 8 ', 
                command=lambda: handle_pin_button(8), 
                height=1, width=15, padx = 18, pady=18).grid(row = 3, column  = 1,ipady=25, sticky='nesw')

    tk.Button(horizontalFrame, text=' 9 ', 
                command=lambda: handle_pin_button(9), 
                height=1, width=15, padx = 18, pady=18).grid(row = 3, column  = 2,ipady=25, sticky='nesw')  

    # ----- Row 5 -----

    # Cancel/Clear button here. 'bg' and 'activebackground' should be 'red'. But calls 'clear_pin_entry' function.
    tk.Button(horizontalFrame, text=' Cancel/Clear', 
                command=lambda: clear_pin_entry(0), 
                bg = 'red',
                activebackground = 'red',
                height=1, width=15, padx = 18, pady=18).grid(row = 4, column  = 0,ipady=25, sticky='nesw')


    # Button 0 here
    tk.Button(horizontalFrame, text=' 0 ', 
                command=lambda: handle_pin_button(0), 
                height=1, width=15, padx = 18, pady=18).grid(row = 4, column  = 1,ipady=25, sticky='nesw')


    # Login button here. 'bg' and 'activebackground' should be 'green'). Button calls 'log_in' function.
    tk.Button(horizontalFrame, text=' login ', 
                bg = 'green',
                activebackground = 'green',
                command=lambda: log_in(0), 
                height=1, width=15, padx = 18, pady=18).grid(row = 4, column  = 2,ipady=25, sticky='nesw')


    # ----- Set column & row weights -----

    # Set column and row weights. There are 5 columns and 6 rows (0..4 and 0..5 respectively)
    

def create_account_screen(account_no):
    '''Function to create the account screen.'''
    win = tk.Tk()
    # Set window size here to '440x640' pixels
    win.geometry('440x640')

    # Set window title here to 'FedUni Banking'
    win.title('FedUni Banking')


    mainFrame = tk.Frame(win)
    mainFrame.pack(fill='both', expand = True)


    verticalFrame = tk.Frame(mainFrame)
    verticalFrame.pack(fill='both')
    
    # ----- Row 0 -----

    # FedUni Banking label here. Font size should be 24.
    label = tk.Label( verticalFrame, text="Account Services", font = 'Arial 24 bold', bg='white')
    label.pack(fill='both', padx = 40, pady=40)

    # ----- Row 1 -----

    _horizontalFrame = tk.Frame(mainFrame)
    _horizontalFrame.pack(fill = 'both')

    # Account number label here
    _text = "Account Number : " + account_no
    _balance = "Balance : $" + account.getBalance(account_no)
    _ = tk.Label(_horizontalFrame, text=_text, pady=15 , font = 'Arial 11 bold' )
    _.grid(row = 0, column  = 0)
    # Balance label here
    _ = tk.Label(_horizontalFrame, text=_balance, pady=15 , font = 'Arial 11 bold')
    _.grid(row = 0, column  = 1)
    # Log out button here
    tk.Button(_horizontalFrame, text=' LogOut ', 
                command=lambda: win.destroy(), 
                height=1, width=20, padx = 1, pady=1).grid(row = 0, 
                column  = 2, sticky='nesw')


    # ----- Row 2 -----

    horizontalFrame = tk.Frame(mainFrame)
    horizontalFrame.pack(fill = 'both')

    # Amount label here
    _ = tk.Label(horizontalFrame, text="Amount ($)", pady=15 ,width=16, font = 'Arial 11 bold' )
    _.grid(row = 0, column  = 0)
    # Amount entry here
    ammount = tk.Entry(horizontalFrame)
    ammount.grid(row = 0, column  = 1,ipady=15, sticky='nesw')

    # Deposit button here
    tk.Button(horizontalFrame, text=' Deposit ', 
            command=lambda: perform_deposit(account_no, ammount.get()), 
            height=1, width=10, padx = 1, pady=1).grid(row = 0, 
            column  = 2, sticky='nesw')
    # Withdraw button here
    tk.Button(horizontalFrame, text=' Withdraw ', 
                command=lambda: perform_withdrawal(account_no,ammount.get()), 
                height=1, width=10, padx = 1, pady=1).grid(row = 0, 
                column  = 3, sticky='nesw')
    # NOTE: Bind Deposit and Withdraw buttons via the command attribute to the relevant deposit and withdraw
    #       functions in this file. If we "BIND" these buttons then the button being pressed keeps looking as
    #       if it is still pressed if an exception is raised during the deposit or withdraw operation, which is
    #       offputting.
    
    
    # ----- Row 3 -----

    textFrame = tk.Frame(mainFrame)
    textFrame.pack(fill = 'both')
    text_area = scrolledtext.ScrolledText(textFrame,  
                                      wrap = tk.WORD,  
                                      height = 8,  
                                      font = ("Times New Roman", 
                                              15)) 
  
    text_area.pack(fill='both') 
    text_area.insert(tk.INSERT, account.getAllTransactions(account_no))
    # ----- Row 4 - Graph -----

    plot_interest_graph(textFrame)
    # Call plot_interest_graph() here to display the graph
    

    # ----- Set column & row weights -----

    # Set column and row weights here - there are 5 rows and 5 columns (numbered 0 through 4 not 1 through 5!)

    win.mainloop()

def popupmsg(msg):
    popup = tk.Tk()
    popup.geometry('100x100')
    popup.wm_title("!")
    label = tk.Label(popup, text=msg,)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

# ---------- Display Login Screen & Start Main loop ----------

create_login_screen()
# create_account_screen('1122')
win.mainloop()
