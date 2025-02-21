






import streamlit as st
import matplotlib.pyplot as plt
from datetime import date
import time

# App Title
st.title("🚀 Motivation & Productivity Hub")

# Navigation Tabs
options = ["🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Success Stories", "🎯 Goal Setting", "📝 Productivity Tips", "🤔 Reflection", "🧠 Brain Teasers"]
page = st.selectbox("🔍 Choose a section:", options)

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Productivity Hub! ✨")
    st.markdown("""
    🔥 **Stay Inspired & Productive!**
    - Set and track your goals 🎯
    - Build productive habits ✅
    - Daily motivation & tips 💡
    """)
    st.image("https://source.unsplash.com/800x400/?motivation,success", use_column_width=True)

# Habit Tracker
elif page == "📅 Habit Tracker":
    st.header("📅 Track Your Habit Progress")
    habit = st.text_input("Enter a habit:")
    days = st.slider("Days consistent:", 1, 30, 5)
    
    fig, ax = plt.subplots()
    ax.bar([habit], [days], color="blue")
    ax.set_ylabel("Days Tracked")
    st.pyplot(fig)
    
    if st.button("Save Progress"):
        st.balloons()
        st.success(f"🎯 Keep going! '{habit}' is becoming a habit!")

# Daily Motivation
elif page == "💭 Daily Motivation":
    st.header("💭 Daily Motivation")
    quotes = [
        "Believe in yourself!", 
        "Every day is a new chance!", 
        "Push your limits!", 
        "Stay focused & never give up!"
    ]
    st.write(f"💡 **Today's Quote:** {quotes[date.today().day % len(quotes)]}")
    if st.button("Inspire Me"):
        st.balloons()

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Real-Life Success Stories")
    stories = [
        ("💡 **Elon Musk**", "Transformed multiple industries."),
        ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter."),
        ("🏀 **Michael Jordan**", "Cut from his school team but became a legend.")
    ]
    for name, story in stories:
        st.subheader(name)
        st.write(story)
    if st.button("Get Inspired"):
        st.balloons()

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Goals")
    goal = st.text_input("Your Goal:")
    deadline = st.date_input("Deadline:")
    if st.button("Save Goal"):
        st.balloons()
        st.success(f"✅ Goal '{goal}' set for {deadline}!")

# Productivity Tips
elif page == "📝 Productivity Tips":
    st.header("📝 Productivity Hacks")
    tips = [
        "Use time blocking to focus better.",
        "Prioritize tasks using the Eisenhower Matrix.",
        "Take breaks to boost efficiency.",
        "Sleep well to perform better."
    ]
    st.write(f"💡 **Today's Tip:** {tips[date.today().day % len(tips)]}")
    if st.button("Boost Productivity"):
        st.balloons()

# Self-Reflection
elif page == "🤔 Reflection":
    st.header("🤔 End-of-Day Reflection")
    journal = st.text_area("Write your thoughts:")
    if st.button("Save Reflection"):
        st.balloons()
        st.success("✅ Reflection saved! Keep growing!")

# Brain Teasers
elif page == "🧠 Brain Teasers":
    st.header("🧠 Sharpen Your Mind")
    riddles = [
        ("What has keys but can't open locks?", "A piano"),
        ("What has to be broken before you can use it?", "An egg"),
        ("The more you take, the more you leave behind. What is it?", "Footsteps")
    ]
    question, answer = riddles[date.today().day % len(riddles)]
    st.write(question)
    if st.button("Show Answer"):
        st.balloons()
        st.write(f"✅ **Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("💡 *Created with ❤️ using Streamlit. Stay inspired!*")










