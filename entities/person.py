#Clase de persona
class Person:
    def __init__(self):
        self.__ID 
        self.__name 
        self.__phone 

    # Getters
    def getID(self):
        return self.__ID

    def getName(self):
        return self.__name

    def getPhone(self):
        return self.__phone

    # Setters
    def setID(self, new_ID):
        self.__ID = new_ID

    def setName(self, new_name):
        self.__name = new_name

    def setPhone(self, new_phone):
        self.__phone = new_phone
