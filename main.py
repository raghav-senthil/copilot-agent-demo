"""A simple banking application."""


class InsufficientFundsError(Exception):
    """Raised when an account cannot cover a withdrawal or transfer."""


class BankAccount:
    """Represent a bank account with basic money movement operations."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add money to the account."""
        self._validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Remove money, raising an error when the balance is too low."""
        self._validate_amount(amount)
        if amount > self.balance:
            raise InsufficientFundsError(
                f"{self.owner} has insufficient funds for a {amount:.2f} withdrawal"
            )
        self.balance -= amount

    def transfer(self, amount: float, recipient: "BankAccount") -> None:
        """Transfer money to another account."""
        self.withdraw(amount)
        recipient.deposit(amount)

    @staticmethod
    def _validate_amount(amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")


def main() -> None:
    print("Create two bank accounts")
    first_account = BankAccount(
        input("First account owner: ").strip(),
        float(input("First account starting balance: ")),
    )
    second_account = BankAccount(
        input("Second account owner: ").strip(),
        float(input("Second account starting balance: ")),
    )
    accounts = [first_account, second_account]

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Show balances\n5. Exit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                account = accounts[int(input("Account (1 or 2): ")) - 1]
                account.deposit(float(input("Deposit amount: ")))
                print(f"New balance: ${account.balance:.2f}")
            elif choice == "2":
                account = accounts[int(input("Account (1 or 2): ")) - 1]
                account.withdraw(float(input("Withdrawal amount: ")))
                print(f"New balance: ${account.balance:.2f}")
            elif choice == "3":
                sender = accounts[int(input("Sender account (1 or 2): ")) - 1]
                recipient = accounts[int(input("Recipient account (1 or 2): ")) - 1]
                sender.transfer(float(input("Transfer amount: ")), recipient)
                print("Transfer completed")
            elif choice == "4":
                for account in accounts:
                    print(f"{account.owner}: ${account.balance:.2f}")
            elif choice == "5":
                print("Goodbye")
                break
            else:
                print("Please choose an option from 1 to 5")
        except (ValueError, IndexError):
            print("Please enter valid account numbers, amounts, and balances")
        except InsufficientFundsError as error:
            print(f"Transaction declined: {error}")


if __name__ == "__main__":
    main()
