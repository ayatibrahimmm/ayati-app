import streamlit as st
import datetime

# --- 1. CONFIG & THEME ---
st.set_page_config(page_title="Ayati", page_icon="🎀", layout="wide")

# ADVANCED CSS FOR READABILITY & CONTRAST
st.markdown("""
    <style>
    /* Background Gradient */
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce7f3 100%); }
    
    /* Global Text Settings */
    html, body, [class*="css"]  {
        color: #500724 !important; /* Dark Berry for high contrast */
        font-size: 110% !important; /* Larger general text */
    }

    /* Action Cards with White Glow */
    .action-card {
        background: rgba(255, 255, 255, 0.9); /* More solid white background */
        border-radius: 20px;
        padding: 25px;
        border: 2px solid #f9a8d4;
        box-shadow: 0 8px 32px 0 rgba(219, 39, 119, 0.15);
        text-align: center;
        margin-bottom: 20px;
    }

    /* Make Headers Bold and Dark */
    h1, h2, h3, h4 {
        color: #831843 !important; 
        font-weight: 800 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Navigation Labels */
    .st-expanderHeader {
        font-size: 1.3rem !important;
        font-weight: bold !important;
        color: #be185d !important;
        background-color: white !important;
        border-radius: 10px;
    }

    /* Sidebar Contrast */
    [data-testid="stSidebar"] { 
        background-color: #fdf2f8 !important; 
        border-right: 3px solid #f9a8d4;
    }
    
    /* Input Labels */
    label {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #500724 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE PASSWORD LOCK ---
def check_password():
    if "password_correct" not in st.session_state:
        st.markdown("<h1 style='text-align: center;'>✨ Ayati Private Access</h1>", unsafe_allow_html=True)
        col_a, col_b, col_c = st.columns([1,2,1])
        with col_b:
            pwd = st.text_input("Secret Key", type="password")
            if st.button("Unlock Dashboard"):
                if pwd == "Ayati2026":
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("❌ Access Denied")
        return False
    return True

if not check_password():
    st.stop()

# --- 3. THE DASHBOARD ---
st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>🌸 AYATI 🌸</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; font-weight: 600;'>The Road to 130 lbs: Tiny Waist & Big Glutes</p>", unsafe_allow_html=True)

# STATS CARDS
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="action-card"><h3>📏 Waist</h3><h2 style="color:#db2777;">33"</h2><p>Goal: 29"</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="action-card"><h3>🍑 Glutes</h3><h2 style="color:#db2777;">42"</h2><p>Puffy & Rounded</p></div>', unsafe_allow_html=True)
with col3:
    curr_w = st.sidebar.number_input("Weight (lbs)", value=165.0)
    st.sidebar.progress(max(0.0, min(1.0, (165-curr_w)/(165-130))))
    st.markdown(f'<div class="action-card"><h3>⚖️ Weight</h3><h2 style="color:#db2777;">{curr_w} lbs</h2><p>{165-curr_w} lbs lost</p></div>', unsafe_allow_html=True)

# APP NAVIGATION
st.write("---")
with st.expander("🕒 MY DAILY ROUTINE", expanded=True):
    st.subheader("Morning Actions")
    st.write("✅ **05:30 AM:** Stomach Vacuums (3 sets)")
    st.subheader("Evening Actions")
    st.write("✅ **06:05 PM:** Iftar + 5g Creatine")
    st.write("✅ **07:30 PM:** Heavy Glute Growth Lifting")

with st.expander("📚 ACADEMICS & WORK"):
    exam = st.text_input("What's the Exam or Homework?")
    date = st.date_input("Deadline Date")
    if st.button("Add to My Planner"):
        st.success(f"Tracked: {exam} for {date}")

with st.expander("🕌 SPIRITUAL GOALS"):
    st.checkbox("Fajr Prayer")
    st.checkbox("Dhuhr Prayer")
    st.checkbox("Asr Prayer")
    st.checkbox("Maghrib Prayer (Iftar)")
    st.checkbox("Isha Prayer")

with st.expander("📸 LOG MEASUREMENTS"):
    st.number_input("Update Waist (inches)", value=33.0)
    st.number_input("Update Glutes (inches)", value=42.0)
    st.button("Save New Measurements")
