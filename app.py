import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date

# App Title
st.title("🌟 Daily Motivation & Productivity Hub")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Inspirational Stories",
    "🎯 Goal Setting", "📝 Productivity Tips", "🤔 Self-Reflection", "🧠 Brain Teasers", "🧠 Growth Mindset"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Daily Motivation & Productivity Hub! 🚀")
    st.markdown("""
    ### Why Focus on Productivity & Motivation?
    ✅ **Stay Inspired**: Start each day with positive energy.  
    ✅ **Build Consistent Habits**: Small steps lead to big success.  
    ✅ **Set and Achieve Goals**: Turn your dreams into reality.  
    ✅ **Develop a Growth Mindset**: Keep learning and improving!  
    """)
    st.image("https://media.istockphoto.com/id/1183245141/photo/inspiration-motivation-message-on-a-road.webp", use_container_width=True)

# Habit Tracker
elif page == "📅 Habit Tracker":
    st.header("📅 Track Your Daily Habits")
    habit = st.text_input("Enter a habit you're working on:")
    days = st.slider("How many days have you been consistent?", 1, 30, 5)
    
    fig, ax = plt.subplots()
    ax.pie([days, 30 - days], labels=["Tracked", "Remaining"], autopct="%1.1f%%", colors=["blue", "lightgray"])
    st.pyplot(fig)
    
    st.subheader("📊 Your Habit Progress")
    progress = np.random.randint(50, 100, size=7)
    days_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    fig, ax = plt.subplots()
    ax.plot(days_labels, progress, marker='o', linestyle='-', color='green')
    ax.set_ylabel("Consistency %")
    ax.set_title("Weekly Habit Consistency")
    st.pyplot(fig)
    
    if st.button("Save Progress"):
        st.success(f"🎯 Keep it up! {habit} is becoming a habit!")
        st.balloons()

# Daily Motivation
elif page == "💭 Daily Motivation":
    st.header("💭 Your Daily Dose of Motivation")
    
    quotes = [
        "🌟 *Believe in yourself and all that you are!*", 
        "🚀 *Small daily improvements lead to stunning results!*", 
        "🔥 *Your potential is endless. Keep going!*", 
        "💡 *Work hard in silence, let success make the noise.*",
        "🏆 *Every expert was once a beginner. Start now!*"
    ]
    
    st.write(f"💡 **Today's Motivation:** {quotes[date.today().day % len(quotes)]}")
    st.balloons()

# Inspirational Stories
elif page == "📖 Inspirational Stories":
    st.header("📖 Real-Life Success Stories")
    
    stories = [
        ("💡 **Elon Musk**", "Started multiple companies and transformed industries."),
        ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter."),
        ("🏀 **Michael Jordan**", "Was cut from his high school team but became an icon."),
        ("🎶 **Ed Sheeran**", "Once told he couldn't sing, now he's a global artist.")
    ]
    
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Footer
st.markdown("---")
st.markdown("💡 *Created with ❤️ using Streamlit. Stay motivated!*")
