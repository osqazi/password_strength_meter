import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", layout="centered", page_icon="🔒")

uCase = "[A-Z]"
lCase = "[a-z]"
num = "[0-9]"
special = "[@_!#$%^&*()<>?/\|}{~:]"
           
def check(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long to be Strong."
    elif not re.search(uCase, password):
        return ("Weak Password. Use at least one uppercase letter to be strong.")
    elif not re.search(lCase, password):
        return ("Weak Password!. Use at least one lowercase letter to be strong.")
    elif not re.search(num, password) :
        return ("Weak Password! Use at least one number to be strong.")
    elif not re.search(special, password) :
        return ("Moderate Password! Use at least one special character to be strong.")
    st.balloons()
    return "Your Password is Perfectly Strong!."

st.markdown(

"""
<style>
.stApp {
    background-color: #f1ffb2;
}
</style>

""",
unsafe_allow_html=True
)


st.title("Password Strength Meter / Checker")
st.header("Project 2 - Created by Owais Qazi")
st.write("Enter your password to check its Strength.")
st.write("It will also helps you to to create a strong password.")
password = st.text_input("Enter your desired Password: ", type="password")
if st.button("Check Strength"):
    st.header(check(password))
    





        
    