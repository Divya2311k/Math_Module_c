import streamlit as st
from fractions import Fraction

st.set_page_config(page_title="🧮 Fraction vs Float", layout="centered")

st.title("🔢 Fraction vs Float Calculator")
st.markdown("""
This app uses Python's built-in `fractions` module to demonstrate how **exact rational arithmetic** works compared to float approximations.
""")

st.header("📥 Enter Two Fractions")

# User inputs
input1 = st.text_input("Enter first fraction (e.g. 2/3)", "2/3")
input2 = st.text_input("Enter second fraction (e.g. 3/5)", "3/5")

# Operation selection
operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

try:
    frac1 = Fraction(input1)
    frac2 = Fraction(input2)

    # Perform operation
    if operation == "Addition":
        result = frac1 + frac2
        symbol = "+"
    elif operation == "Subtraction":
        result = frac1 - frac2
        symbol = "-"
    elif operation == "Multiplication":
        result = frac1 * frac2
        symbol = "×"
    elif operation == "Division":
        result = frac1 / frac2
        symbol = "÷"

    st.divider()
    st.subheader("📊 Results")

    st.markdown(f"""
    **Operation**: {frac1} {symbol} {frac2}  
    **Fraction Result**: `{result}`  
    **Float Equivalent**: `{float(result):.10f}`  
    """)

    st.info("✅ Fractions provide **exact** results. Floats may introduce rounding errors.")

except Exception as e:
    st.error(f"⚠️ Invalid input. Please enter valid fraction strings like `1/2`, `3/4`, etc.\n\n{e}")

st.divider()
st.caption("Built with Python's `fractions` module & Streamlit.")
