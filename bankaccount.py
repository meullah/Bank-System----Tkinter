import os
import fileinput
import datetime
class BankAccount(object):
    """
    ACME Bank
    """
    def __init__(self):
        try:
            open('users.txt','x')
        except :
            pass

        if not os.path.exists('transactions'):
            os.makedirs('transactions')

    def accountExists(self,acc_id):
        with open('users.txt', 'r') as file:
            for line in file:
                data = line.split(',')
                if data[0] == acc_id.strip():
                    return True

        return False

    def signUp(self,acc_id,pin,balance=0,interest=3):
        if not self.accountExists(acc_id):
            str_to_write = "{},{},{},{}\n".format(acc_id,pin,balance,interest)
            self.write_line_to_file('users.txt',str_to_write)
        else:
            print('account already exisits')

    def signIn(self,acc_id,pin):
        with open('users.txt', 'r') as file:
            for line in file:
                data = line.split(',')
                if data[0] == acc_id.strip():
                    if data[1] == pin.strip():
                        return True

        return False

    def deposit(self,acc_id,ammount):
        data = self.getAccountDetails(acc_id).split(',')
        acc_id = data[0]
        pin = data[1]
        balance = int(data[2]) + int(ammount)
        interest  = data[3]

        with fileinput.input('users.txt', inplace=True) as file:
            for line in file:
                data = line.split(',')
                if(data[0] == acc_id):
                    str_to_write = "{},{},{},{}".format(acc_id,pin,balance,interest)
                    print(str_to_write,end='')
                else:
                    # print(line.rstrip())
                    pass
        filename = "transactions/{}.txt".format(acc_id)
        line = "deposit,{},{}\n".format(ammount, str(datetime.datetime.now()))
        self.write_line_to_file(filename,line)


    def withdraw(self,acc_id,ammount):
        if self.checkBalance(acc_id,ammount):
            data = self.getAccountDetails(acc_id).split(',')
            acc_id = data[0]
            pin = data[1]
            balance = int(data[2]) - int(ammount)
            interest  = data[3]

            with fileinput.input('users.txt', inplace=True) as file:
                for line in file:
                    data = line.split(',')
                    if(data[0] == acc_id):
                        str_to_write = "{},{},{},{}".format(acc_id,pin,balance,interest)
                        print(str_to_write,end='')
                    else:
                        print(line.rstrip())
        
            filename = "transactions/{}.txt".format(acc_id)
            line = "withdraw,{},{}\n".format(ammount,str(datetime.datetime.now()))
            self.write_line_to_file(filename,line)
            return True
        
        else:
            return False


    def checkBalance(self,acc_id,ammount):
        """
        checks if remaining balance after ammount withdrawl will be less than zero
        Returns True if remaining balance will not be less than zero False otherwise
        """
        with open('users.txt', 'r') as file:
            for line in file:
                data = line.split(',')
                if data[0] == acc_id.strip():
                    if((int(data[2]) - int(ammount)) < 0):
                        return False
                    else:
                        return True

        return False

    def write_line_to_file(self,filename, line):
        with open(filename, 'a') as file:
            file.write(line)

    def getAccountDetails(self,acc_id):
        with open('users.txt', 'r') as file:
            for line in file:
                data = line.split(',')
                if data[0] == acc_id.strip():
                    return line

        return None

    def getBalance(self,acc_id):
        """
        returns account balance 
        """

        data = self.getAccountDetails(acc_id).split(',')
        return data[2]

    def getAllTransactions(self,acc_id):
        filename = "transactions/{}.txt".format(acc_id)
        details = ""
        with open(filename, 'r') as file:
            for line in file:
                details = details + line
        
        return details
