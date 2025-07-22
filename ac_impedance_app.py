import streamlit as st
import cmath

st.set_page_config(page_title="🔌 RLC Circuit Impedance", layout="centered")
st.title("🔌 RLC Circuit Impedance Calculator (AC Analysis)")

st.markdown("""
This app calculates the **total impedance (Z)** of a **series RLC circuit** using Python's `cmath` module  
(which handles complex numbers, crucial for electrical engineering problems like AC analysis).

---
""")

# --- Inputs ---
st.header("🔧 Circuit Parameters")

R = st.number_input("Resistance R (Ohms)", min_value=0.0, value=10.0)
L = st.number_input("Inductance L (Henries)", min_value=0.0, value=0.05)
C = st.number_input("Capacitance C (Farads)", min_value=0.0000001, value=0.0001, format="%.7f")
f = st.number_input("AC Frequency f (Hz)", min_value=0.1, value=60.0)

# Angular frequency
omega = 2 * cmath.pi * f

# Calculate complex impedance Z = R + jωL - j/(ωC)
Z = complex(R) + 1j * omega * L - 1j / (omega * C)

# Output
st.divider()
st.header("📊 Results")

st.markdown(f"""
**Angular frequency (ω)**: {omega:.2f} rad/s  
**Impedance (Z)**: `{Z:.4f}` Ohms  
**|Z| (Magnitude)**: `{abs(Z):.4f}` Ohms  
**Phase Angle (θ)**: `{cmath.phase(Z):.4f}` radians
""")

# Visual phase angle (optional)
st.caption("Note: Z is a complex number = Resistance + Reactance (imaginary part).")
st.caption("Built using cmath to handle all complex operations safely.")

