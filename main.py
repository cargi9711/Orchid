from orchid import Orchid
from care import OrchidCare
from environment import Environment

orchid = Orchid("Phalaenopsis", "White", "Asia")
care = OrchidCare("Indirect sunlight", "Moderate", 70)
env = Environment(22, 70)

print(orchid)
print(orchid.bloom())
print(care.instructions())
print(env.describe())
