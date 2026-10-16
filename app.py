

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Employee Attrition Analysis", page_icon="📊", layout="wide"
)

st.title("📊 Employee Attrition Analysis Dashboard")
st.write(
    "Unified Mentor Internship Project - Palo Alto Attrition Analysis Dashboard"
)


# Data load karne ka function
@st.cache_data
def load_data():
  try:
    # Pehle cleaned file check karte hain
    df = pd.read_csv("Employee_Attrition_Cleaned.csv")
  except:
    try:
      df = pd.read_csv("Palo Alto Networks unified.csv")
    except:
      # Agar extension missing ho toh excel try karte hain
      df = pd.read_excel("Employee_Attrition_Cleaned")
  return df


try:
  df = load_data()

  # Sidebar filters
  st.sidebar.header("Filter Options")
  if "Department" in df.columns:
    dept = st.sidebar.selectbox(
        "Select Department", ["All"] + list(df["Department"].unique())
    )
    if dept != "All":
      df = df[df["Department"] == dept]

  # Key Metrics
  total_emp = len(df)
  st.metric("Total Employees", total_emp)

  if "Attrition" in df.columns:
    attrition_count = (df["Attrition"] == "Yes").sum()
    attrition_rate = (attrition_count / total_emp) * 100 if total_emp > 0 else 0
    st.metric("Attrition Count", attrition_count)
    st.metric("Attrition Rate (%)", f"{attrition_rate:.2f}%")

  st.subheader("Dataset Preview")
  st.dataframe(df.head(10))

except Exception as e:
  st.error(
      f"File read karne mein error aayi hai. Kripya check karein ki CSV file"
      f" folder mein hai. Error: {e}"
  )