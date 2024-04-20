import unittest

class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, transaction):
        if isinstance(transaction, int):
            self.handle_transaction(transaction)
        else:
            raise ValueError("please use int for amount")

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __iter__(self):
        return iter(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __eq__(self, other):
        return self.amount == other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __add__(self, other):
        return Account(owner=f"{self.owner}&{other.owner}", amount=self.amount + other.amount)

