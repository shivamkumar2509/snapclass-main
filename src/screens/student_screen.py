import streamlit as st
import numpy as np
from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image

def student_screen():
    style_background_dashboard()
    style_base_layout()
    
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    # st.markdown(
    #             "<h2 style='text-align:center; color:#1a1a1a; margin-bottom: 1.5rem;'>Login using password</h2>",
    #             unsafe_allow_html=True
    #         )

    st.header('Login using FACEID',text_alignment='center')
    st.space()
    st.space()

    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        np.array(Image.open(photo_source))
    footer_dashboard()