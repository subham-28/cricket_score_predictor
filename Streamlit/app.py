import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
pipe = joblib.load('Models/Pipe.pkl')

# Lists of teams & cities
teams = ['Bangladesh', 'Australia', 'New Zealand', 'Pakistan', 'Sri Lanka',
         'South Africa', 'West Indies', 'England', 'India', 'Zimbabwe']

cities = ['Lahore', 'Sydney', 'Chandigarh', 'Colombo', 'Mirpur', 'Pallekele',
          'Tarouba', 'Barbados', 'Chittagong', 'Durban', 'Cardiff',
          'Centurion', 'Pune', 'Bridgetown', 'Karachi', 'Providence',
          'Brisbane', 'Sylhet', 'Nottingham', 'Dubai', 'Melbourne', 'Delhi',
          'Wellington', 'Sharjah', 'Dhaka', 'Mount Maunganui', 'Dambulla',
          'St Lucia', 'Cape Town', 'Kandy', 'Harare', 'Abu Dhabi',
          'Hamilton', "St George's", 'Auckland', 'Gros Islet', 'London',
          'Birmingham', 'Chattogram', 'Trinidad', 'Rajkot', 'Bristol',
          'Johannesburg', 'Southampton', 'Rawalpindi', 'Mumbai',
          'Christchurch', 'Hambantota', 'Kingston', 'Lauderhill', 'Napier',
          'Manchester', 'Hobart', 'Adelaide', 'Nagpur', 'Perth', 'Kolkata',
          'Ahmedabad', 'Bangalore']

# ---------- 🌟 Custom CSS ----------
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0E1117;
        color: white;
        text-align: center;
        padding: 8px;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

# App title & description
st.markdown("# 🏏 Cricket Score Predictor")
st.markdown("⚡ **Predict the final score of a T20 match based on current situation!**")
st.markdown("---")

# Team selection with placeholder
team_options = ['-- Choose Team --'] + sorted(teams)

st.subheader("🧢 Select Teams")
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('🏏 Batting Team', team_options)
with col2:
    bowling_team = st.selectbox('🎯 Bowling Team', team_options)

# City selection with placeholder
city_options = ['-- Choose Venue --'] + sorted(cities)

st.subheader("📍 Match Details")
city = st.selectbox('🏟️ Venue / City', city_options)

# Match situation
st.subheader("📊 Current Match Situation")
col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input('✅ Current Score', min_value=0, value=0, step=1, format="%d")
with col4:
    overs = st.number_input('⏱️ Overs done (min 5.0, max 20.0)', min_value=5.0, max_value=20.0,
                            value=5.0, step=0.1, format="%.1f")
with col5:
    wickets = st.number_input('❌ Wickets Gone', min_value=0, max_value=10, value=0, step=1, format="%d")

last_five = st.number_input('🔥 Runs scored in last 5 overs', min_value=0, value=0, step=1, format="%d")

# Separator
st.markdown("---")

# Compute fractional part for validation
completed_overs = int(overs)
fractional_part = round((overs - completed_overs) * 10)

# Predict button
if st.button('🚀 Predict Final Score'):
    # Validation checks
    if batting_team == '-- Choose Team --' or bowling_team == '-- Choose Team --':
        st.error("⚠️ Please select both batting and bowling teams.")
    elif city == '-- Choose Venue --':
        st.error("⚠️ Please select the match venue/city.")
    elif batting_team == bowling_team:
        st.error("⚠️ Batting team and bowling team cannot be the same. Please select different teams.")
    elif fractional_part > 5:
        st.error("⚠️ Invalid overs: decimal part must be ≤ .5 (i.e., max 5 balls after decimal).")
    else:
        balls_bowled = completed_overs * 6 + fractional_part
        balls_left = 120 - balls_bowled
        wickets_left = 10 - wickets
        crr = current_score / overs if overs > 0 else 0

        # Create dataframe for prediction
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'current_score': [current_score],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'crr': [crr],
            'last_five': [last_five]
        })

        # Make prediction
        predicted_score = pipe.predict(input_df)
        st.header("🎯 Predicted Final Score: " + str(int(predicted_score[0])) )

# ---------- 🔗 Footer ----------
st.markdown('<div class="footer">Made by Subham Mohanty | Powered by Streamlit</div>', unsafe_allow_html=True)
