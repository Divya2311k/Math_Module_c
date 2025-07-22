import streamlit as st
from decimal import Decimal, getcontext

# Set precision
getcontext().prec = 28

st.set_page_config(page_title="💸 High-Precision Loan Calculator", layout="centered")
st.title("💸 High-Precision Loan Calculator using `decimal`")

st.markdown("""
This calculator uses Python's `decimal` module for **high-precision financial calculations**,  
ideal for exact monetary computations without floating-point rounding errors.
---
""")

# Input section
loan_amount = st.number_input("Loan Amount (₹)", min_value=1000.0, value=100000.0, step=1000.0)
annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.1, value=7.5, step=0.1)
years = st.number_input("Loan Tenure (Years)", min_value=1, value=5, step=1)
compounds_per_year = st.selectbox("Compounding Frequency", [1, 2, 4, 12], index=3)

# Decimal conversion
P = Decimal(str(loan_amount))
r = Decimal(str(annual_rate)) / Decimal("100")
t = Decimal(str(years))
n = Decimal(str(compounds_per_year))

# Compound interest formula: A = P * (1 + r/n)^(n*t)
one = Decimal("1")
compound_rate = one + (r / n)
nt = n * t
A = P * (compound_rate ** nt)
interest_paid = A - P
monthly_payment = A / (t * 12)

# Output results
st.divider()
st.subheader("📊 Loan Summary")

st.write(f"**Total Amount Payable (A)**: ₹{A.quantize(Decimal('0.01'))}")
st.write(f"**Total Interest Paid**: ₹{interest_paid.quantize(Decimal('0.01'))}")
st.write(f"**Estimated Monthly Payment**: ₹{monthly_payment.quantize(Decimal('0.01'))}")

st.caption("Note: All calculations are performed using `decimal.Decimal` for precision.")
