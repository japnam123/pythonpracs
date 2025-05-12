class ATM:
    def __init__(self, account_number, initial_balance=0, pin="0000"):
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__pin = pin
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            return True
        return False
    
    def verify_pin(self, pin):
        return self.__pin == pin
    
    def check_balance(self, pin):
        if self.verify_pin(pin):
            return self.__balance
        return "Invalid PIN"
    
    def deposit(self, amount, pin):
        if not self.verify_pin(pin):
            return "Invalid PIN"
        
        if amount <= 0:
            return "Amount must be positive"
        
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"
    
    def withdraw(self, amount, pin):
        if not self.verify_pin(pin):
            return "Invalid PIN"
        
        if amount <= 0:
            return "Amount must be positive"
        
        if amount > self.__balance:
            return "Insufficient funds"
        
        self.__balance -= amount
        return f"Withdrawn {amount}. New balance: {self.__balance}"

def main():
    # Create ATM instance
    atm = ATM("1234567890", 1000, "1234")
    
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            pin = input("Enter PIN: ")
            result = atm.check_balance(pin)
            print(f"Balance: {result}")
        
        elif choice == "2":
            pin = input("Enter PIN: ")
            amount = float(input("Enter amount to deposit: "))
            result = atm.deposit(amount, pin)
            print(result)
        
        elif choice == "3":
            pin = input("Enter PIN: ")
            amount = float(input("Enter amount to withdraw: "))
            result = atm.withdraw(amount, pin)
            print(result)
        
        elif choice == "4":
            old_pin = input("Enter current PIN: ")
            if atm.verify_pin(old_pin):
                new_pin = input("Enter new PIN: ")
                if atm.set_pin(new_pin):
                    print("PIN changed successfully")
                else:
                    print("Invalid PIN format. PIN must be 4 digits")
            else:
                print("Invalid current PIN")
        
        elif choice == "5":
            print("Thank you for using our ATM")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main() 