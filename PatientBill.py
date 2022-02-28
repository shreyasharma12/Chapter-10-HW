from functools import total_ordering
import PatientClass as a
import ProcedureClass as b


def main(): 


    my_patient = a.Patient(1,"Matt Jones","123 Main st, Waco TX 76706","254-555-7415",'TRUE')


    my_procedure1 = b.Procedure("Physical Exam","2/15/2022","Dr. Irvine",250,1)
    my_procedure2 = b.Procedure("MRI","2/15/2022","Dr. Hamilton",1500,1)
    my_procedure3 = b.Procedure("CT Scan","2/17/2022","Dr. Drey",1200,2)

    total_charges = 0


    print('*** Patient Bill *** ')
    print("Name:",my_patient.get_name()) 
    print("Address:",my_patient.get_address())
    print("Phone:",my_patient.get_phone())

    print()
    print("Procedure:",my_procedure1.get_procedurename())
    print("Date:",my_procedure1.get_proceduredate())
    print("Practitioner:",my_procedure1.get_practitoner())
    print("Charge: $",format(my_procedure1.get_charges(),'.2f'))

    print()
    print("Procedure:",my_procedure2.get_procedurename())
    print("Date:",my_procedure2.get_proceduredate())
    print("Practitioner:",my_procedure2.get_practitoner())
    print("Charge: $",format(my_procedure2.get_charges(),'.2f'))


    
    if my_procedure1.get_NameID == my_patient.get_patientID():
        total_charges += my_procedure1.get_charges()

    if my_procedure2.get_NameID() == my_patient.get_patientID():
        total_charges += my_procedure2.get_charges()

    if my_procedure3.get_NameID() == my_patient.get_patientID():
        total_charges += my_procedure3.get_charges()

    if my_patient.get_veteran_status() == "TRUE":
        total_charges*= .60

    
    print()
    print("Total Charges: $",format(total_charges,',.2f'))
    
main()