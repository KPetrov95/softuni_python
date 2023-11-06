class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Singer(Person):
    def __init__(self, instrument, name, surname):
        super().__init__(name, surname)
        self.instrument = instrument


class Employee(Person, Singer):
    def __init__(self, name, surname, instrument, job):
        super().__init__(name, surname, instrument)
        self.job = job
