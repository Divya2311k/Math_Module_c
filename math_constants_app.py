import streamlit as st
import math

# ------------------------------
# Sidebar: Math Cheat Sheet
# ------------------------------
st.sidebar.title("📘 Math Constants Cheat Sheet")
st.sidebar.markdown("### π (`math.pi`)")
st.sidebar.markdown("- Value: `3.14159...`\n- Circle: Area = πr², Circumference = 2πr")

st.sidebar.markdown("### e (`math.e`)")
st.sidebar.markdown("- Value: `2.71828...`\n- Used in exponential growth: A = Pe^(rt)")

st.sidebar.markdown("### τ (`math.tau`)")
st.sidebar.markdown("- Value: `6.28318...`\n- Tau = 2π (1 full turn in radians)")

st.sidebar.markdown("### ∞ (`math.inf`)")
st.sidebar.markdown("- Represents infinity\n- Used for comparisons and limits")

st.sidebar.markdown("### NaN (`math.nan`)")
st.sidebar.markdown("- Not a Number\n- Used for invalid or missing data\n- Can be filtered using `math.isnan()`")

# ------------------------------
# Main App
# ------------------------------
st.title("🔢 Python `math` Constants in Real Life")

st.markdown("This mini-project demonstrates the use of:")
st.markdown("- π (`math.pi`) for circle calculations")
st.markdown("- e (`math.e`) for compound interest")
st.markdown("- τ (`math.tau`) for full rotations")
st.markdown("- ∞ (`math.inf`) for extreme value comparisons")
st.markdown("- NaN (`math.nan`) for invalid/missing data")

st.divider()

# 1. π (pi)
st.header("🔵 Circle Properties with π")
radius = st.number_input("Enter radius of a circle", min_value=0.0, value=5.0)
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
st.write(f"**Area** = {area:.2f}")
st.write(f"**Circumference** = {circumference:.2f}")

st.divider()

# 2. e
st.header("💰 Compound Interest with e")
P = st.number_input("Principal (P)", value=1000.0)
r = st.number_input("Annual interest rate (r)", value=0.05)
t = st.number_input("Time in years (t)", value=3.0)
A = P * math.e ** (r * t)
st.write(f"**Compound Amount** = ${A:.2f}")

st.divider()

# 3. τ (tau)
st.header("🔁 Full Rotations with τ (2π)")
turns = st.slider("Number of full turns", 1, 10, 2)
radians = turns * math.tau
st.write(f"{turns} full turn(s) = **{radians:.2f} radians**")

st.divider()

# 4. ∞ (inf)
st.header("📉 Find Minimum with ∞ (Infinity)")
input_numbers = st.text_input("Enter comma-separated numbers", "45, 22, 99, 4, 18")
try:
    numbers = [float(x.strip()) for x in input_numbers.split(",")]
    min_val = math.inf
    for num in numbers:
        if num < min_val:
            min_val = num
    st.write(f"**Minimum value** = {min_val}")
except:
    st.warning("Please enter valid numbers separated by commas.")

st.divider()

# 5. NaN (Not a Number)
st.header("🚫 Clean Data with NaN")
raw_data = [4.5, math.nan, 6.3, math.nan, 7.2]
st.write("Raw data:", raw_data)
cleaned_data = [x for x in raw_data if not math.isnan(x)]
st.write("Cleaned data (NaN removed):", cleaned_data)
