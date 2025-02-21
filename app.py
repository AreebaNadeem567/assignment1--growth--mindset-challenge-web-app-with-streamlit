import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="🌱 Growth Mindset Challenge", layout='wide')
st.title("🚀 Growth Mindset Challenge")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Challenge", "Progress", "Reflection"])

# Sidebar for user details
st.sidebar.header("👤 Your Profile")
name = st.sidebar.text_input("Enter your name:")
current_date = datetime.now().strftime('%Y-%m-%d')

# Dark Mode Toggle
st.sidebar.header("🌙 Dark Mode")
dark_mode = st.sidebar.toggle("Enable Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
        body { background-color: #1E1E1E; color: white; }
        .stTextInput, .stTextArea, .stSelectbox, .stRadio { background-color: #333333; color: white; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Motivational Quote Section
quotes = [
    "“Success is not an accident, success is a choice.” – Stephen Curry",
    "“Failure is success in progress.” – Albert Einstein",
    "“The only way to do great work is to love what you do.” – Steve Jobs",
    "“Don’t let what you cannot do interfere with what you can do.” – John Wooden",
    "“Challenges are what make life interesting. Overcoming them is what makes life meaningful.”",
    "“Believe you can and you’re halfway there.” – Theodore Roosevelt",
    "“Hardships often prepare ordinary people for an extraordinary destiny.” – C.S. Lewis",
]
st.sidebar.write("💡 **Motivational Quote:**")
st.sidebar.write(f"📢 *{random.choice(quotes)}*")

if page == "Home":
    st.write("Welcome! Track your progress and embrace challenges with a growth mindset.")

elif page == "Challenge":
    st.subheader("🚀 Challenge of the Day")
    challenge_list = [
        "Try learning something completely new today!",
        "Embrace failure and reflect on what you can learn from it.",
        "Step outside your comfort zone and tackle a difficult task.",
        "Ask for constructive feedback and act on it.",
        "Teach someone else a concept you're mastering.",
        "Turn a negative thought into a positive one!",
        "Practice gratitude by writing three things you’re grateful for.",
        "Spend 15 minutes meditating or reflecting on your goals.",
        "Challenge yourself to avoid distractions and focus on deep work.",
    ]
    selected_challenge = st.selectbox("Choose a challenge to focus on today:", challenge_list)

elif page == "Progress":
    st.subheader("📊 Track Your Progress")
    progress_options = ["Not Started", "In Progress", "Completed"]
    progress = st.radio("How far along are you?", progress_options, index=0)
    
    # Initialize session state for progress tracking
    if "progress_data" not in st.session_state:
        st.session_state.progress_data = {"Not Started": 0, "In Progress": 0, "Completed": 0}
    
    if st.button("💾 Save Progress"):
        st.session_state.progress_data[progress] += 1
        st.success("✅ Your progress has been saved! Keep growing!")
    
    # Progress Visualization
    st.subheader("📈 Growth Mindset Progress Chart")
    progress_chart_data = st.session_state.progress_data
    fig, ax = plt.subplots()
    ax.bar(progress_chart_data.keys(), progress_chart_data.values(), color=['red', 'orange', 'green'])
    ax.set_ylabel("Count")
    ax.set_title("Progress Status")
    st.pyplot(fig)

elif page == "Reflection":
    st.subheader("✍️ Reflection Journal")
    reflection = st.text_area("Write about your experience today:")
    if st.button("💾 Save Reflection"):
        st.success("✅ Your reflection has been saved! Keep growing!")

st.sidebar.write("💡 Remember: Growth happens when you push yourself beyond your limits!")
