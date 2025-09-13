import streamlit as st
import numpy as np
import pandas as pd
import joblib

# -----------------------------
# تنظیمات اولیه
# -----------------------------

# لیست آدرس‌ها
from utils import columns 
# بارگذاری مدل
model = joblib.load('xgb_model.joblib')

st.title('Salary Prediction')

# -----------------------------
# دریافت ورودی‌ها از کاربر
# -----------------------------
param1 = st.number_input("'Avg min between sent tnx'",value=0.0, step=0.00001,format="%.5f" )
param2 = st.number_input("Avg min between received tnx",value=0.0, step=0.00001,format="%.5f" )
param3 = st.number_input("Time Diff between first and last (Mins)",value=0.0, step=0.00001,format="%.5f" )
param4 = st.number_input("Sent tnx",value=0.0, step=0.00001,format="%.5f" )
param5 = st.number_input("Received Tnx",value=0.0, step=0.00001,format="%.5f" )
param6 = st.number_input("Number of Created Contracts",value=0.0, step=0.00001,format="%.5f" )
param7 = st.number_input("max value received ",value=0.0, step=0.00001,format="%.5f" )
param8 = st.number_input("avg val received",value=0.0, step=0.00001,format="%.5f" )
param9 = st.number_input("avg val sent",value=0.0, step=0.00001,format="%.5f" )
param10 = st.number_input("total Ether sent",value=0.0, step=0.00001,format="%.5f" )
param11 = st.number_input("total ether balance",value=0.0, step=0.00001,format="%.5f" )
param12 = st.number_input("ERC20 total Ether received",value=0.0, step=0.00001,format="%.5f" )
param13 = st.number_input("ERC20 total ether sent",value=0.0, step=0.00001,format="%.5f" )
param14 = st.number_input("ERC20 total Ether sent contract",value=0.0, step=0.00001,format="%.5f" )
param15 = st.number_input("ERC20 uniq sent addr",value=0.0, step=0.00001,format="%.5f" )
param16 = st.number_input("ERC20 uniq rec token name",value=0.0, step=0.00001,format="%.5f" )



# -----------------------------
    # ویژگی‌های عددی/باینری
row = {
    "Avg min between sent tnx": param1,
    "Avg min between received tnx": param2,
    "Time Diff between first and last (Mins)": param3,
    "Sent tnx": param4,
    "Received Tnx": param5,
    "Number of Created Contracts": param6,
    "max value received ": param7,
    "avg val received": param8,
    "avg val sent', 'total Ether sent": param9,
    "total Ether sent": param10,
    "total ether balance": param11,
    " ERC20 total Ether received'": param12,
    " ERC20 total ether sent": param13,
    " ERC20 total Ether sent contract": param14,
    " ERC20 uniq sent addr": param15,
    " ERC20 uniq rec token name": param16,


}

# دیتافریم نهایی با صفر
X = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

# مقداردهی به ویژگی‌های عددی/باینری
for col, val in row.items():
    if col in X.columns:
        X.at[0, col] = val


# -----------------------------
# تابع پیش‌بینی
# -----------------------------
def predict(x):          
    # پیش‌بینی
    prediction = model.predict(x)
    st.write("Fraud Predicted", f"{prediction[0]:,.0f} $")

# -----------------------------
# دکمه پیش‌بینی
# -----------------------------
if st.button("Predict"):
    predict(X)
