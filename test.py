from buildings import Farm
from tiles import Plain


t1 = Plain()
print(t1.buildings)
print(t1.sites)
print(t1.has_available_site())

t1.build(Farm())

print(t1.buildings)
print(t1.sites)
print(t1.has_available_site())

[building.produce() for building in t1.buildings]
[building.produce() for building in t1.buildings]
[print(building.storage) for building in t1.buildings]
