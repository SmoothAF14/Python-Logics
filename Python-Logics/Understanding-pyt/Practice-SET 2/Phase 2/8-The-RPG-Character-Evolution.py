class warrior:
    def attack(self):
        return 100
class Paladin(warrior):
    def attack(self):
        return super().attack() *1.2
    def heal(self):
        return "healing"
w = warrior()
p = Paladin()
print(w.attack())  # Output: 100
print(p.attack())  # Output: 120.0
print(p.heal())    # Output: healing
