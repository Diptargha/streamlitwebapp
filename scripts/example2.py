import streamlit as st

st.title("Welcome to Streamlit")

check_one = st.checkbox("Yes")
check_two = st.checkbox("No")

if check_one:
    value = "Yes"
elif check_two:
    value = "No"
else:
    value="No value selected"

st.write(f"You selected: {value}")