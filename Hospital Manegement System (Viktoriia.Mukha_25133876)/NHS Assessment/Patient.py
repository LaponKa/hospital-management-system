class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms
        pass
        self.__doctor = None
       

    
    def full_name(self) :
        """full name is first_name and surname"""
        return f"{self.__first_name} {self.__surname}"
        pass


    def get_doctor(self) :
        return self.__doctor
        pass

    def set_doctor(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        print(f"The symptoms for {self.full_name()} are: {self.__symptoms}")
        pass
    
    def get_surname(self):
        return self.__surname
    
    def get_age(self):
        return self.__age

    def get_mobile(self):
        return self.__mobile

    def get_symptoms(self):
        return self.__symptoms
    
    def get_postcode(self):
        return self.__postcode

    def __str__(self):
        if self.__doctor is None:
            doctor_name = "Not assigned"
        else:
            doctor_name = self.__doctor.full_name()
    
        return f'{self.full_name():^30}|{doctor_name:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
