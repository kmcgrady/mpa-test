import streamlit as st

st.title("🎈 My new app!")
st.write("Welcome to your new app. Have fun editing it")
st.balloons()

"streamlit_app"

if st.button("Press to add query params"):
    st.experimental_set_query_params(foo="bar")

if st.button("Press to reset query params"):
    st.experimental_set_query_params()
