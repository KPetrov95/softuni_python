from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        sub = next((s.__repr__() for s in self.subscriptions if s.id == subscription_id))
        customer = next((c.__repr__() for c in self.customers if c.id == subscription_id))
        trainer = next((t.__repr__() for t in self.trainers if t.id == subscription_id))
        equipment = next((e.__repr__() for e in self.equipment if e.id == subscription_id))
        plan = next((p.__repr__() for p in self.plans if p.id == subscription_id))
        result = f"{sub}\n{customer}\n{trainer}\n{equipment}\n{plan}"
        return result
