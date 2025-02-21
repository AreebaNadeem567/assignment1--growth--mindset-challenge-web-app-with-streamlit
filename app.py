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
    st.success("Today is a new beginning! Make the most of it! 🚀")

# Habit Tracker
elif page == "📅 Habit Tracker":
    st.header("📅 Track Your Daily Habits")
    habit = st.text_input("Enter a habit you're working on:")
    days = st.slider("How many days have you been consistent?", 1, 30, 5)
    
    fig, ax = plt.subplots()
    ax.plot(range(1, days + 1), np.random.randint(1, 10, days), marker='o', linestyle='-')
    ax.set_xlabel("Days")
    ax.set_ylabel("Progress Level")
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
        "🌱 *Your only limit is the one you set yourself!*",
        "💪 *Success is the sum of small efforts, repeated daily.*"
    ]
    st.success(f"💡 **Today's Motivation:** {quotes[date.today().day % len(quotes)]}")
    st.info("Tip: Write down your top 3 priorities for today!")
    st.text_input("📌 Your top priority today:")

# Inspirational Stories
elif page == "📖 Inspirational Stories":
    st.header("📖 Real-Life Success Stories")
    stories = [
        ("💡 **Elon Musk**", "Started multiple companies and transformed industries."),
        ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter."),
        ("🏀 **Michael Jordan**", "Was cut from his high school team but became an icon."),
        ("🌍 **Nelson Mandela**", "Spent 27 years in prison and changed a nation.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)
    st.button("Read More Stories")

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set and Track Your Goals")
    goal = st.text_input("📝 Write your goal:")
    deadline = st.date_input("📅 Set a deadline:")
    milestones = st.text_area("📍 Define your key milestones:")
    
    if st.button("Save Goal"):
        st.success(f"✅ Goal '{goal}' set for {deadline}! Stay focused!")
        st.balloons()
    
    fig, ax = plt.subplots()
    ax.barh(["Milestone 1", "Milestone 2", "Milestone 3"], np.random.randint(10, 100, 3), color='green')
    ax.set_xlabel("Progress %")
    st.pyplot(fig)

# Brain Teasers
elif page == "🧠 Brain Teasers":
    st.header("🧠 Sharpen Your Mind")
    riddle = "🤔 What can travel around the world while staying in the same spot?"
    st.write(riddle)
    if st.button("Submit Answer"):
        time.sleep(1)
        st.success("A stamp!")
        st.balloons()

# Footer
st.markdown("---")
st.markdown("💡 *Created with ❤️ using Streamlit. Stay motivated!*")
