from typing import List

from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []


    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker_to_fire = next((w for w in self.workers if w.name == worker_name), None)
        if worker_to_fire:
            self.workers.remove(worker_to_fire)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([w.salary for w in self.workers])
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animal_costs = sum([a.money_for_care for a in self.animals])
        if self.__budget < animal_costs:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animal_costs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]

        result = [f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:"]
        result.extend(lions)
        result.append(f'----- {len(tigers)} Tigers:')
        result.extend(tigers)
        result.append(f'----- {len(cheetahs)} Cheetahs:')
        result.extend(cheetahs)
        return f'\n'.join(result)

    def workers_status(self):
        keepers = [repr(w) for w in self.workers if isinstance(w, Keeper)]
        caretakers = [repr(w) for w in self.workers if isinstance(w, Caretaker)]
        vets = [repr(w) for w in self.workers if isinstance(w, Vet)]

        result = [f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:"]
        result.extend(keepers)
        result.append(f'----- {len(caretakers)} Caretakers:')
        result.extend(caretakers)
        result.append(f'----- {len(vets)} Vets:')
        result.extend(vets)
        return f'\n'.join(result)