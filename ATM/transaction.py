import account

def check_balance():
    return account.balance

def deposit(amount):
    if amount>0:
        account.balance += amount
        return True
    
def withdraw(amount):
    if 0 < amount <= account.balance:
        account.balance -= amount
        return True
    return False