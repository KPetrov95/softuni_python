from project.clients.base_client import BaseClient


class Student(BaseClient):
    INTEREST: float = 2.0
    VALID_LOAN = 'StudentLoan'

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, interest=self.INTEREST)


    def increase_clients_interest(self):
        self.interest += 1.0

