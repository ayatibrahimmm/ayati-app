import streamlit as st
import datetime

# --- 1. CONFIG & THEME ---
st.set_page_config(page_title="Ayati", page_icon="🎀", layout="wide")

# HIGH CONTRAST DARK MODE CSS
st.markdown("""
    <style>
    /* Background: Deep Pink Gradient */
    .stApp { background: linear-gradient(135deg, #4d0221 0%, #831843 100%); }
    
    /* Text Color: Light Pink/White for High Visibility */
    html, body, [class*="css"], label, p {
        color: #fce7f3 !important; 
        font-size: 115% !important;
        font-weight: 600;
    }

    /* Action Cards: Deep Berry Glass (No White!) */
    .action-card {
        background: rgba(45, 0, 18, 0.8) !important; /* Deep Dark Berry */
        border-radius: 20px;
        padding: 25px;
        border: 2px solid #db2777; /* Bright Pink Border */
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        text-align: center;
        margin-bottom: 20px;
    }

    /* Headers: Bright Neon Pink */
    h1, h2, h3, h4 {
        color: #f472b6 !important; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* Navigation Sections */
    .st-expanderHeader {
        background-color: #500724 !important;
        color: #fbcfe8 !important;
        border: 1px solid #db2777 !important;
        font-size: 1.3rem !important;
    }

    /* Sidebar: Dark Background */
    [data-testid="stSidebar"] { 
        background-color: #2d0012 !important; 
        border-right: 2px solid #f472b6;
    }
    
    /* Buttons: Neon Glow */
    .stButton>button {
        background: linear-gradient(90deg, #db2777, #be185d) !important;
        color: white !important;
        border: 1px solid #f9a8d4 !important;
        font-weight: bold;
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
st.markdown("<h1 style='text-align: center;'>🌸 AYATI 🌸</h1>", unsafe_allow_html=True)

# STATS CARDS (High Visibility Dark Background)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="action-card"><h3>📏 Waist</h3><h2 style="color:#f472b6;">33"</h2><p>Goal: 29"</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="action-card"><h3>🍑 Glutes</h3><h2 style="color:#f472b6;">42"</h2><p>Puffy & Rounded</p></div>', unsafe_allow_html=True)
with col3:
    curr_w = st.sidebar.number_input("Weight (lbs)", value=165.0)
    st.sidebar.progress(max(0.0, min(1.0, (165-curr_w)/(165-130))))
    st.markdown(f'<div class="action-card"><h3>⚖️ Weight</h3><h2 style="color:#f472b6;">{curr_w} lbs</h2><p>{165-curr_w} lbs lost</p></div>', unsafe_allow_html=True)

# NAVIGATION
st.write("---")
with st.expander("🕒 MY DAILY ROUTINE", expanded=True):
    st.write("✅ **05:30 AM:** Stomach Vacuums")
    st.write("✅ **06:05 PM:** Iftar + Creatine")
    st.write("✅ **07:30 PM:** Heavy Glute Growth")

with st.expander("📚 ACADEMICS & WORK"):
    exam = st.text_input("Exam or Homework?")
    date = st.date_input("Deadline")
    if st.button("Add to Planner"):
        st.success(f"Tracked: {exam}")

with st.expander("🕌 SPIRITUAL GOALS"):
    st.checkbox("Prayed all 5 today")

with st.expander("📸 LOG MEASUREMENTS"):
    st.number_input("New Waist", value=33.0)
    st.number_input("New Glutes", value=42.0)
    st.button("Save Stats")
