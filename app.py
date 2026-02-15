import streamlit as st
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import openfoodfacts

# --- THEME & CONFIG ---
st.set_page_config(page_title="Ayati", page_icon="🎀", layout="wide")
st.markdown("<style>.stApp { background: linear-gradient(135deg, #4d0221 0%, #831843 100%); } .action-card { background: rgba(45,0,18,0.8); border-radius: 20px; padding: 20px; border: 2px solid #db2777; margin-bottom: 15px; }</style>", unsafe_allow_html=True)

# 1. SECURITY
if "password_correct" not in st.session_state:
    pwd = st.text_input("Ayati Secret Key", type="password")
    if st.button("Unlock"):
        if pwd == "Ayati2026": st.session_state["password_correct"] = True; st.rerun()
    st.stop()

# 2. DAILY PROTEIN TRACKER LOGIC
if "daily_protein" not in st.session_state:
    st.session_state.daily_protein = 0.0

st.title("🌸 AYATI: Snap & Track")

# PROGRESS BAR TO 140G
st.header(f"Total Protein Today: {st.session_state.daily_protein:.1f}g / 140g")
st.progress(min(1.0, st.session_state.daily_protein / 140.0))

# 3. BARCODE SCANNER SECTION
with st.expander("📸 SCAN BARCODE OR TAKE PHOTO", expanded=True):
    img_file = st.camera_input("Snap a Barcode")
    
    if img_file:
        # Process the image to find barcode
        file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
        opencv_img = cv2.imdecode(file_bytes, 1)
        barcodes = decode(opencv_img)
        
        if barcodes:
            code = barcodes[0].data.decode('utf-8')
            st.success(f"Barcode Detected: {code}")
            
            # Lookup on OpenFoodFacts
            api = openfoodfacts.API(user_agent="AyatiApp/1.0")
            product = api.product.get(code, fields=["product_name", "nutriments"])
            
            if product:
                name = product.get('product_name', 'Unknown Item')
                prot = product.get('nutriments', {}).get('proteins_100g', 0)
                st.subheader(f"Found: {name}")
                st.write(f"Protein: {prot}g per 100g")
                
                # Button to Add to Daily Total
                if st.button(f"Add {name} to Daily Log"):
                    st.session_state.daily_protein += float(prot)
                    st.success(f"Added! New total: {st.session_state.daily_protein}g")
            else:
                st.error("Product not found in database.")
        else:
            st.warning("No barcode detected. Try getting closer or improving light!")

# 4. MANUAL LOGGING (For things without barcodes like Chicken)
with st.expander("✍️ MANUAL LOG (For Whole Foods)"):
    manual_name = st.text_input("Food/Drink Name")
    manual_prot = st.number_input("Protein Grams", min_value=0.0)
    if st.button("Add Manual Entry"):
        st.session_state.daily_protein += manual_prot
        st.balloons()

if st.button("Reset Daily Progress"):
    st.session_state.daily_protein = 0.0
    st.rerun()
