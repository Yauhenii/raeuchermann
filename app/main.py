import streamlit as st
from app.parser import PDPParser
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException

url = st.text_input('Paste Check24 URL')

st.write('**URL**')
st.write(url)
try:
    title_text, attribute_dict = PDPParser.get_product_info(url)
    st.write('**Title**')
    st.write(title_text)
    st.write('**Attributes**')
    st.write(attribute_dict)
except InvalidArgumentException as e:
    print(e)
except NoSuchElementException as e:
    st.write('**Wrong URL**')
