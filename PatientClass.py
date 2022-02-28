

class Patient:

    def __init__(self,patientID,name,address,phone,veteran_status):
        self.__IDNumber = int(patientID)
        self.__name = name
        self.__address = address
        self.__phonenumber = phone
        self.__veteranstatus = veteran_status

    def get_patientID(self):
        return self.__IDNumber

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phonenumber

    def get_veteran_status(self):
        return self.__veteranstatus