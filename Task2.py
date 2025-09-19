# Task2.py - Streamlit single-page Hacktoberfest event app (with Organizer View)
import streamlit as st
import pandas as pd
from datetime import datetime
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Hacktoberfest @ GDG Galgotias", layout="wide", initial_sidebar_state="collapsed")
st.markdown(
    """
    <style>
    /* Make text adapt automatically to Streamlit theme */
    p, label, span, div, h1, h2, h3, h4, h5, h6 {
        color: var(--text-color) !important;
    }

    /* Define theme-aware variables */
    :root {
        --text-color: black;
    }
    [data-theme="dark"] {
        --text-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -------------------------
# Theme state (persistent)
# -------------------------
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

# Top bar: Title (left) + small theme toggle button (right)

col_left, col_right = st.columns([9, 1])
with col_left:
    st.markdown(
        f"""
        <h1 style="margin:0; font-family: 'Segoe UI', sans-serif;
                   background: linear-gradient(90deg,#4285F4,#34A853,#FBBC05,#EA4335);
                   -webkit-background-clip: text; color: transparent; font-size:2.4rem;">
            <img src="https://raw.githubusercontent.com/Dhruvdot7/GDGoC-GU-Task2/main/gdglogo.png" 
                 width="60" style="vertical-align:middle; margin-right:8px;">
            Hacktoberfest @ GDG Galgotias
        </h1>
        <p style="margin:4px 0 14px 0; color: #6b7280;">
            Open-source contribution sprint • Learn Git • Make your first PR
        </p>
        <p style="margin:2px 0; color:#1f2937; font-weight:600;">
            📅 Event Date: 1st October 2025
        </p>
        <p style="margin:2px 0; color:#1f2937; font-weight:600;">
            🏆 Reward Ceremony: 5th October 2025
        </p>
        """,
        unsafe_allow_html=True
    )

with col_right:
    btn_label = "🌙" if not st.session_state["dark_mode"] else "🌞"
    if st.button(btn_label, key="theme_btn"):
        st.session_state["dark_mode"] = not st.session_state["dark_mode"]

# -------------------------
# Apply global theme CSS
# -------------------------
if st.session_state["dark_mode"]:
    page_bg = "#0f1720"
    text_color = "#e6eef8"
else:
    page_bg = "#f8fafc"
    text_color = "#111827"

st.markdown(
    f"""
    <style>
      .stApp {{
        background: {page_bg};
        color: {text_color};
      }}
      h1, h2, h3 {{ margin-top: 0.25rem; margin-bottom: 0.25rem; }}
      .muted {{ color: rgba(0,0,0,0.6); }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Countdown
# -------------------------
event_date = datetime(2025, 10, 1, 10, 0, 0)  
now = datetime.now()
remaining = event_date - now
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60

st.markdown(
    f"""
    <div style="display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
      <div style="background:rgba(255,255,255,0.04); padding:18px 26px; border-radius:12px;
                  box-shadow: 0 8px 20px rgba(0,0,0,0.08); text-align:center;">
        <div style="font-size:18px; color:{text_color};">⏳ Event starts in</div>
        <div style="font-weight:700; font-size:20px; margin-top:6px; color:{text_color};">
          {days} days • {hours} hrs • {minutes} mins
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Floating animated highlights
# -------------------------
card_bg = "#16181b" if st.session_state["dark_mode"] else "#ffffff"
card_text = "#e6eef8" if st.session_state["dark_mode"] else "#0b1220"
desc_color = "rgba(230,238,248,0.85)" if st.session_state["dark_mode"] else "rgba(11,18,32,0.72)"
glow = (
    "0 0 12px rgba(66,133,244,0.10),"
    "0 0 20px rgba(52,168,83,0.06),"
    "0 0 28px rgba(251,188,5,0.04),"
    "0 0 36px rgba(234,67,53,0.03)"
)

st.markdown(
    f"""
    <style>
      .cards-wrapper {{
        display:flex;
        gap:18px;
        justify-content:center;
        flex-wrap:nowrap;
        overflow-x:auto;
        padding: 6px 4px 18px 4px;
      }}
      .card {{
        background: {card_bg};
        color: {card_text};
        width: 320px;
        min-width: 260px;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 10px 24px rgba(2,6,23,0.08);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        text-align: center;
      }}
      .card:hover {{
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 18px 40px rgba(2,6,23,0.18), {glow};
      }}
      .icon {{ font-size:56px; margin-bottom:10px; }}
      .card-title {{ font-weight:700; font-size:18px; margin-bottom:8px; }}
      .card-desc {{ font-size:14px; color: {desc_color}; }}
    </style>

    <div class="cards-wrapper">
      <div class="card">
        <div class="icon">🌍</div>
        <div class="card-title">Open Source 101</div>
        <div class="card-desc">Hands-on intro to Git & GitHub basics.</div>
      </div>

      <div class="card">
        <div class="icon">🤝</div>
        <div class="card-title">Contribution Sprint</div>
        <div class="card-desc">Work with mentors & peers to make your first PR.</div>
      </div>

      <div class="card">
        <div class="icon">🏆</div>
        <div class="card-title">Community & Networking</div>
        <div class="card-desc">Meet contributors, showcase work & collect swag.</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(f"<div style='text-align:center; margin-top:10px;'><b style='color:{card_text}'>✨ GDGOC Organizer: Vanshika Prakash</b></div>", unsafe_allow_html=True)
st.write("---")

# -------------------------
# Registration Form
# -------------------------
st.subheader("📝 Register for Hacktoberfest (GDG Galgotias)")
# Google Sheets Setup
# Define scope
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Load creds_dict from st.secrets (best for deployment)
creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)

# Authorize client
client = gspread.authorize(creds)
# Open Google Sheet
sheet = client.open("Hacktoberfest Registrations").sheet1

with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    college = st.text_input("College / Organization")
    interest = st.selectbox("Interest Area", ["Open Source", "Docs & Community", "Frontend", "Backend", "DevOps", "Other"])
    submitted = st.form_submit_button("Register")
    
    if submitted:
        if not (name and email and college):
            st.error("Please fill in Name, Email and College/Organization.")
        else:
            try:
                # Store directly in Google Sheet
                sheet.append_row([name, email, college, interest, datetime.now().isoformat()])
                
                st.success(f"🎉 Thanks {name}! Registration saved.")
                st.info(f"📧 Confirmation email simulated to {email}")
            except Exception as e:
                st.error(f"⚠️ Could not save registration: {e}")

# -------------------------
# Event Schedule
# -------------------------

st.subheader("📅 Event Schedule (Same for every round)")
st.markdown( 
    """ 
    <style>
    .timeline {
      position: relative;
      margin: 20px 0;
      padding: 0 0 0 25px;
      border-left: 3px solid #4285F4;
    } 
    .timeline-entry {
      margin-bottom: 20px;
      position: relative;
    } 
    .timeline-entry:before { 
      content: ""; 
      position: absolute; 
      left: -11px; 
      top: 5px; 
      width: 16px; 
      height: 16px; 
      background: #4285F4; 
      border-radius: 50%; 
      box-shadow: 0 0 0 3px rgba(66,133,244,0.25); 
    } 
    .timeline-time {
      font-weight: bold;
      margin-bottom: 4px; 
    } 
    .timeline-desc { 
      color: #6b7280; 
      font-size: 14px; 
    } 
    </style>
    <div class="timeline"> 
      <div class="timeline-entry">
         <div class="timeline-time">10:00 AM – 11:00 AM</div>
          <div class="timeline-desc">🌍 Open Source 101 – Intro to Git & GitHub basics</div>
      </div> 
      <div class="timeline-entry">
         <div class="timeline-time">11:15 AM – 2:00 PM</div>
          <div class="timeline-desc">🤝 Contribution Sprint – Work on repos, make PRs with mentors</div>
      </div> 
      <div class="timeline-entry">
         <div class="timeline-time">2:30 PM – 4:00 PM</div> 
          <div class="timeline-desc">🏆 Showcase & Networking – Share contributions + swag distribution</div> 
      </div> 
    </div>
    """,
    unsafe_allow_html=True,
  )

# -------------------------
# Location
# -------------------------
st.subheader("📍 Event Location")
st.markdown("**Galgotias University** — Greater Noida, Uttar Pradesh, Sector 17-A")
st.map(pd.DataFrame({"lat": [28.474387], "lon": [77.503990]}), zoom=14)

st.write("---")

# -------------------------
# Footer
# -------------------------
st.markdown(
    """
    <div style="text-align:center; padding:10px 0 40px 0;">
      <a href="https://gdg.community.dev" target="_blank">🌐 GDG Website</a> |
      <a href="https://www.instagram.com/gdgocgu" target="_blank">📸 Instagram</a> |
      <a href="https://www.linkedin.com/company/gdg-on-campus-galgotias-university/" target="_blank">💼 LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True,
)














