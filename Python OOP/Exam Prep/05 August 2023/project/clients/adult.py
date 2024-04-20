from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INTEREST: float = 4.0
    VALID_LOAN = 'MortgageLoan'

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, interest=self.INTEREST)
        self.loans = []

    def increase_clients_interest(self):
        self.interest += 2.0

