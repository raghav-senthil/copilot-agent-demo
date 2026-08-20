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
    alice = BankAccount("Alice")
    bob = BankAccount("Bob", 25.0)

    alice.deposit(100.0)
    alice.transfer(30.0, bob)
    print(f"{alice.owner}: ${alice.balance:.2f}")
    print(f"{bob.owner}: ${bob.balance:.2f}")


if __name__ == "__main__":
    main()
