from entities.flight import Flight

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




