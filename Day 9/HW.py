class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        if isinstance(other, Account):
            return self._balance + other._balance
        return NotImplemented
    
class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05

class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02

if __name__ == "__main__":
    ravi_acc = SavingsAccount("Ravi", 10000.0)
    anjali_acc = CurrentAccount("Anjali", 15000.0)

    ravi_interest = ravi_acc.calculate_interest()
    anjali_interest = anjali_acc.calculate_interest()

    total_balance = ravi_acc + anjali_acc

    print("=== Account Details ===")
    print(f"Name: {ravi_acc._name}")
    print(f"Account Type: Savings Account")
    print(f"Balance: ${ravi_acc._balance:.2f}")
    print(f"Interest (5%): ${ravi_interest:.2f}\n")

    print(f"Name: {anjali_acc._name}")
    print(f"Account Type: Current Account")
    print(f"Balance: ${anjali_acc._balance:.2f}")
    print(f"Interest (2%): ${anjali_interest:.2f}\n")

    print("=== Summary ===")
    print(f"Total Combined Balance: ${total_balance:.2f}")