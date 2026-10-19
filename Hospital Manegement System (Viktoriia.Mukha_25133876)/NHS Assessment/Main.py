# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234', 'Caugh'), Patient('Mike','Jones', 37,'07555551234','L2 2AB', 'Back pain'), Patient('David','Smith', 15, '07123456789','C1 ABC', 'Headache')]
    discharged_patients = []
    doctors[0].add_appointment("April")
    doctors[0].add_appointment("May")
    doctors[1].add_appointment("January")
    doctors[2].add_appointment("March")

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Group patients by family')
        print(' 7- Save patients to file')
        print(' 8- Load patients from file')
        print(' 9- Relocate patient to another doctor')
        print(' 10- Generate Management Report')
        print(' 11- View Report Diagrams')
        print(' 12- Launch Report')
        print(' 0- Quit')
        

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
          admin.doctor_management(doctors)
          pass

        elif op == '2':
            # 2- View or discharge patients
            admin.view_patient(patients)
            pass

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    admin.discharge(patients, discharged_patients)
                    pass

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            admin.view_discharge(discharged_patients)
            pass

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()
            
            # 6- Group patient by family surname
        elif op == '6':
            admin.group_patients_by_family(patients)
            
            # 7- Save patients to the file
        elif op == '7':
            admin.save_patients_to_file(patients)
            
            # 8- Load patients from the file
        elif op == '8':
            admin.load_patients_from_file()
            
            # 9- Relocate patient to another doctor
        elif op == '9':
            admin.relocate_patient(patients, doctors)
        
            # 10- Generates a management report
        elif op == '10':
            admin.generate_management_report(doctors, patients)
        
            # 11- View report diagrams
        elif op == '11':
            admin.view_report_diagrams(doctors, patients)
            
        elif op == '12':
            root = tk.Tk()
            app = HospitalGUI(root, admin, doctors, patients)
            root.mainloop()
        
            # 0 - Quit
        elif op == '0':
            print('You are logged out')
            
            running = False
            pass

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

class HospitalGUI:
    def __init__(self, root, admin, doctors, patients):
        self.root = root
        self.admin = admin
        self.doctors = doctors
        self.patients = patients
        
        # Window Setup
        self.root.title("Hospital Management System - Admin Portal")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f0f0f0")

        # Header Section
        header = tk.Frame(self.root, bg="#2c3e50", height=60)
        header.pack(fill="x")
        tk.Label(header, text="HOSPITAL DASHBOARD", fg="white", bg="#2c3e50", 
                 font=("Helvetica", 18, "bold")).pack(pady=15)

        # Main Layout
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Left Column: Buttons
        menu_frame = tk.Frame(main_frame, bg="#f0f0f0")
        menu_frame.pack(side="left", fill="y", padx=10)

        tk.Label(menu_frame, text="Menu", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)
        
        btn_style = {"width": 25, "font": ("Arial", 10), "pady": 5}
        
        tk.Button(menu_frame, text=" Register Doctor", command=self.gui_register_doctor, **btn_style).pack(pady=5)
        tk.Button(menu_frame, text=" Assign Doctor", command=self.gui_assign_doctor, **btn_style).pack(pady=5)
        tk.Button(menu_frame, text=" Relocate Patient", command=self.gui_relocate_patient, **btn_style).pack(pady=5)
        tk.Button(menu_frame, text=" Management Stats", command=self.show_management_stats, **btn_style).pack(pady=5)
        tk.Button(menu_frame, text=" View All Patients", command=self.display_patients, **btn_style).pack(pady=5)
        tk.Button(menu_frame, text=" Doctor Workload", command=self.display_doctors, **btn_style).pack(pady=5)
        tk.Button(menu_frame, text=" Export Data to File", command=lambda: self.admin.save_patients_to_file(self.patients), **btn_style).pack(pady=5)
        
        tk.Button(menu_frame, text="Close Dashboard", command=self.root.destroy, bg="#e74c3c", fg="white", width=20).pack(side="bottom", pady=20)

        # Right Column: Data Display
        display_container = tk.LabelFrame(main_frame, text="Data Monitor", padx=10, pady=10)
        display_container.pack(side="right", fill="both", expand=True)

        self.txt_display = tk.Text(display_container, height=15, width=40, font=("Courier New", 10))
        self.txt_display.pack(fill="both", expand=True)

    def update_display(self, text):
        self.txt_display.delete('1.0', tk.END)
        self.txt_display.insert(tk.END, text)
        
    def gui_register_doctor(self):
        name = simpledialog.askstring("Input", "Enter Doctor First Name:")
        surname = simpledialog.askstring("Input", "Enter Doctor Surname:")
        speciality = simpledialog.askstring("Input", "Enter Speciality:")
    
        if name and surname and speciality:
            from Doctor import Doctor
            self.doctors.append(Doctor(name, surname, speciality))
            messagebox.showinfo("Success", f"Dr. {surname} registered!")
            self.display_doctors() 
    
    def gui_relocate_patient(self):
        p_idx = simpledialog.askinteger("Input", "Enter Patient ID from the monitor:")
        d_idx = simpledialog.askinteger("Input", "Enter New Doctor ID from the monitor:")
    
        if p_idx and d_idx:
            messagebox.showinfo("System", "Patient relocation processed.")
            
    def gui_assign_doctor(self):
        p_idx = simpledialog.askinteger("Input", "Enter Patient ID (from the list):")
        if p_idx is None: return # Користувач натиснув Cancel
        
        d_idx = simpledialog.askinteger("Input", "Enter Doctor ID (from the list):")
        if d_idx is None: return

        try:
            patient = self.patients[p_idx - 1]
            doctor = self.doctors[d_idx - 1]

            doctor.add_patient(patient) 
            
            messagebox.showinfo("Success", f"Patient {patient.full_name()} assigned to Dr. {doctor.get_surname()}")
            self.display_doctors() # Оновлюємо монітор, щоб побачити зміни в навантаженні
            
        except IndexError:
            messagebox.showerror("Error", "Invalid Patient or Doctor ID!")

    def show_management_stats(self):
        stats = f"----- Hospital Management Report -----\n"
        stats += f"Total number of doctors: {len(self.doctors)}\n\n"
        
        stats += "Patients per doctor:\n"
        for dr in self.doctors:
            stats += f"- Dr. {dr.full_name()}: {dr.get_patient_count()} patients\n"
        
        stats += "\nAppointments per doctor for the current month (April):\n"
        for dr in self.doctors:
            count = dr.get_appointments_per_month("April")
            stats += f"- Dr. {dr.full_name()}: {count} appointments\n"
            
        stats += "\nPatients based on illness type:\n"
        illness_counts = {}
        for p in self.patients:
            symptom = p.get_symptoms()
            illness_counts[symptom] = illness_counts.get(symptom, 0) + 1
        
        for illness, count in illness_counts.items():
            stats += f"- {illness}: {count} patients\n"
            
        self.update_display(stats)

    def display_patients(self):
        header = f"{'ID':<3} | {'FULL NAME':<18} |  {'AGE':<4} | {'MOBILE':<12} | {'POSTCODE':<8} | {'SYMPTOMS'}\n"
        separator = "-" * 75 + "\n"
        output = header + separator
        
        for i, p in enumerate(self.patients):
            output += (f"{i+1:<3} | {p.full_name():<18} | {p.get_age():<4} | {p.get_mobile():<12} | {p.get_postcode():<8} | {p.get_symptoms()}\n")
            
        self.update_display(output)
        
    def display_doctors(self):
        header = f"{'ID':<3} | {'DOCTOR NAME':<17} | {'SPECIALITY':<15} | {'PATIENTS'}\n"
        separator = "-" * 60 + "\n"
        output = header + separator
        
        for i, d in enumerate(self.doctors):
            output += (f"{i+1:<3} | {d.full_name():<17} | "
                       f"{d.get_speciality():<15} | {d.get_patient_count()}\n")
            
        self.update_display(output)



if __name__ == '__main__':
    main()
    