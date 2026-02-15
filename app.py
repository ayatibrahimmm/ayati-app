import streamlit as st
import pandas as pd
import openfoodfacts

st.set_page_config(page_title="Snatched & Puffy", page_icon="🍑")

st.title("Snatched & Puffy Tracker")
st.subheader("Goal: 130 lbs | Tiny Waist & Big Glutes")

# 1. Measurement Tracker
st.header("📏 Body Progress")
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (lbs)", value=165.0)
    waist = st.number_input("Waist (inches)", value=33.0)
with col2:
    stomach = st.number_input("Stomach (inches)", value=39.0)
    glutes = st.number_input("Glutes (inches)", value=42.0)

if st.button("Save My Progress"):
    st.success(f"Saved! You are {weight - 130:.1f} lbs from your goal.")

# 2. Daily Schedule
st.header("🕒 Ramadan Daily Schedule")
schedule = {
    "05:30 AM": "Stomach Vacuums (3 sets)",
    "06:00 PM": "Iftar (Dates + Water + 5g Creatine)",
    "07:30 PM": "Heavy Glute Workout",
    "09:00 PM": "High Protein Meal + Lymphatic Drainage"
}
for time, task in schedule.items():
    st.write(f"**{time}**: {task}")
