import streamlit as st
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException

from app.parser import PDPParser
from app.generator import CompletionTextGenerator

completion_generator = CompletionTextGenerator()
url = st.text_input('Paste Check24 URL')

st.write('**URL**')
st.write(url)
try:
    title_text, attribute_dict = PDPParser.get_product_info(url)
    st.write('**Title**')
    st.write(title_text)
    st.write('**Attributes**')
    st.write(attribute_dict)
    with st.spinner('Generating description...'):
        description = completion_generator.generate_description(title_text, attribute_dict)
        st.write('**Description**')
        st.write(description)
except InvalidArgumentException as e:
    print(e)
except NoSuchElementException as e:
    st.write('**Wrong URL**')
