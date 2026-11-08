import streamlit as st
from supabase import create_client

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)

try:
    response = (
        supabase.table("teachers")
        .select("username")
        .limit(1)
        .execute()
    )

    print("Teachers table connection successful!")
    print("Returned records:", len(response.data))
    print("Data:", response.data)

except Exception as e:
    print("Database query failed:", repr(e))