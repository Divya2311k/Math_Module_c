import streamlit as st
import math

st.set_page_config(page_title="Advanced Math Explorer", layout="wide")
st.title("🧠 Advanced Math Explorer")
st.markdown("Explore advanced mathematical functions from Python’s `math` module.")

# --- Tabs for clarity ---
tabs = st.tabs(["Logarithmic Precision", "Trigonometric", "Inverse Trig", "Hyperbolic"])

# ---------------------------------
# 1. LOGARITHMIC & POWER FUNCTIONS
# ---------------------------------
with tabs[0]:
    st.header("📊 Logarithmic and Power Precision")
    x = st.number_input("Enter a small value (x)", value=0.001, format="%.6f")
    p = st.number_input("Enter power (for exp2)", value=3.0)

    st.write("**math.log1p(x)** → log(1 + x):", math.log1p(x))
    
    try:
        # Only available in Python 3.12+
        exp2_result = math.exp2(p)
        st.write("**math.exp2(p)** → 2^p:", exp2_result)
    except AttributeError:
        st.error("⚠️ math.exp2() is only available in Python 3.12 or later.")

# ---------------------------------
# 2. TRIGONOMETRIC FUNCTIONS
# ---------------------------------
with tabs[1]:
    st.header("📐 Basic Trigonometry")
    angle_deg = st.slider("Angle (degrees)", 0, 360, 90)
    angle_rad = math.radians(angle_deg)

    st.write(f"Converted to radians: {angle_rad:.4f}")
    st.write(f"**sin({angle_rad:.2f})**:", math.sin(angle_rad))
    st.write(f"**cos({angle_rad:.2f})**:", math.cos(angle_rad))
    st.write(f"**tan({angle_rad:.2f})**:", math.tan(angle_rad))

# ---------------------------------
# 3. INVERSE TRIGONOMETRIC FUNCTIONS
# ---------------------------------
with tabs[2]:
    st.header("🔁 Inverse Trigonometry")
    x_inv = st.slider("Enter value for arcsin/arccos (between -1 and 1)", -1.0, 1.0, 0.5)
    y_inv = st.slider("Enter value for atan2 y", -10.0, 10.0, 5.0)
    x2_inv = st.slider("Enter value for atan2 x", -10.0, 10.0, 5.0)

    st.write(f"**asin({x_inv}) →**", math.asin(x_inv))
    st.write(f"**acos({x_inv}) →**", math.acos(x_inv))
    st.write(f"**atan({x_inv}) →**", math.atan(x_inv))
    st.write(f"**atan2(y={y_inv}, x={x2_inv}) →**", math.atan2(y_inv, x2_inv))

# ---------------------------------
# 4. HYPERBOLIC FUNCTIONS
# ---------------------------------
with tabs[3]:
    st.header("🌊 Hyperbolic Trigonometry")
    hyper_x = st.number_input("Enter x value for hyperbolic functions", value=1.0)

    st.write(f"**sinh({hyper_x})**:", math.sinh(hyper_x))
    st.write(f"**cosh({hyper_x})**:", math.cosh(hyper_x))
    st.write(f"**tanh({hyper_x})**:", math.tanh(hyper_x))

    st.write("### Inverse Hyperbolic")
    st.write(f"**asinh({hyper_x})**:", math.asinh(hyper_x))
    if hyper_x >= 1:
        st.write(f"**acosh({hyper_x})**:", math.acosh(hyper_x))
    else:
        st.warning("acosh(x) only works for x ≥ 1")

    if -1 < hyper_x < 1:
        st.write(f"**atanh({hyper_x})**:", math.atanh(hyper_x))
    else:
        st.warning("atanh(x) only works for -1 < x < 1")
