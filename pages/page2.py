import streamlit as st

"Page 2"

if st.button("Press to add query params"):
    st.experimental_set_query_params(foo="bar")

if st.button("Press to reset query params"):
    st.experimental_set_query_params()
