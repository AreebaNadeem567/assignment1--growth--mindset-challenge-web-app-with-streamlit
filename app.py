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
    
    fig, ax = plt.subplots()
    ax.bar(["Motivation Level"], [np.random.randint(50, 100)], color='orange')
    ax.set_ylabel("Percentage")
    st.pyplot(fig)

# Inspirational Stories
elif page == "📖 Inspirational Stories":
    st.header("📖 Real-Life Success Stories")
    stories = [
        ("💡 **Elon Musk**", "Started multiple companies and transformed industries."),
        ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter."),
        ("🏀 **Michael Jordan**", "Was cut from his high school team but became an icon."),
        ("🌍 **Nelson Mandela**", "Spent 27 years in prison and changed a nation."),
        ("🎶 **Ed Sheeran**", "Slept on sofas while pursuing music, now a global icon.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)
    st.button("Read More Stories")

# Productivity Tips
elif page == "📝 Productivity Tips":
    st.header("📝 Boost Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
        "💤 **Get Enough Sleep** – Rested minds perform better.",
        "📖 **Learn Something New** – Growth fuels productivity.",
        "📵 **Reduce Distractions** – Limit social media to stay focused."
    ]
    st.write(f"💡 **Tip for Today:** {tips[date.today().day % len(tips)]}")
    
    fig, ax = plt.subplots()
    ax.pie([60, 25, 15], labels=["Focused Work", "Breaks", "Distractions"], autopct='%1.1f%%', colors=["green", "yellow", "red"])
    st.pyplot(fig)

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 End-of-Day Reflection")
    journal = st.text_area("📖 Write about your achievements, challenges, and lessons learned:")
    
    if st.button("Save Reflection"):
        st.success("✅ Reflection saved! Keep growing!")
        st.balloons()

# Brain Teasers
elif page == "🧠 Brain Teasers":
    st.header("🧠 Sharpen Your Mind")
    riddles = [
        ("🤔 **What has keys but can't open locks?**", "A piano"),
        ("🔍 **What has to be broken before you can use it?**", "An egg"),
        ("🎭 **The more you take, the more you leave behind. What is it?**", "Footsteps"),
        ("❓ **I speak without a mouth and hear without ears. What am I?**", "An echo")
    ]
    
    question, answer = riddles[date.today().day % len(riddles)]
    st.write(question)
    if st.button("Show Answer"):
        time.sleep(1)
        st.success(f"✅ **Answer:** {answer}")
        st.balloons()

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
    """)
    st.progress(np.random.randint(50, 100))

# Footer
st.markdown("---")
st.markdown("💡 *Created with ❤️ using Streamlit. Stay motivated!*")
