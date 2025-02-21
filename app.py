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

# Habit Tracker
elif page == "📅 Habit Tracker":
    st.header("📅 Track Your Daily Habits")
    habit = st.text_input("Enter a habit you're working on:")
    days = st.slider("How many days have you been consistent?", 1, 30, 5)
    
    fig, ax = plt.subplots()
    ax.plot(range(1, days + 1), np.random.randint(50, 100, days), marker='o', linestyle='-')
    ax.set_xlabel("Days")
    ax.set_ylabel("Consistency %")
    ax.set_title("Habit Progress Over Time")
    st.pyplot(fig)
    
    if st.button("Save Progress"):
        st.success(f"🎯 Keep it up! {habit} is becoming a habit!")

# Daily Motivation
elif page == "💭 Daily Motivation":
    st.header("💭 Your Daily Dose of Motivation")
    st.write("💡 Stay focused and energized! Here's your quote for today:")
    quotes = [
        "🌟 *Believe in yourself and all that you are!*", 
        "🚀 *Small daily improvements lead to stunning results!*", 
        "🔥 *Your potential is endless. Keep going!*", 
        "💡 *Work hard in silence, let success make the noise.*"
    ]
    st.success(quotes[date.today().day % len(quotes)])
    
    st.info("Tip: Write down your top 3 priorities for today!")

# Inspirational Stories
elif page == "📖 Inspirational Stories":
    st.header("📖 Real-Life Success Stories")
    stories = [
        ("💡 **Elon Musk**", "Started multiple companies and transformed industries."),
        ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter."),
        ("🏀 **Michael Jordan**", "Was cut from his high school team but became an icon.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)
    
    st.info("What’s your success story? Start creating it today!")

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set and Track Your Goals")
    goal = st.text_input("📝 Write your goal:")
    deadline = st.date_input("📅 Set a deadline:")
    priority = st.radio("Set Priority Level:", ["Low", "Medium", "High"])
    
    if st.button("Save Goal"):
        st.success(f"✅ Goal '{goal}' set for {deadline}! Priority: {priority} Keep pushing forward!")

    fig, ax = plt.subplots()
    categories = ["Short-term", "Mid-term", "Long-term"]
    progress = np.random.randint(40, 100, size=3)
    ax.bar(categories, progress, color=['purple', 'yellow', 'blue'])
    ax.set_ylabel("Completion %")
    ax.set_title("Goal Progress")
    st.pyplot(fig)

# Brain Teasers
elif page == "🧠 Brain Teasers":
    st.header("🧠 Sharpen Your Mind")
    riddles = [
        ("🤔 **What has keys but can't open locks?**", "A piano"),
        ("🔍 **What has to be broken before you can use it?**", "An egg"),
        ("🎭 **The more you take, the more you leave behind. What is it?**", "Footsteps"),
        ("🧩 **I have cities but no houses, mountains but no trees, and water but no fish. What am I?**", "A map")
    ]
    question, answer = riddles[date.today().day % len(riddles)]
    st.write(question)
    if st.button("Show Answer"):
        st.write(f"✅ **Answer:** {answer}")
        st.snow()

# Growth Mindset
elif page == "🧠 Growth Mindset":
    st.header("🧠 Develop a Growth Mindset")
    st.markdown("""
    ### How to Cultivate a Growth Mindset:
    ✅ **Embrace Challenges** – See difficulties as opportunities for growth.  
    ✅ **Learn from Criticism** – Feedback is a tool for improvement.  
    ✅ **Persist in the Face of Setbacks** – Failures are stepping stones to success.  
    ✅ **Stay Curious** – Always be willing to learn and improve.  
    """)
    
    fig, ax = plt.subplots()
    mindset_factors = ["Resilience", "Curiosity", "Effort", "Learning"]
    scores = np.random.randint(60, 100, size=4)
    ax.bar(mindset_factors, scores, color=['purple', 'yellow', 'blue', 'green'])
    ax.set_ylabel("Mindset Score")
    ax.set_title("Growth Mindset Factors")
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("💡 *Created with ❤️ using Streamlit. Stay motivated!*")
