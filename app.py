import streamlit as st
import datetime

# --- 1. CONFIG & THEME ---
st.set_page_config(page_title="Ayati", page_icon="🎀", layout="wide")

# ADVANCED CSS FOR MOBILE APP VIBE
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce7f3 100%); }
    .action-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 192, 203, 0.5);
        box-shadow: 0 8px 32px 0 rgba(236, 72, 153, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        background: linear-gradient(90deg, #f472b6, #db2777);
        color: white;
        border: none;
        padding: 12px;
        font-weight: 600;
    }
    [data-testid="stSidebar"] { background-color: rgba(255, 255, 255, 0.5); }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE PASSWORD LOCK ---
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center; color: #db2777;'>✨ Ayati Private Access</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Please enter your secret key to unlock your dashboard.</p>", unsafe_allow_html=True)
        
        # Center the login box
        col_a, col_b, col_c = st.columns([1,2,1])
        with col_b:
            pwd = st.text_input("Secret Key", type="password")
            if st.button("Unlock Dashboard"):
                if pwd == "Ayatzeyadib123": # You can change this to your own password!
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("❌ Access Denied")
        return False
    return True

if not check_password():
    st.stop()

# --- 3. THE DASHBOARD (Only shows if password is correct) ---
st.markdown("<h1 style='text-align: center; color: #be185d; margin-bottom: 0;'>🌸 AYATI 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #db2777; font-style: italic;'>Your journey to 130 lbs starts now.</p>", unsafe_allow_html=True)

# STATS CARDS
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="action-card"><h3>📏 Waist</h3><h2>33"</h2><p>Goal: 29"</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="action-card"><h3>🍑 Glutes</h3><h2>42"</h2><p>Puffy & Rounded</p></div>', unsafe_allow_html=True)
with col3:
    curr_w = st.sidebar.number_input("Current Weight", value=165.0)
    st.sidebar.progress(max(0.0, min(1.0, (165-curr_w)/(165-130))))
    st.markdown(f'<div class="action-card"><h3>⚖️ Weight</h3><h2>{curr_w} lbs</h2><p>{165-curr_w} lbs lost</p></div>', unsafe_allow_html=True)

# APP NAVIGATION
with st.expander("🕒 VIEW DAILY ROUTINE", expanded=True):
    st.info("**Morning:** 05:30 - Stomach Vacuums")
    st.info("**Evening:** 19:30 - Glute Growth (Heavy)")

with st.expander("📚 ACADEMICS & WORK"):
    exam = st.text_input("Assignment/Exam Name")
    date = st.date_input("Deadline")
    if st.button("Add to Calendar"):
        st.success(f"Saved: {exam} for {date}")

with st.expander("🕌 PRAYER & SPIRIT"):
    st.checkbox("Fajr")
    st.checkbox("Dhuhr")
    st.checkbox("Asr")
    st.checkbox("Maghrib (Iftar)")
    st.checkbox("Isha")

with st.expander("📸 UPDATE BODY STATS"):
    st.number_input("New Waist Measurement", value=33.0)
    st.number_input("New Glute Measurement", value=42.0)
    st.button("Save New Stats")
