import mysql.connector
import streamlit as st
import datetime as dt
from datetime import date
from tabulate import tabulate

connect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "intern"
)

st.set_page_config(
    page_title = "Sample DB Connection",
    page_icon = "📕",
    layout = "wide"
)

def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

def main():
    st.title("Sample Form")
    data = st.sidebar.selectbox(label = "Operations", options = ["Insert", "Read", "Update"])
    if data == "Insert":
        st.subheader("Insert Data")
        
        # Name and Email in normal flow
        name = st.text_input("Enter your Name : ")
        email = st.text_input("Enter your Email : ")
        
        # DOB and Age in columns
        col1, col2 = st.columns(2)
        with col1:
            dob = st.date_input(
                "Enter your Date of Birth :",
                min_value=date(1900, 1, 1),
                max_value=date.today()
            )
        with col2:
            age = calculate_age(dob)
            st.number_input(
                "Enter your Age :",
                value=age,
                disabled=True
            )
            
        if st.button("Insert Data"):
            query = "INSERT INTO sample (name, age, email, date_of_birth) VALUES (%s, %s, %s, %s)"
            values = (name, age, email, dob)
            cursor = connect.cursor()
            cursor.execute(query, values)
            connect.commit()
            st.success("Data inserted successfully!")

    elif data == "Read":
        st.subheader("Read Data")
        if st.button("Show Data"):
            read()
    
    elif data == "Update":
        if st.button("Update Data"):
            update()
    
def read():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM sample")
    data = cursor.fetchall()
    headers = ['ID', 'Name', 'Email', 'Date of Birth', 'Age']
    
    st.dataframe(
        data,
        column_config={
            "0": "ID",
            "1": "Name",
            "2": "Email",
            "3": "Date of Birth",
            "4": "Age"
        },
        hide_index=True,
        use_container_width=True
    )   

def update():
    try:
        st.info("Update any field below. Make sure ID exists.")

        with st.form("update_form"):
            id = st.number_input("Enter the ID to update:", min_value=1, step=1)
            field = st.selectbox("Select the field to update:", ["Name", "Email", "Date of Birth", "Age"])

            new_value = None

            if field == "Name":
                new_value = st.text_input("Enter the new Name:", key="update_name")
            elif field == "Email":
                new_value = st.text_input("Enter the new Email:", key="update_email")
            elif field == "Date of Birth":
                new_value = st.date_input("Enter the new Date of Birth:", key="update_dob")
            elif field == "Age":
                new_value = st.number_input("Enter the new Age:", min_value=0, max_value=150, step=1, key="update_age")

            submit = st.form_submit_button("Update")

            if submit:
                cursor = connect.cursor()
                if field == "Name":
                    query = "UPDATE sample SET name = %s WHERE id = %s"
                elif field == "Email":
                    query = "UPDATE sample SET email = %s WHERE id = %s"
                elif field == "Date of Birth":
                    query = "UPDATE sample SET date_of_birth = %s WHERE id = %s"
                elif field == "Age":
                    query = "UPDATE sample SET age = %s WHERE id = %s"

                cursor.execute(query, (new_value, id))
                connect.commit()
                cursor.close()
                st.success(f"{field} updated successfully for ID {id}!")

    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()