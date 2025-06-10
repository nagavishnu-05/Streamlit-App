import streamlit as st

#Text Elements
st.title("Title")
st.header("Header")
st.subheader("SubHeader")
st.write("😂 Text") #Emoji Text
st.text("Another Text")
#Italic
st.write("Italic Text")
#Size
st.write("# Bigger Text")
st.write("## Big Text")
#Bulletin
st.write("- Bulletin Text")
#Code Element
st.code("""
    a = 5
    b = 3
    print(a+b) #Outupt: 8
""", language="python")
#Math Element
st.latex(r"E = mc^2")
#Indications
st.metric(label="Temprature", value="70°F", delta="1.2°F")
#Progress
st.progress(0.5, text="50%")

#Form Elements
st.text_input("Enter Name :")
st.text_input("Enter Age :")
st.date_input("Enter You DOB :")
st.checkbox("I agree")
st.radio("Gender :",["Male", "Female", "Others"])
st.selectbox("Country :", ["India", "USA", "Others"])
#Multi Selection Options
st.multiselect("Intrests :", ["Singing", "Music", "Books"])
#Slider
st.slider(label="Your English Proefficiency", min_value=0, max_value=100, value=90)
