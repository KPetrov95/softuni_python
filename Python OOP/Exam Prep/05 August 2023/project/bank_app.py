from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Adult": Adult, "Student": Student}

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type in self.VALID_LOANS.keys():
            new_loan = self.VALID_LOANS[loan_type]()
            self.loans.append(new_loan)
            return f"{loan_type} was successfully added."
        raise Exception("Invalid loan type!")

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS.keys():
            raise Exception("Invalid client type!")
        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."
        new_client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(cl for cl in self.clients if cl.client_id == client_id)
        loan = next(lo for lo in self.loans if lo.type == loan_type)
        if loan.type != client.VALID_LOAN:
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        client = next((cl for cl in self.clients if cl.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans_to_increase = [lo.increase_interest_rate() for lo in self.loans if lo.type == loan_type]
        return f"Successfully changed {len(loans_to_increase)} loans."

    def increase_clients_interest(self, min_rate: float):
        affected_clients = [cl.increase_clients_interest() for cl in self.clients if cl.interest < min_rate]
        return f"Number of clients affected: {len(affected_clients)}."

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = sum(cl.income for cl in self.clients)
        loans_count_granted_to_clients = sum([len(cl.loans) for cl in self.clients])
        granted_sum = sum([sum([lo.amount for lo in cl.loans]) for cl in self.clients])
        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum([loan.amount for loan in self.loans])
        avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0

        return f"Active Clients: {total_clients_count}" \
               f"\nTotal Income: {total_clients_income:.2f}" \
               f"\nGranted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}" \
               f"\nAvailable Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}" \
               f"\nAverage Client Interest Rate: {avg_client_interest_rate:.2f}"


bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())
