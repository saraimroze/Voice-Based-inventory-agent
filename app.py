import streamlit as st
import pandas as pd
import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Smart Inventory Dashboard",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.big-title {
    font-size:40px;
    font-weight:bold;
    text-align:center;
    color:#4CAF50;
}
.card {
    padding:15px;
    border-radius:10px;
    background:#f3f3f3;
    box-shadow:0px 0px 10px rgba(0,0,0,0.1);
}
.mic-btn {
    background:#ff4b4b;
    padding:15px;
    border-radius:50%;
    text-align:center;
    font-size:30px;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown('<p class="big-title">🎯 Smart Inventory Dashboard</p>', unsafe_allow_html=True)

# -----------------------------
# SAMPLE INVENTORY DATA
# -----------------------------
data = {
    "Item": ["Keyboard", "Mouse", "Monitor", "CPU", "Headphones"],
    "Stock": [50, 30, 20, 15, 40],
    "Price": [800, 400, 9000, 25000, 1200]
}
df = pd.DataFrame(data)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("➕ Add Item")
item = st.sidebar.text_input("Item name")
stock = st.sidebar.number_input("Stock", 0)
price = st.sidebar.number_input("Price", 0)

if st.sidebar.button("Add"):
    new_row = pd.DataFrame([[item, stock, price]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    st.success("Item Added")

# -----------------------------
# INVENTORY TABLE
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Inventory Table")
    st.dataframe(df, use_container_width=True)

# -----------------------------
# VISUALIZATION
# -----------------------------
with col2:
    st.subheader("📊 Stock Visualization")
    st.bar_chart(df.set_index("Item")["Stock"])

# -----------------------------
# MIC BUTTON UI
# -----------------------------
st.subheader("🎤 Voice Command")
if st.button("🎤 Tap to Speak"):
    st.success("Voice command captured (demo mode)")
    st.write("Example: Add 10 keyboards")

# -----------------------------
# ACTIVITY LOG
# -----------------------------
st.subheader("📝 Activity Log")

if "log" not in st.session_state:
    st.session_state.log = []

if st.button("Simulate Activity"):
    st.session_state.log.append(
        f"Stock updated at {datetime.datetime.now().strftime('%H:%M:%S')}"
    )

for activity in st.session_state.log[::-1]:
    st.info(activity)

# -----------------------------
# METRICS
# -----------------------------
st.subheader("📈 Dashboard Metrics")
c1, c2, c3 = st.columns(3)

c1.metric("Total Items", len(df))
c2.metric("Total Stock", df["Stock"].sum())
c3.metric("Total Value", df["Stock"].mul(df["Price"]).sum())