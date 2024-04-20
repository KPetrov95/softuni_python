from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo

z = Zoo("Zoo", 1500, 1, 1)
#z.hire_worker(Keeper("K", 45, 100))
res = z.fire_worker("K")
print(z.workers)

print(res)