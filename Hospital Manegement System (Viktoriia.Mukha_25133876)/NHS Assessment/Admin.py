from Doctor import Doctor


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address
        self.__discharged_patients = []

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if username == self.__username and password == self.__password:
            print("You are logged in")
            return True
        else:
            return False
        pass

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        return self.__first_name, self.__surname, self.__speciality
        pass

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        

        op = int(input("Enter option(1 / 2 / 3 / 4): "))
        pass


        # register
        if op == 1:
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name = input("Enter the first name: ")
            surname = input("Enter the surname: ")
            speciality = input("Enter the speciality: ")
            pass
            
        
            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    if name_exists:
                        return
                    pass # save time and end the loop

            doctors.append(Doctor(first_name, surname, speciality))
            
            pass# add the doctor ...
                                                         # ... to the list of doctors
            print('Doctor registered.')

        # View
        elif op == 2:
            print("-----List of Doctors-----")
            self.view(doctors)
            pass

        # Update
        elif op == 3:
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
        
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    if self.find_index(index, doctors):
                        break
                    else:
                        print("Doctor not found")
                except ValueError:
                    print('Invalid ID')
        
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
        
            field = int(input('Input: '))
        
            if field == 1:
                new_name = input('New first name: ')
                doctors[index].set_first_name(new_name)
        
            elif field == 2:
                new_surname = input('New surname: ')
                doctors[index].set_surname(new_surname)
        
            elif field == 3:
                new_speciality = input('New speciality: ')
                doctors[index].set_speciality(new_speciality)
        
            print("Doctor details updated.")

        
        # Delete
        elif op == 4:
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            while True:
                    doctor_index = input('Enter the ID of the doctor to be deleted: ')
            
                    try:
                        doctor_index = int(doctor_index) - 1
                        if doctor_index in range(len(doctors)):
                            del doctors[doctor_index]
                            print('Doctor deleted.')
                            break
                        else:
                            print('ID not found. Try again.')
                    except ValueError:
                        print('Invalid input. Please enter a number.')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode     | Symptoms ')
        self.view(patients)
        pass
    
    def get_discharged_patients(self):
        """Returns the list of discharged patients"""
        return self.__discharged_patients

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode     | Symptoms ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                patients[patient_index].set_doctor(doctors[doctor_index])
                doctors[doctor_index].add_patient(patients[patient_index])
                pass
                
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        patient_index = input('Please enter the patient ID: ')

        try:
            index = int(patient_index) - 1
            if index in range(len(patients)):
                discharge_patients.append(patients[index])
                del patients[index]
                print("Patient discharged.")
                return
        except:
            pass 
        print("Invalid ID.")

    def view_discharge(self, discharged_patients):
        """Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients"""

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)
        pass

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            self.__username = input('Enter new username: ')
            pass

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            self.__address = input('Enter the new address: ')
            pass

        else:
            print('Invalid option chosen.')
            pass
        
    def group_patients_by_family(self, patients):
        """Allow patients of the same family be grouped together by Admin"""
        print("----- Patients Grouped by Family -----")
        
        # list of surname
        checked_surnames = []

        for p1 in patients:
            surname = p1.get_surname()
            
            if surname not in checked_surnames:
                family_members = []
                
                # find a patient with the same surname
                for p2 in patients:
                    if p2.get_surname() == surname:
                        family_members.append(p2.full_name())
                
                # if there is more than 1 patient with this surname
                if len(family_members) > 1:
                    print(f"\nFamily: {surname}")
                    for name in family_members:
                        print(f"  - {name}")
                    
                    # Add a surname to the list
                    checked_surnames.append(surname)

    def save_patients_to_file(self, patients):
        """Save the list of patients to a text file"""
        try:
            with open('patients.txt', 'w') as f:
                for p in patients:
                    line = f"{p.full_name()},{p.get_surname()}\n"
                    f.write(line)
            print("Patients data saved to patients.txt")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_patients_from_file(self):
        """Load and print patient names from the file (Task 10)"""
        print("----- Loading Patients From File -----")
        try:
            with open('patients.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print("No saved data found.")
            
    def relocate_patient(self, patients, doctors):
        """Relocate a patient to a new doctor"""
        print("----- Relocate Patient -----")
        self.view_patient(patients)
        
        try:
            p_index = int(input("Enter Patient ID to relocate: ")) - 1
            if p_index not in range(len(patients)):
                print("Invalid Patient ID.")
                return

            current_patient = patients[p_index]
            old_doctor = current_patient.get_doctor()

            print("----- Available Doctors -----")
            self.view(doctors)
            d_index = int(input("Enter New Doctor ID: ")) - 1
            
            if d_index in range(len(doctors)):
                new_doctor = doctors[d_index]

                # Remove patient from the old doctor's list if they had one
                if old_doctor is not None:
                    old_doctor.remove_patient(current_patient)

                # Link patient to the new doctor
                current_patient.set_doctor(new_doctor)

                # Add patient to the new doctor's list
                new_doctor.add_patient(current_patient)
                
                print(f"Patient {current_patient.full_name()} relocated to Dr. {new_doctor.full_name()}.")
            else:
                print("Invalid Doctor ID.")
        except ValueError:
            print("Please enter valid numeric IDs.")
            
    def generate_management_report(self, doctors, patients):
        """Creates a management report"""
        print("\n----- Hospital Management Report -----")
        
        # a) Total number of doctors in the system
        total_doctors = len(doctors)
        print(f"Total number of doctors: {total_doctors}")

        # b) Total number of patients per doctor
        print("\nPatients per doctor:")
        for dr in doctors:
            print(f"- Dr. {dr.full_name()}: {dr.get_patient_count()} patients")
        
        # c) Total number of appointments per month per doctor
        print("\nAppointments per doctor for the current month (April):")
        for dr in doctors:
            count = dr.get_appointments_per_month("April")
            print(f"- Dr. {dr.full_name()}: {count} appointments")
        
        # d) Total number of patients based on the illness type
        print("\nPatients based on illness type:")
        illness_counts = {}
        for p in patients:
            # We assume symptoms are stored in __symptoms attribute
            # Using a simple way to count occurrences
            symptom = getattr(p, '_Patient__symptoms', 'Unknown')
            if symptom not in illness_counts:
                illness_counts[symptom] = 0
            illness_counts[symptom] += 1
        
        for illness, count in illness_counts.items():
            print(f"- {illness}: {count} patients")
            
    def view_report_diagrams(self, doctors, patients):
        """Displays text-based bar charts for the management report"""
        print("\n----- Management Report Diagrams -----")
        
        # Total number of doctors
        total_docs = len(doctors)
        print(f"\n TOTAL DOCTORS IN SYSTEM: {total_docs} ")
        
        # Diagram for Patients per Doctor
        print("\n1. Patients per Doctor:")
        for dr in doctors:
            count = dr.get_patient_count()
            # Each '*' represents 1 patient
            bar = '*' * count
            print(f"Dr. {dr.full_name():<15} | {bar} ({count})")

        # 2. Diagram for Illness types
        print("\n2. Patients by Illness Type:")
        illness_counts = {}
        for p in patients:
            symptom = getattr(p, '_Patient__symptoms', 'Unknown')
            illness_counts[symptom] = illness_counts.get(symptom, 0) + 1
        
        for illness, count in illness_counts.items():
            bar = '#' * count
            print(f"{illness:<18} | {bar} ({count})")

        # 3. Diagram for Appointments
        print("\n3. Appointments for April:")
        for dr in doctors:
            count = dr.get_appointments_per_month("April")
            bar = '=' * count
            print(f"Dr. {dr.full_name():<15} | {bar} ({count})")