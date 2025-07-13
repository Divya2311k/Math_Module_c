import streamlit as st
import math

st.set_page_config(page_title="Math Toolkit", layout="wide")
st.title("🧮 Math Toolkit — Explore Python's `math` Module")

st.markdown("This interactive app lets you explore **all numeric functions** from Python's `math` module grouped by category.")

# Grouped Tabs for Clarity
tabs = st.tabs(["Basic Math", "Exponents & Logs", "Rounding & Floats", "Trigonometry", "Combinatorics"])

# ----------------- TAB 1: BASIC MATH -----------------
with tabs[0]:
    st.header("📌 Basic Arithmetic & Power")
    x = st.number_input("Enter a number (x)", value=5.5)
    y = st.number_input("Enter another number (y)", value=3.0)

    st.write("**Ceil:**", math.ceil(x))
    st.write("**Floor:**", math.floor(x))
    st.write("**Trunc:**", math.trunc(x))
    st.write("**Fabs (absolute):**", math.fabs(x))
    st.write("**Fmod (x % y):**", math.fmod(x, y))
    st.write("**Remainder:**", math.remainder(x, y))
    st.write("**Modf:** Fractional and Integer Parts:", math.modf(x))
    st.write("**Copysign (x sign of y):**", math.copysign(x, y))
    st.write("**Pow (x^y):**", math.pow(x, y))
    st.write("**Sqrt:**", math.sqrt(x))
    st.write("**Isqrt (int sqrt):**", math.isqrt(int(x)))
    st.write("**Product of list [x, y]:**", math.prod([x, y]))
    st.write("**Sum of list [x, y]:**", math.fsum([x, y]))

# ----------------- TAB 2: EXPONENTIAL & LOGS -----------------
with tabs[1]:
    st.header("📈 Logarithmic & Exponential Functions")
    a = st.number_input("Enter base number (a)", value=math.e)
    b = st.number_input("Enter exponent (b)", value=2.0)

    st.write("**exp(b)** = e^b:", math.exp(b))
    st.write("**expm1(b)** = e^b - 1:", math.expm1(b))
    st.write("**log(a):**", math.log(a))
    st.write("**log10(a):**", math.log10(a))
    st.write("**log2(a):**", math.log2(a))
    mantissa, exponent = math.frexp(a)
    st.write("**frexp(a):**", f"Mantissa = {mantissa}, Exponent = {exponent}")
    st.write("**ldexp(mantissa, exponent):**", math.ldexp(mantissa, exponent))

# ----------------- TAB 3: ROUNDING & FLOAT BEHAVIOR -----------------
with tabs[2]:
    st.header("🧮 Rounding, Comparison, and Float Checks")

    a2 = st.number_input("Number A", value=1.00000001)
    b2 = st.number_input("Number B", value=1.00000002)

    st.write("**isfinite(A):**", math.isfinite(a2))
    st.write("**isinf(A):**", math.isinf(a2))
    st.write("**isnan(A):**", math.isnan(a2))
    st.write("**isclose(A, B):**", math.isclose(a2, b2, rel_tol=1e-9))
    st.write("**dist([x1, y1], [x2, y2]):**", math.dist([a2, 0], [b2, 0]))
    st.write("**hypot(x, y):**", math.hypot(a2, b2))

# ----------------- TAB 4: TRIGONOMETRY -----------------
with tabs[3]:
    st.header("📐 Angle Conversion")
    angle_deg = st.slider("Angle in degrees", min_value=0, max_value=360, value=180)
    angle_rad = math.radians(angle_deg)

    st.write("**Radians:**", angle_rad)
    st.write("**Back to Degrees:**", math.degrees(angle_rad))

# ----------------- TAB 5: COMBINATORICS -----------------
with tabs[4]:
    st.header("🎲 Combinatorics and Special Functions")
    n = st.number_input("n (non-negative integer)", min_value=0, step=1, value=5)
    k = st.number_input("k (0 ≤ k ≤ n)", min_value=0, max_value=n, step=1, value=3)

    st.write("**Factorial(n):**", math.factorial(n))
    st.write("**Gamma(n):**", math.gamma(n))
    st.write("**Log Gamma (lgamma):**", math.lgamma(n))
    st.write("**Combinations (n choose k):**", math.comb(n, k))
    st.write("**Permutations (n P k):**", math.perm(n, k))
