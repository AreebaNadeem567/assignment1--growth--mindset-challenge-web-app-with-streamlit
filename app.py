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

# Productivity Tips
elif page == "📝 Productivity Tips":
    st.header("📝 Boost Your Productivity")
    tips = [
        "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
        "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
        "💤 **Get Enough Sleep** – Rested minds perform better.",
        "📖 **Learn Something New** – Growth fuels productivity.",
        "💪 **Take Regular Breaks** – Avoid burnout and maintain energy levels."
    ]
    st.write(f"💡 **Tip for Today:** {tips[date.today().day % len(tips)]}")
    st.success("Set a small challenge today and complete it! 🚀")
    
    # Graph
    fig, ax = plt.subplots()
    productivity_factors = ["Focus", "Energy", "Planning", "Execution"]
    scores = np.random.randint(50, 100, size=4)
    ax.bar(productivity_factors, scores, color=['blue', 'orange', 'green', 'red'])
    ax.set_ylabel("Efficiency %")
    ax.set_title("Productivity Factors")
    st.pyplot(fig)

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 End-of-Day Reflection")
    journal = st.text_area("📖 Write about your achievements, challenges, and lessons learned:")
    rating = st.slider("How was your day on a scale of 1-10?", 1, 10, 7)
    
    if st.button("Save Reflection"):
        st.success("✅ Reflection saved! Keep growing!")
        st.balloons()
    
    st.info("Reflection helps you improve daily. Keep journaling! 📝")

# Brain Teasers
elif page == "🧠 Brain Teasers":
    st.header("🧠 Sharpen Your Mind")
    riddles = [
        ("🤔 **What has keys but can't open locks?**", "A piano"),
        ("🔍 **What has to be broken before you can use it?**", "An egg"),
        ("🎭 **The more you take, the more you leave behind. What is it?**", "Footsteps"),
        ("🧩 **I speak without a mouth and hear without ears. What am I?**", "An echo")
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
    ### What is a Growth Mindset?
    A growth mindset is the belief that abilities and intelligence can be developed with effort, learning, and persistence.
    
    ### How to Cultivate a Growth Mindset:
    ✅ **Embrace Challenges** – See difficulties as opportunities for growth.  
    ✅ **Learn from Criticism** – Feedback is a tool for improvement.  
    ✅ **Persist in the Face of Setbacks** – Failures are stepping stones to success.  
    ✅ **Celebrate Effort, Not Just Results** – Growth comes from trying, not just succeeding.  
    ✅ **Stay Curious** – Always be willing to learn and improve.  
    """)
    st.success("Take one new challenge today and see how much you grow! 💪")
    
    # Graph
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
