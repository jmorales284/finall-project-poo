from entities.person import Person
# Clase de pasajeros
class Passenger(Person):
    def __init__(self):
        super()
        self.__status = None

    def getStatus(self):
            return self.__status
        
    def setStatus(self, new_status):
            self.__status = new_status

    def getPassengerInfo(self):
        return self.getID(), self.getName(), self.getPhone(), self.__status

    def peopleFlights(self, airline):
        passengerFlights = []
        for flight in airline.getFlight():
            if self in flight.PassengersFlights(flight.getFlightNumber()):
                passengerFlights.append(flight)
        return passengerFlights
