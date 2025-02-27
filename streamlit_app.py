import streamlit as st
from backend import get_travel_options

st.title("🌍 AI-Powered Travel Planner")
st.markdown("Find the best travel options with AI!")

# User inputs
source = st.text_input("Enter Source City", placeholder="e.g., New York")
destination = st.text_input("Enter Destination City", placeholder="e.g., Los Angeles")

if st.button("Find Travel Options"):
    if source and destination:
        response = get_travel_options(source, destination)
        st.success("Here are your travel options:")
        st.write(response)
    else:
        st.warning("Please enter both source and destination.")
