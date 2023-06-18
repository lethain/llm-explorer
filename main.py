import streamlit as st
import pandas as pd


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
})

st.text_input("Your name", key="name")
name = st.session_state.name
st.write(f"This table is created by {name}:")


st.line_chart(df)
st.dataframe(df.style.highlight_max(axis=0))
