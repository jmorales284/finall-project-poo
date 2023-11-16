from entities.passenger import Passenger

#clase de vuelos
class Flight:
    def __init__(self):
        self.__flightNumber = None
        self.__origin = None
        self.__arrival = None
        self.__planeID = None
        self.__pilotName = None
        self.__flightTime = None
        self.__flightDate = None
        self.__status = None
        self.__passengerList = []

        # Getters
    def getFlightNumber(self):
        return self.__flightNumber
    def getOrigin(self):
        return self.__origin
    def getArrival(self):
        return self.__arrival
    def getPlaneID(self):
        return self.__planeID
    def getPilotName(self):
        return self.__pilotName
    def getFlightTime(self):
        return self.__flightTime
    def getFlightDate(self):
        return self.__flightDate
    def getStatus(self):
        return self.__status
    # Setters
    def setFlightNumber(self, newFlightNumber):
        self.__flightNumber = newFlightNumber
    def setOrigin(self, newOrigin):
        self.__origin = newOrigin
    def setArrival(self, newArrival):
        self.__arrival = newArrival
    def setPlaneID(self, newPlaneID):
        self.__planeID = newPlaneID
    def setPilotName(self, newPilotName):
        self.__pilotName = newPilotName
    def setFlightTime(self, newFlightTime):
        self.__flightTime = newFlightTime
    def setFlightDate(self, newFlightDate):
        self.__flightDate = newFlightDate
    def setStatus(self, newStatus):
        self.__status = newStatus


    
    def addToTheList(self, passenger):
        self.__passengerList.append(passenger)

    def PassengersFlights(self, searchFlightNumber):
        passengersInFlight = []
        if self.__flightNumber == searchFlightNumber:
            for passenger in self.__passengerList:
                passengersInFlight.append(passenger)
        return passengersInFlight

    def removePassenger(self, passenger_id):
        for passenger in self.__passengerList:
            if passenger.getID() == passenger_id:
                self.__passengerList.remove(passenger)
                return f"Passenger {passenger.getName()} removed from the flight."
        return "Passenger not found in the flight."

    def searchPassenger(self, passenger_id):
        for passenger in self.__passengerList:
            if passenger.getID() == passenger_id:
                return passenger
        return "Passenger not found in the flight."
    
    def calculateTotalPassengers(self):
        return len(self.__passengerList)
    
