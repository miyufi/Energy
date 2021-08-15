import streamlit as st
from streamlit import caching
from streamlit.script_runner import StopException, RerunException
from PIL import Image 
import time

st.set_page_config(page_title='Axie Energy Calculator', page_icon='👾', layout='centered')

st.image('./images/axie-header.png')

st.markdown("<h1 style='text-align: center'>Axie Energy Calculator 👾</h1>", unsafe_allow_html=True)

energy = str(st.number_input('Energy', value = 3))    

st.markdown("# Energy Count: " + energy)
st.text("\n")
st.text("\n")
st.text("\n")

st.image('./images/axie-class.png', width = None)
st.write("Refresh page or put 3 in the energy manually to reset")
st.write("Source code: [Github](https://github.com/miyufi/Energy)")