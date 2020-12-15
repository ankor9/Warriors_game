from lesson2HomeworkGeneral import *

class Individual(General):

    def archary_name(self):
        return str("I am Archary and my name is " + self.name)
    def arch_shoot(self):
        self.shoot += 1
    def arch_total_shoot(self):
        return str((self.name + " shooted " + str(self.shoot)))

    def doctor_name(self):
        return str("I am Doctor and my name is " + self.name)
    def doctor_gave_health(self):
        self.gave_health += 1
    def doctor_lost_health(self):
        self.lost_health += 1
    def doctor_saved_lost_lives(self):
        return str(self.name + " saved lives: " + str(self.gave_health) + " and lost lives: "+ str(self.lost_health))

    def solder_name(self):
        return str("I am Solder and my name is " + self.name)
    def solder_fight(self):
        self.fight += 1
    def solder_total_fight(self):
        return str(self.name + " had " + str(self.fight) +" fights." )

arch1 = Individual('Mr.Arch1')
print(arch1.archary_name())
arch1.arch_shoot()
arch1.arch_shoot()
arch1.arch_shoot()
print(arch1.arch_total_shoot())
print(arch1.get_helth_value(0))
print(arch1.get_move(1) + "\n")

doc1 = Individual('Mr.Doctor1')
print(doc1.doctor_name())
doc1.doctor_gave_health()
doc1.doctor_gave_health()
doc1.doctor_lost_health()
print(doc1.doctor_saved_lost_lives())
print(doc1.get_helth_value(-1))
print(doc1.get_move(0) + "\n")

solder1 = Individual('Mr.Solder1')
print(solder1.solder_name())
solder1.solder_fight()
solder1.solder_fight()
solder1.solder_fight()
print(solder1.solder_total_fight())
print(solder1.get_helth_value(5))
print(solder1.get_move(-1) + "\n")

