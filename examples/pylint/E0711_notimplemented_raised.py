class Account:
    """Abstract base class describing the API for an account."""

    def __init__(self, balance: float) -> None:
        self._balance = balance

    def withdraw(self, ammount: float) -> float:
        """Withdraw some money from an account."""
        # Error on the following line: Use `NotImplementedError` instead
        raise NotImplemented
