#Hands-on 17
#Kian Mojami

import sqlite3
connect = sqlite3.connect('medicaldemo.db')
cursor = connect.cursor()

cursor.execute("select * from surgery")
surgeryRecords = cursor.fetchall()
for surgery in surgeryRecords:
    print(surgery)

cursor.execute("select * from doctor")
doctorRecords = cursor.fetchall()
for doctor in doctorRecords:
    print(doctor)

cursor.execute("select * from patient")
patientRecords = cursor.fetchall()
for patient in patientRecords:
    print(patient)

cursor.execute("Select patientFN, patientLN, doctorFN, doctorLN from patient, doctor where patient.doctorID = doctor.doctorID")
info = cursor.fetchall()
for patientFN, patientLN, doctorFN, doctorLN in info:
    print(f'Patient: {patientFN} {patientLN}   Doctor: {doctorFN} {doctorLN}')

cursor.execute("Select patientFN, patientLN, surgeryDesc, doctorFN, doctorLN from patient, surgery, doctor where surgery.doctorID = doctor.doctorID and surgery.patientID = patient.patientID order by surgeryDesc")
surgery = cursor.fetchall()
for patientFN, patientLN, surgeryDesc, doctorFN, doctorLN in surgery:
    print(f"Patient: {patientFN} {patientLN}   Surgery: {surgeryDesc}   Doctor: {doctorFN} {doctorLN}")

cursor.execute("Select surgeryDesc, sum(surgerycost) Cost from surgery group by surgeryDesc")
cost = cursor.fetchall()
total = 0
for surgeryDesc, surgerycost in cost:
    print(f"Surgery: {surgeryDesc}  Cost: ${surgerycost}")
    total = total + float(surgerycost)
print(f"The total cost is ${total}")

connect.close()
