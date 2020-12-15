class General:
    def __init__(self, name):
        self.name = name
        self.gave_health = 0
        self.lost_health = 0
        self.shoot = 0
        self.fight = 0
        self.move = 0
        self.individual_health_value = 0

    def get_helth_value(self, health_record):
        self.individual_health_value = self.individual_health_value + health_record
        if self.individual_health_value < 0:
            return str((self.name + ", Sorry, you dead."))
        elif self.individual_health_value == 0:
            return str((self.name + ", Good News, you can be treated!"))
        else:
            return str((self.name + ", You are stil alive!"))

    def get_move(self, move):
        self.move += move # if -1 it means person fail down, 0 means didnt move
        return str(self.move)

