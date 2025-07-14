
import streamlit as st
import csv
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("your-credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Appointments").sheet1  
st.title("Clinic Appointment Booking")

# Input fields
parent_name = st.text_input("Parent's Full Name")
phone = st.text_input("Contact Number")
child_name = st.text_input("Child's Full Name")
age = st.text_input("Child's Age")
symptoms = st.text_area("Describe Your Child’s Symptoms")

if st.button("Book Appointment"):
    if parent_name and phone and child_name and age and symptoms:
        # Save to CSV file
        file_exists = os.path.isfile("appointments.csv")
        with open("appointments.csv", mode="a", newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Parent Name", "Contact Number", "Child Name", "Age", "Symptoms"])
            writer.writerow([parent_name, phone, child_name, age, symptoms])

        st.success("✅ Appointment booked successfully!")
    else:
        st.warning("Please fill all fields.")
st.caption("Created by Divisha Gupta | GitHub: @DivishaGupta2008|JAN 2025")