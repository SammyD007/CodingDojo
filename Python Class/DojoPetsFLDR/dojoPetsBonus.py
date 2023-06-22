from ninja import Ninja
from pet import Pet

ninja1 = Ninja("Sam", "Dalrymple", "Beggin Bits", "Kibble", Pet("Buddy", "Dog", "Sit", 100, 100))

ninja1.feed().walk().bathe()