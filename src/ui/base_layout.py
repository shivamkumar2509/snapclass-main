import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #5865F2 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #a0a7f2 !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@100..900&display=swap');

            /* ---------- HIDE STREAMLIT CHROME ---------- */
            /*#MainMenu,
            footer,
            header {
                visibility: hidden;
            }*/

            .block-container {
                padding-top: 1.5rem !important;
            }

            /* ---------- TYPOGRAPHY ---------- */
            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
                color: black !important;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif;
            }

            /* ---------- FORCE LIGHT FORM WIDGETS ---------- */
            .stApp {
                color-scheme: light !important;
            }

            /* ---------- INPUT FIELDS ---------- */
            .stApp div[data-baseweb="input"],
            .stApp div[data-baseweb="input"] > div,
            .stApp div[data-baseweb="base-input"],
            .stApp div[data-baseweb="base-input"] > div,
            .stApp div[data-baseweb="input"] input,
            .stApp input[type="text"],
            .stApp input[type="password"] {
                background-color: #ffffff !important;
                color: #000000 !important;
                border-radius: 1rem !important;
            }

            .stApp input::placeholder {
                color: #888888 !important;
                opacity: 1 !important;
            }

            /* Kill the dark focus tint Streamlit adds */
            .stApp div[data-baseweb="input"]:focus-within,
            .stApp div[data-baseweb="base-input"]:focus-within {
                background-color: #ffffff !important;
                border: 2px solid #5865F2 !important;
                border-radius: 1rem !important;
                box-shadow: none !important;
            }

            /* Icon inside input (e.g. password eye) */
            .stApp div[data-baseweb="input"] svg,
            .stApp div[data-baseweb="base-input"] svg {
                fill: #000000 !important;
                color: #000000 !important;
            }

            /* ---------- FOOTER ---------- */
            .footer-text,
            .footer-text p {
                color: #000000 !important;
                font-weight: bold !important;
            }

            /* ---------- BUTTONS ---------- */
            button {
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: #fff !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button:hover {
                transform: scale(1.05);
            }
        </style>
    """, unsafe_allow_html=True)