import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date

# App Title
st.title("🌟 Daily Motivation & Productivity Hub")
st.balloons()

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Success Stories",
    "🎯 Goal Setting", "📝 Productivity Tips", "🤔 Self-Reflection", "🧠 Brain Teasers", "🎲 Fun Activity"
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
    st.image("https://source.unsplash.com/800x400/?motivation,success", use_container_width=True)

# Habit Tracker with Improved Graph
elif page == "📅 Habit Tracker":
    st.header("📅 Track Your Daily Habits")
    habit = st.text_input("Enter a habit you're working on:")
    days = st.slider("How many days have you been consistent?", 1, 30, 5)
    
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * days / 10  # Sine wave to make graph visually appealing
    ax.plot(x, y, color='blue', linewidth=2)
    ax.set_title("Habit Progress Graph")
    st.pyplot(fig)
    
    if st.button("Save Progress"):
        st.success(f"🎯 Keep it up! {habit} is becoming a habit!")

# Daily Motivation
elif page == "💭 Daily Motivation":
    st.header("💭 Your Daily Dose of Motivation")
    
    quotes = [
        "🌟 *Believe in yourself and all that you are!*", 
        "🚀 *Small daily improvements lead to stunning results!*", 
        "🔥 *Your potential is endless. Keep going!*", 
        "💡 *Work hard in silence, let success make the noise.*"
    ]
    
    st.write(f"💡 **Today's Motivation:** {quotes[date.today().day % len(quotes)]}")

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Real-Life Success Stories")
    
    stories = [
        ("🚀 **Steve Jobs**", "Co-founded Apple and revolutionized technology."),
        ("📚 **Oprah Winfrey**", "Overcame struggles to become a media mogul."),
        ("⚽ **Cristiano Ronaldo**", "From poverty to becoming a football legend.")
    ]
    
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set and Track Your Goals")
    goal = st.text_input("📝 Write your goal:")
    deadline = st.date_input("📅 Set a deadline:")
    
    if st.button("Save Goal"):
        st.success(f"✅ Goal '{goal}' set for {deadline}! Keep pushing forward!")

# Productivity Tips
elif page == "📝 Productivity Tips":
    st.header("📝 Boost Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
        "💤 **Get Enough Sleep** – Rested minds perform better.",
        "📖 **Learn Something New** – Growth fuels productivity."
    ]
    st.write(f"💡 **Tip for Today:** {tips[date.today().day % len(tips)]}")

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 End-of-Day Reflection")
    journal = st.text_area("📖 Write about your achievements, challenges, and lessons learned:")
    
    if st.button("Save Reflection"):
        st.success("✅ Reflection saved! Keep growing!")

# Brain Teasers
elif page == "🧠 Brain Teasers":
    st.header("🧠 Sharpen Your Mind")
    riddles = [
        ("🤔 **What has keys but can't open locks?**", "A piano"),
        ("🔍 **What has to be broken before you can use it?**", "An egg"),
        ("🎭 **The more you take, the more you leave behind. What is it?**", "Footsteps")
    ]
    
    question, answer = riddles[date.today().day % len(riddles)]
    st.write(question)
    if st.button("Show Answer"):
        st.write(f"✅ **Answer:** {answer}")

# Fun Activity
elif page == "🎲 Fun Activity":
    st.header("🎲 Let's Play a Quick Game")
    activities = [
        ("💡 **Solve this:** What comes next in the sequence? 2, 4, 8, 16, __", "32"),
        ("🎭 **Riddle:** I speak without a mouth and hear without ears. What am I?", "An Echo"),
        ("🔢 **Math:** What is 15 + 27?", "42")
    ]
    
    question, answer = activities[date.today().day % len(activities)]
    st.write(question)
    if st.button("Show Answer 🎯"):
        st.write(f"✅ **Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("💡 *Created with ❤️ using Streamlit. Stay motivated!*")
