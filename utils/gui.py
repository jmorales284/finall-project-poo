import tkinter as tk
from tkinter import messagebox
from entities.flight import Flight
from entities.airline import Airline
from entities.passenger import Passenger




#Instanciamos los objetos
airline = Airline()
airline.upload()
airline.uploadPassengers()



class AirlineApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Airline App")
        
        # datos del vuelo
        self.entryFlightNumber = None
        self.entryOrigin = None
        self.entryArrival = None
        self.entryPlaneID = None
        self.entryPilotName = None
        self.entryFlightTime = None
        self.entryFlightDate = None
        self.entryStatus = None

        # Ventana de datos
        self.dataWindow = None

        # Datos del pasajero
        self.entryID = None
        self.entryName = None
        self.entryPhone = None

        # Agregar widgets
        self.label = tk.Label(master, text="¡Bienvenido a la Aerolínea!")
        self.label.pack(pady=10)

        self.button_add_flight = tk.Button(master, text="Adicionar vuelo", command=self.graphicsAddFlight)
        self.button_add_flight.pack(pady=5)

        self.button_add_passenger = tk.Button(master, text="Adicionar pasajero", command=self.graphicsAddPassenger)
        self.button_add_passenger.pack(pady=5)

        self.button_passenger_flights = tk.Button(master, text="Consultar pasajeros de vuelo", command=self.graphicsPassengerFlights)
        self.button_passenger_flights.pack(pady=5)

        self.button_scheduled_flights = tk.Button(master, text="Consultar vuelos programados", command=self.scheduledFlights)
        self.button_scheduled_flights.pack(pady=5)

        self.button_finished_flights = tk.Button(master, text="Consultar vuelos realizados", command=self.finishedFlights)
        self.button_finished_flights.pack(pady=5)

        self.button_people_flights = tk.Button(master, text="Consultar vuelos de una persona", command=self.graphicsPeopleFlights)
        self.button_people_flights.pack(pady=5)

        self.button_change_flight_status = tk.Button(master, text="Modificar estado de vuelo a realizado", command=self.graphicsChangeFlightStatus)
        self.button_change_flight_status.pack(pady=5)

        self.button_change_passenger_status = tk.Button(master, text="Registrar pasajero a bordo", command=self.graphicsChangePassengerStatus)
        self.button_change_passenger_status.pack(pady=5)

        self.button_change_passenger_status = tk.Button(master, text="Calcular total de pasajeros", command=self.graphicsCalculateTotalPassengers)
        self.button_change_passenger_status.pack(pady=5)

        self.button_exit = tk.Button(master, text="Salir", command=self.master.destroy)
        self.button_exit.pack(pady=10)

    #Funciones graficas
    def graphicsAddFlight(self):
        self.dataWindow = tk.Toplevel(self.master)
        self.dataWindow.title("Ingresar Datos de Vuelo")

        tk.Label(self.dataWindow, text="Número de Vuelo:").grid(row=0, column=0)
        self.entryFlightNumber = tk.Entry(self.dataWindow)
        self.entryFlightNumber.grid(row=0, column=1)

        tk.Label(self.dataWindow, text="Origen:").grid(row=1, column=0)
        self.entryOrigin = tk.Entry(self.dataWindow)
        self.entryOrigin.grid(row=1, column=1)

        tk.Label(self.dataWindow, text="Destino:").grid(row=2, column=0)
        self.entryArrival = tk.Entry(self.dataWindow)
        self.entryArrival.grid(row=2, column=1)

        tk.Label(self.dataWindow, text="ID del Avión:").grid(row=3, column=0)
        self.entryPlaneID = tk.Entry(self.dataWindow)
        self.entryPlaneID.grid(row=3, column=1)

        tk.Label(self.dataWindow, text="Nombre del Piloto:").grid(row=4, column=0)
        self.entryPilotName = tk.Entry(self.dataWindow)
        self.entryPilotName.grid(row=4, column=1)

        tk.Label(self.dataWindow, text="Hora del Vuelo:").grid(row=5, column=0)
        self.entryFlightTime = tk.Entry(self.dataWindow)
        self.entryFlightTime.grid(row=5, column=1)

        tk.Label(self.dataWindow, text="Fecha del Vuelo:").grid(row=6, column=0)
        self.entryFlightDate = tk.Entry(self.dataWindow)
        self.entryFlightDate.grid(row=6, column=1)

        tk.Label(self.dataWindow, text="Estado del Vuelo:").grid(row=7, column=0)
        self.entryStatus = tk.Entry(self.dataWindow)
        self.entryStatus.grid(row=7, column=1)

        tk.Button(self.dataWindow, text="Guardar", command=self.addFlight).grid(row=8, column=0, columnspan=2)


    def graphicsAddPassenger(self):
        self.dataWindow = tk.Toplevel(self.master)
        self.dataWindow.title("Ingresar Datos de Pasajero")

        tk.Label(self.dataWindow, text="ID del Pasajero:").grid(row=0, column=0)
        self.entryID = tk.Entry(self.dataWindow)
        self.entryID.grid(row=0, column=1)

        tk.Label(self.dataWindow, text="Nombre del Pasajero:").grid(row=1, column=0)
        self.entryName = tk.Entry(self.dataWindow)
        self.entryName.grid(row=1, column=1)

        tk.Label(self.dataWindow, text="Teléfono del Pasajero:").grid(row=2, column=0)
        self.entryPhone = tk.Entry(self.dataWindow)
        self.entryPhone.grid(row=2, column=1)

        tk.Label(self.dataWindow, text="Numero de vuelo:").grid(row=3, column=0)
        self.entryFlightNumber = tk.Entry(self.dataWindow)
        self.entryFlightNumber.grid(row=3, column=1)

        tk.Button(self.dataWindow, text="Guardar", command=self.addPassenger).grid(row=4, column=0, columnspan=2)

    def graphicsPassengerFlights(self):
        self.dataWindow = tk.Toplevel(self.master)
        self.dataWindow.title("buscar pasajeros de vuelo")

        tk.Label(self.dataWindow, text="Número de Vuelo:").grid(row=0, column=0)
        self.entryFlightNumber = tk.Entry(self.dataWindow)
        self.entryFlightNumber.grid(row=0, column=1)

        tk.Button(self.dataWindow, text="Buscar", command=self.passengerFlights).grid(row=1, column=0, columnspan=2)

    def graphicsPeopleFlights(self):
        self.dataWindow = tk.Toplevel(self.master)
        self.dataWindow.title("buscar vuelos de una persona")

        tk.Label(self.dataWindow, text="ID del Pasajero:").grid(row=0, column=0)
        self.entryID = tk.Entry(self.dataWindow)
        self.entryID.grid(row=0, column=1)

        tk.Button(self.dataWindow, text="Buscar", command=self.peopleFlights).grid(row=1, column=0, columnspan=2)

    def graphicsChangeFlightStatus(self):
        self.dataWindow = tk.Toplevel(self.master)
        self.dataWindow.title("Modificar estado de vuelo")

        tk.Label(self.dataWindow, text="Número de Vuelo:").grid(row=0, column=0)
        self.entryFlightNumber = tk.Entry(self.dataWindow)
        self.entryFlightNumber.grid(row=0, column=1)

        tk.Button(self.dataWindow, text="Guardar", command=self.changeFlightStatus).grid(row=2, column=0, columnspan=2)


    def graphicsChangePassengerStatus(self):
        self.dataWindow = tk.Toplevel(self.master)
        self.dataWindow.title("Registrar pasajero a bordo")

        tk.Label(self.dataWindow, text="Número de Vuelo:").grid(row=0, column=0)
        self.entryFlightNumber = tk.Entry(self.dataWindow)
        self.entryFlightNumber.grid(row=0, column=1)

        tk.Label(self.dataWindow, text="ID del Pasajero:").grid(row=1, column=0)
        self.entryID = tk.Entry(self.dataWindow)
        self.entryID.grid(row=1, column=1)

        tk.Button(self.dataWindow, text="Guardar", command=self.changePassengerStatus).grid(row=2, column=0, columnspan=2)

    def graphicsCalculateTotalPassengers(self):
        self.dataWindow = tk.Toplevel(self.master)
        self.dataWindow.title("Calcular total de pasajeros")

        tk.Label(self.dataWindow, text="Número de Vuelo:").grid(row=0, column=0)
        self.entryFlightNumber = tk.Entry(self.dataWindow)
        self.entryFlightNumber.grid(row=0, column=1)

        tk.Button(self.dataWindow, text="Calcular", command=self.calculateTotalPassengers).grid(row=2, column=0, columnspan=2)


    #Funciones logicas
    def addFlight(self):
        if not self.entryFlightNumber.get() or not self.entryOrigin.get() or not self.entryArrival.get() or not self.entryPlaneID.get() or not self.entryPilotName.get() or not self.entryFlightTime.get() or not self.entryFlightDate.get() or not self.entryStatus.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        flights = Flight()

        flights.setFlightNumber(self.entryFlightNumber.get())
        flights.setOrigin(self.entryOrigin.get())
        flights.setArrival(self.entryArrival.get())
        flights.setPlaneID(self.entryPlaneID.get())
        flights.setPilotName(self.entryPilotName.get())
        flights.setFlightTime(self.entryFlightTime.get())
        flights.setFlightDate(self.entryFlightDate.get())
        flights.setStatus(self.entryStatus.get())

        if not (flights.getFlightNumber() and flights.getOrigin() and flights.getArrival() and flights.getPlaneID() and flights.getPilotName() and flights.getFlightTime() and flights.getFlightDate() and flights.getStatus()):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        airline.addToTheList(flights)
        messagebox.showinfo("Hecho", "Vuelo agregado con éxito")
        with open('VUELOS.txt', 'a') as file:
            file.write(f"{flights.getFlightNumber()} {flights.getOrigin()} {flights.getArrival()} "
                       f"{flights.getPlaneID()} {flights.getPilotName()} {flights.getFlightTime()} "
                       f"{flights.getFlightDate()} {flights.getStatus()}\n")
        self.dataWindow.destroy()
        
    def addPassenger(self):
        if not self.entryID.get() or not self.entryName.get() or not self.entryPhone.get() or not self.entryFlightNumber.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        passenger = Passenger()
        passenger.setID(self.entryID.get())
        passenger.setName(self.entryName.get())
        passenger.setPhone(self.entryPhone.get())
        passenger.setStatus(1)

        flightNumber = self.entryFlightNumber.get()

        flight = next((f for f in airline.getFlight() if f.getFlightNumber() == flightNumber), None)
        print(flight)
        if flight:
            flight.addToTheList(passenger)
            print(flight.getPassengerList())
            messagebox.showinfo("Hecho", "Pasajero agregado al vuelo con éxito")
            # Cierra la ventana después de acceder a los valores
            with open('PASAJEROS.txt', 'a') as file:
                file.write(f"{passenger.getID()} {passenger.getName()} {passenger.getPhone()} {passenger.getStatus()} {flight.getFlightNumber()}\n")
            self.dataWindow.destroy()
        else:
            messagebox.showerror("Error", f"No se encontró un vuelo con el número {flightNumber}")


    def passengerFlights(self):
        if not self.entryFlightNumber.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        flightNumber = self.entryFlightNumber.get()
        flight = next((f for f in airline.getFlight() if f.getFlightNumber() == flightNumber), None)
        print(flight)
        if flight:
            passengers = flight.getPassengerList()
            print(passengers)
            if not passengers:
                messagebox.showinfo("Información", f"No hay pasajeros para el vuelo con número {flightNumber}")
                self.dataWindow.destroy()
                return
            self.dataWindow = tk.Toplevel(self.master)
            self.dataWindow.title("Pasajeros de Vuelo")
            tk.Label(self.dataWindow, text="Información de Pasajeros").grid(row=0, column=0)
            for passenger in passengers:
                passengerInfo = f"{passenger.getID()} {passenger.getName()} {passenger.getPhone()} {passenger.getStatus()}"
                tk.Label(self.dataWindow, text=passengerInfo).grid(row=passengers.index(passenger)+1, column=0)
        else:
            messagebox.showerror("Error", f"No se encontró un vuelo con el número {flightNumber}")
            self.dataWindow.destroy()
        
        
    def scheduledFlights(self):
        scheduledFlights = airline.ScheduledFlights()
        print(scheduledFlights)
        if not scheduledFlights:
            messagebox.showinfo("Información", "No hay vuelos programados")
            return
        self.dataWindow = tk.Toplevel(self.master)
        self.dataWindow.title("Vuelos Programados")
        tk.Label(self.dataWindow, text="Número de Vuelo").grid(row=0, column=0)

        for flight in scheduledFlights:
            flightInfo = f"{flight.getFlightNumber()} {flight.getOrigin()} {flight.getArrival()} {flight.getPlaneID()} {flight.getPilotName()} {flight.getFlightTime()} {flight.getFlightDate()} {flight.getStatus()}"
            tk.Label(self.dataWindow, text=flightInfo).grid(row=scheduledFlights.index(flight)+1, column=0)

    def finishedFlights(self):
        finishedFlights = airline.finishedFlights()
        print(finishedFlights)
        if not finishedFlights:
            messagebox.showinfo("Información", "No hay vuelos realizados")
            return
        self.dataWindow = tk.Toplevel(self.master)
        self.dataWindow.title("Vuelos realizados")
        tk.Label(self.dataWindow, text="Número de Vuelo").grid(row=0, column=0)

        for flight in finishedFlights:
            flightInfo = f"{flight.getFlightNumber()} {flight.getOrigin()} {flight.getArrival()} {flight.getPlaneID()} {flight.getPilotName()} {flight.getFlightTime()} {flight.getFlightDate()} {flight.getStatus()}"
            tk.Label(self.dataWindow, text=flightInfo).grid(row=finishedFlights.index(flight)+1, column=0)

    def peopleFlights(self):
    
        if not self.entryID.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        passengerID = self.entryID.get()   
        peopleFlights = airline.peopleFlights(passengerID)
        print(peopleFlights)
        if not peopleFlights:
            messagebox.showinfo("Información", f"No hay vuelos para la persona con ID {passengerID}")
            self.dataWindow.destroy()
            return

        self.dataWindowResults = tk.Toplevel(self.master)
        self.dataWindowResults.title("Vuelos de una Persona")

        tk.Label(self.dataWindowResults, text="Informacion de Vuelos").grid(row=0, column=0)

        for flight in peopleFlights:
            flightInfo = f"{flight.getFlightNumber()} {flight.getOrigin()} {flight.getArrival()} {flight.getPlaneID()} {flight.getPilotName()} {flight.getFlightTime()} {flight.getFlightDate()} {flight.getStatus()}"
            tk.Label(self.dataWindowResults, text=flightInfo).grid(row=peopleFlights.index(flight)+1, column=0)
        self.dataWindow.destroy()


    def changeFlightStatus(self):
        if not self.entryFlightNumber.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        flightNumber = self.entryFlightNumber.get()
        flight = next((f for f in airline.getFlight() if f.getFlightNumber() == flightNumber), None)
        print(flight)
        if flight:
            if flight.getStatus() == '1' or flight.getStatus() == 1:
                messagebox.showerror("Error", f"El vuelo {flightNumber} ya está registrado como realizado")
                self.dataWindow.destroy()
                return
            flight.setStatus(1)
            for passenger in flight.getPassengerList():
                passenger.setStatus(2)
            messagebox.showinfo("Hecho", f"El estado del vuelo {flightNumber} ha sido modificado")
            self.dataWindow.destroy()
            try:
                with open("VUELOS.txt", 'w') as file:
                    for flight in airline.getFlight():
                        file.write(f"{flight.getFlightNumber()} {flight.getOrigin()} {flight.getArrival()} "
                                   f"{flight.getPlaneID()} {flight.getPilotName()} {flight.getFlightTime()} "
                                   f"{flight.getFlightDate()} {flight.getStatus()}\n")
            except FileNotFoundError:
                print("El archivo VUELOS.TXT no se encontró.")
            except Exception as e:
                print(f"Error: {e}")

            try:
                with open("PASAJEROS.txt", 'w') as file:
                    for flight in airline.getFlight():
                        for passenger in flight.getPassengerList():
                            file.write(f"{passenger.getID()} {passenger.getName()} {passenger.getPhone()} {passenger.getStatus()} {flight.getFlightNumber()}\n")
            except FileNotFoundError:
                print("El archivo PASAJEROS.TXT no se encontró.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            messagebox.showerror("Error", f"No se encontró un vuelo con el número {flightNumber}")
            self.dataWindow.destroy()


    def changePassengerStatus(self):
        if not self.entryID.get() or not self.entryFlightNumber.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        passengerID = self.entryID.get()
        flightNumber = self.entryFlightNumber.get()
        flight = next((f for f in airline.getFlight() if f.getFlightNumber() == flightNumber), None)
        print(flight)
        if flight:
            passengers = flight.getPassengerList()
            print(passengers)
            if not passengers:
                messagebox.showinfo("Información", f"No hay pasajeros para el vuelo con número {flightNumber}")
                self.dataWindow.destroy()
                return
            passenger = next((p for p in passengers if p.getID() == passengerID), None)
            if passenger:
                if passenger.getStatus() == '2' or passenger.getStatus() == 2:
                    messagebox.showerror("Error", f"El pasajero {passengerID} ya está registrado como a bordo")
                    self.dataWindow.destroy()
                    return
                passenger.setStatus(2)
                messagebox.showinfo("Hecho", f"El pasajero {passengerID} ha sido registrado como a bordo")
                self.dataWindow.destroy()
                try:
                    with open("PASAJEROS.txt", 'w') as file:
                        for flight in airline.getFlight():
                            for passenger in flight.getPassengerList():
                                file.write(f"{passenger.getID()} {passenger.getName()} {passenger.getPhone()} {passenger.getStatus()} {flight.getFlightNumber()}\n")
                except FileNotFoundError:
                    print("El archivo PASAJEROS.TXT no se encontró.")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                messagebox.showerror("Error", f"No se encontró un pasajero con el ID {passengerID}")
                self.dataWindow.destroy()
        else:
            messagebox.showerror("Error", f"No se encontró un vuelo con el número {flightNumber}")
            self.dataWindow.destroy()

    def calculateTotalPassengers(self):
        if not self.entryFlightNumber.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        flightNumber = self.entryFlightNumber.get()
        flight = next((f for f in airline.getFlight() if f.getFlightNumber() == flightNumber), None)
        print(flight)
        if flight:
            passengers = flight.getPassengerList()
            print(passengers)
            if not passengers:
                messagebox.showinfo("Información", f"No hay pasajeros para el vuelo con número {flightNumber}")
                self.dataWindow.destroy()
                return
            self.dataWindow = tk.Toplevel(self.master)
            self.dataWindow.title("Total de Pasajeros")
            tk.Label(self.dataWindow, text="Información de Pasajeros").grid(row=0, column=0)
            tk.Label(self.dataWindow, text=f"Total de pasajeros: {len(passengers)}").grid(row=1, column=0)
        else:
            messagebox.showerror("Error", f"No se encontró un vuelo con el número {flightNumber}")
            self.dataWindow.destroy()

