from entities.flight import Flight
from entities.passenger import Passenger

class Airline:
    def __init__(self):
        self.__flightList = []
    
    def addToTheList(self, flight):
        self.__flightList.append(flight)

    def getFlight(self):
        return self.__flightList
    
    def ScheduledFlights(self):
        scheduledFlights = []
        try:
            with open("VUELOS.txt", 'r') as file:
                for line in file:
                    flightData = line.strip().split()
                    if len(flightData) >= 8 and flightData[7] == '0':
                        flight = Flight()
                        flight.setFlightNumber(flightData[0])
                        flight.setOrigin(flightData[1])
                        flight.setArrival(flightData[2])
                        flight.setPlaneID(flightData[3])
                        flight.setPilotName(flightData[4])
                        flight.setFlightTime(flightData[5])
                        flight.setFlightDate(flightData[6])
                        flight.setStatus(flightData[7])
                        scheduledFlights.append(flight)
        except FileNotFoundError:
            print("El archivo VUELOS.TXT no se encontró.")

        return scheduledFlights
    
    def finishedFlights(self):
        finishedFlights = []
        try:
            with open("VUELOS.txt", 'r') as file:
                for line in file:
                    flightData = line.strip().split()
                    if len(flightData) >= 8 and flightData[7] == '1':
                        flight = Flight()
                        flight.setFlightNumber(flightData[0])
                        flight.setOrigin(flightData[1])
                        flight.setArrival(flightData[2])
                        flight.setPlaneID(flightData[3])
                        flight.setPilotName(flightData[4])
                        flight.setFlightTime(flightData[5])
                        flight.setFlightDate(flightData[6])
                        flight.setStatus(flightData[7])
                        finishedFlights.append(flight)
        except FileNotFoundError:
            print("El archivo VUELOS.TXT no se encontró.")
        
        return finishedFlights
    
    def upload(self):
        try:
            with open("VUELOS.txt", 'r') as file:
                for line in file:
                    flightData = line.strip().split()
                    if len(flightData) >= 8:
                        flightNumber = flightData[0]

                        # Verifica si el vuelo ya está en la lista
                        existing_flight = next((f for f in self.__flightList if f.getFlightNumber() == flightNumber), None)

                        if not existing_flight:
                            flight = Flight()
                            flight.setFlightNumber(flightData[0])
                            flight.setOrigin(flightData[1])
                            flight.setArrival(flightData[2])
                            flight.setPlaneID(flightData[3])
                            flight.setPilotName(flightData[4])
                            flight.setFlightTime(flightData[5])
                            flight.setFlightDate(flightData[6])
                            flight.setStatus(flightData[7])
                            self.addToTheList(flight)
        except FileNotFoundError:
            print("El archivo VUELOS.TXT no se encontró.")
        except Exception as e:
            print(f"Error: {e}")

    def uploadPassengers(self):
        try:
            with open("PASAJEROS.txt", 'r') as file:
                for line in file:
                    passengerData = line.strip().split()
                    if len(passengerData) >= 5:
                        passenger = Passenger()
                        passenger.setID(passengerData[0])
                        passenger.setName(passengerData[1])
                        passenger.setPhone(passengerData[2])
                        passenger.setStatus(passengerData[3])
                        flightNumber = passengerData[4]

                        # Buscar el vuelo correspondiente en la lista
                        flight = next((f for f in self.__flightList if f.getFlightNumber() == flightNumber), None)

                        if flight:
                            flight.addToTheList(passenger)
        except FileNotFoundError:
            print("El archivo PASAJEROS.TXT no se encontró.")
        except Exception as e:
            print(f"Error: {e}")

    
    def peopleFlights(self, ID):
        peopleFlights = []
    
        for flight in self.__flightList:
            passengers = flight.getPassengerList()
    
            for passenger in passengers:
                if passenger.getID() == ID:
                    peopleFlights.append(flight)
    
        print(f"People flights for ID {ID}: {peopleFlights}")
        return peopleFlights

        

    def passengerFlight(self, flightNumber):
        for flight in self.__flightList:
            if flight.getFlightNumber() == flightNumber:
                return flight.getPassengerList()
        print(f"Flight {flightNumber} not found.")
        