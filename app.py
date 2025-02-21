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

    # Graph
    fig, ax = plt.subplots()
    factors = ["Motivation", "Productivity", "Energy", "Focus"]
    scores = np.random.randint(60, 100, size=4)
    ax.bar(factors, scores, color=['blue', 'orange', 'green', 'red'])
    ax.set_ylabel("Daily Score")
    ax.set_title("Daily Performance Metrics")
    st.pyplot(fig)

# Daily Motivation
elif page == "💭 Daily Motivation":
    st.header("💭 Your Daily Dose of Motivation")
    st.write("💡 Stay focused and energized! Here's your quote for today:")
    quotes = [
        "🌟 *Believe in yourself and all that you are!*", 
        "🚀 *Small daily improvements lead to stunning results!*", 
        "🔥 *Your potential is endless. Keep going!*", 
        "💡 *Work hard in silence, let success make the noise.*",
        "🌱 *Your only limit is the one you set yourself!*",
        "💪 *Success is the sum of small efforts, repeated daily.*"
    ]
    st.success(quotes[date.today().day % len(quotes)])
    
    st.info("Tip: Write down your top 3 priorities for today!")
    st.text_input("📌 Your top priority today:")

# Productivity Tips
elif page == "📝 Productivity Tips":
    st.header("📝 Boost Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
        "💤 **Get Enough Sleep** – Rested minds perform better.",
        "📖 **Learn Something New** – Growth fuels productivity.",
        "🎯 **Set SMART Goals** – Make goals specific and achievable.",
        "🧘 **Take Breaks** – Short breaks boost efficiency."
    ]
    st.write(f"💡 **Tip for Today:** {tips[date.today().day % len(tips)]}")
    
    # Graph
    fig, ax = plt.subplots()
    tasks = ["Completed", "Pending", "In Progress"]
    task_data = np.random.randint(5, 15, size=3)
    ax.pie(task_data, labels=tasks, autopct='%1.1f%%', colors=['green', 'red', 'orange'])
    ax.set_title("Task Breakdown")
    st.pyplot(fig)

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 End-of-Day Reflection")
    journal = st.text_area("📖 Write about your achievements, challenges, and lessons learned:")
    mood = st.slider("How was your day?", 1, 10, 5)
    
    if st.button("Save Reflection"):
        st.success("✅ Reflection saved! Keep growing!")
        st.balloons()
    
    # Graph
    fig, ax = plt.subplots()
    moods = ["Bad", "Okay", "Good", "Great", "Amazing"]
    ax.bar(moods, np.random.randint(1, 10, size=5), color=['red', 'orange', 'yellow', 'lightgreen', 'green'])
    ax.set_ylabel("Mood Score")
    ax.set_title("Mood Over Time")
    st.pyplot(fig)

# Brain Teasers
elif page == "🧠 Brain Teasers":
    st.header("🧠 Sharpen Your Mind")
    riddles = [
        ("🤔 **What has keys but can't open locks?**", "A piano"),
        ("🔍 **What has to be broken before you can use it?**", "An egg"),
        ("🎭 **The more you take, the more you leave behind. What is it?**", "Footsteps"),
        ("🧩 **I have cities but no houses, mountains but no trees, and water but no fish. What am I?**", "A map"),
        ("🌀 **The more you remove from me, the bigger I get. What am I?**", "A hole")
    ]
    question, answer = riddles[date.today().day % len(riddles)]
    st.write(question)
    if st.button("Show Answer"):
        st.write(f"✅ **Answer:** {answer}")
        st.snow()

# Footer
st.markdown("---")
st.markdown("💡 *Created with ❤️ using Streamlit. Stay motivated!*")
