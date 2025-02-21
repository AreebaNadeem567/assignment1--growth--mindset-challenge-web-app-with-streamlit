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

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set and Track Your Goals")
    goal = st.text_input("📝 Write your goal:")
    deadline = st.date_input("📅 Set a deadline:")
    
    if st.button("Save Goal"):
        st.success(f"✅ Goal '{goal}' set for {deadline}! Keep pushing forward!")
        st.balloons()

# Productivity Tips
elif page == "📝 Productivity Tips":
    st.header("📝 Boost Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
        "💤 **Get Enough Sleep** – Rested minds perform better.",
        "📖 **Learn Something New** – Growth fuels productivity.",
        "🚶 **Take Breaks** – A short walk boosts creativity and focus."
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
        ("🎭 **The more you take, the more you leave behind. What is it?**", "Footsteps"),
        ("💡 **I speak without a mouth and hear without ears. What am I?**", "An echo")
    ]
    
    question, answer = riddles[date.today().day % len(riddles)]
    st.write(question)
    
    if st.button("Show Answer"):
        time.sleep(1)
        st.write(f"✅ **Answer:** {answer}")

# Growth Mindset
elif page == "🧠 Growth Mindset":
    st.header("🧠 Develop a Growth Mindset")
    st.markdown("""
    ### What is a Growth Mindset?
    A growth mindset is the belief that abilities and intelligence can be developed with effort, learning, and persistence.
    
    ### How to Cultivate a Growth Mindset:
    ✅ **Embrace Challenges** – See difficulties as opportunities for growth.  
    ✅ **Learn from Criticism** – Feedback is a tool for improvement.  
    ✅ **Persist in the Face of Setbacks** – Failures are stepping stones to success.  
    ✅ **Celebrate Effort, Not Just Results** – Growth comes from trying, not just succeeding.  
    ✅ **Stay Curious** – Always be willing to learn and improve.  
    ✅ **Surround Yourself with Positivity** – Mindset is influenced by the company you keep.
    """)

# Footer
st.markdown("---")
st.markdown("💡 *Created with ❤️ using Streamlit. Stay motivated!*")

