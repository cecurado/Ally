import streamlit as st

st.title("Here is my AI 'Agent' LOL  ")
st.write("I knew you could read my codes and understand my broken english before 2026 😌 ")

st.markdown("""
###  I hope you are having an amazing day/night  
""")
import time

for i in range(5):
    st.write("Sending virtual hugs" + " 🤗" * (i+1))
    time.sleep(0.5)

if st.button("Click me!"):
    st.write(" I hope this makes you smile today! 😊")
    st.balloons()
