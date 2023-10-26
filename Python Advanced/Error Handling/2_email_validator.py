class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_NAME_LENGTH = 5   # Minimum number of symbols before "@"
VALID_DOMAINS = ['com', 'bg', 'org', 'net']  # One of these needs to be present after "."

while True:
    command = input()
    domain = command.split('.')[-1]

    if command == 'End':   # Ends the Loop
        break
    if '@' not in command:
        raise MustContainAtSymbolError('Email must contain @')
    if command.index('@') < VALID_NAME_LENGTH - 1:
        raise NameTooShortError('Name must be more than 4 characters')
    if command.split('.')[1] not in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    print('Email is valid')
