class Procedure:
    def __init__(self,procedurename,proceduredate,practitoner,charges,NameID):
        self.__procedure = procedurename
        self.__proddate = proceduredate
        self.__practitoner = practitoner
        self.__charges = int(charges)
        self.__IDNumber = int(NameID)


    def get_procedurename(self):
        return self.__procedure

    def get_proceduredate(self):
        return self.__proddate

    def get_practitoner(self):
        return self.__practitoner

    def get_charges(self):
        return self.__charges

    def get_NameID(self):
        return self.__IDNumber