import streamlit as st
import cmath

st.set_page_config(page_title="📐 cmath Module Explorer", layout="centered")
st.title("📘 Complex Math (`cmath`) Module Explorer")

st.markdown("""
The `cmath` module supports **complex number mathematics** in Python.  
Unlike the `math` module (which only works for real numbers), `cmath` can handle expressions like √(-1), log(-1), etc.

---

""")

st.sidebar.title("🔢 `cmath` Constants")

st.sidebar.markdown("### `cmath.pi`")
st.sidebar.write(cmath.pi)

st.sidebar.markdown("### `cmath.e`")
st.sidebar.write(cmath.e)

st.sidebar.markdown("### `cmath.inf`")
st.sidebar.write(cmath.inf)

st.sidebar.markdown("### `cmath.nan`")
st.sidebar.write(cmath.nan)

# Input area
st.header("✍️ Try a Complex Number")

user_input = st.text_input("Enter a number (e.g., `2+3j`, `-1`, `1j`)", "2+3j")

try:
    z = complex(user_input)

    st.success(f"Input as complex number: {z}")

    st.divider()
    st.subheader("🧮 Functions on Complex Numbers")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ Trigonometric")
        st.write("sin(z):", cmath.sin(z))
        st.write("cos(z):", cmath.cos(z))
        st.write("tan(z):", cmath.tan(z))

        st.markdown("### ✅ Inverse Trigonometric")
        st.write("asin(z):", cmath.asin(z))
        st.write("acos(z):", cmath.acos(z))
        st.write("atan(z):", cmath.atan(z))

        st.markdown("### ✅ Hyperbolic")
        st.write("sinh(z):", cmath.sinh(z))
        st.write("cosh(z):", cmath.cosh(z))
        st.write("tanh(z):", cmath.tanh(z))

    with col2:
        st.markdown("### 📈 Exponent & Logarithm")
        st.write("exp(z):", cmath.exp(z))
        st.write("log(z):", cmath.log(z))
        st.write("log10(z):", cmath.log10(z))
        st.write("sqrt(z):", cmath.sqrt(z))

        st.markdown("### 🧮 Polar / Rectangular")
        st.write("phase(z):", cmath.phase(z))
        st.write("polar(z):", cmath.polar(z))
        st.write("rect(r, φ):", cmath.rect(abs(z), cmath.phase(z)))

        st.markdown("### 📌 Other")
        st.write("conjugate():", z.conjugate())
        st.write("isnan():", cmath.isnan(z))
        st.write("isinf():", cmath.isinf(z))

except Exception as e:
    st.error(f"⚠️ Invalid complex number input. Try things like `3+4j`, `-1`, or `1j`.\n\n{e}")

st.divider()

st.markdown("""
## 🔍 `math` vs `cmath`

| Feature         | `math`         | `cmath`            |
|-----------------|----------------|--------------------|
| Works with real numbers | ✅ Yes        | ✅ Yes              |
| Works with complex numbers | ❌ No         | ✅ Yes              |
| Returns complex output | ❌ No         | ✅ Yes              |
| Use case | Everyday math | Electrical, physics, engineering |

---

Built with 💡 Python & Streamlit.
""")
