"""Public, protected, and private attribute conventions."""


class BankAccount:
    """Demonstrates Python encapsulation conventions."""

    def __init__(self, owner, balance=0):
        self.owner = owner           # public
        self._balance = balance      # protected (convention)
        self.__pin = 1234            # private (name-mangled)

    def deposit(self, amount):
        """Public method to deposit money."""
        if amount > 0:
            self._balance += amount
        return self._balance

    def _validate_pin(self, pin):
        """Protected method: validate PIN."""
        return pin == self.__pin

    def withdraw(self, amount, pin):
        """Withdraw if PIN is correct and funds are sufficient."""
        if not self._validate_pin(pin):
            return "Invalid PIN"
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
        return self._balance

    def get_balance(self):
        """Public getter for balance."""
        return self._balance


if __name__ == "__main__":
    acc = BankAccount("Alice", 1000)
    print(f"Owner: {acc.owner}")
    print(f"Balance: {acc.get_balance()}")
    print(f"Deposit 500: {acc.deposit(500)}")
    print(f"Withdraw 200: {acc.withdraw(200, 1234)}")
    print(f"Bad PIN: {acc.withdraw(100, 0000)}")
    # Name mangling: __pin becomes _BankAccount__pin
    print(f"Mangled access: {acc._BankAccount__pin}")
