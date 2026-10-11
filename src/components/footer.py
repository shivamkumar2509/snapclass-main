import streamlit as st

def footer_home():

    logo_url = "https://t3.ftcdn.net/jpg/05/42/08/50/360_F_542085013_Kq945kXcb9lpjFeZM1cRPJndE97FpBZs.webp"
    st.markdown(f"""
                    <div style="margin-top: 2rem; display: flex; gap: 6px; justify-content: center; align-items: center;">
                        <p style="font-weight: bold; color: white;">Create with ❤️ by </p>
                        <img src="{logo_url}" style="max-height:25px" />
                    </div>
                """,unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://t3.ftcdn.net/jpg/05/42/08/50/360_F_542085013_Kq945kXcb9lpjFeZM1cRPJndE97FpBZs.webp"
    st.markdown(f"""
        <div style="margin-top: 2rem; display: flex; gap: 6px; justify-content: center; align-items: center;">
            <p class="footer-text">Create with ❤️ by </p>
            <img src="{logo_url}" style="max-height:25px" />
        </div>
    """, unsafe_allow_html=True)