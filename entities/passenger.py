from entities.person import Person
# Clase de pasajeros
class Passenger(Person):
    def __init__(self):
        super().__init__("defaultID", "defaultName", "defaultPhone")
        self.__status = None

    def getStatus(self):
            return self.__status
        
    def setStatus(self, new_status):
            self.__status = new_status


    
        