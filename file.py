import streamlit as st

st.title("even or odd ")

a = st.text_input(label="Enter the term number (n)")

if st.button("Submit"):
        num = int(a)
        if num%2==0:
            st.write("even")
        else:
            st.write("odd")