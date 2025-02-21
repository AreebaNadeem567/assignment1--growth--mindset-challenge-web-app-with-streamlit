
import streamlit as st
import matplotlib.pyplot as plt
import random

# Dark Mode Toggle
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

def toggle_theme():
    st.session_state["dark_mode"] = not st.session_state["dark_mode"]

st.sidebar.button("🌙 Toggle Dark Mode" if not st.session_state["dark_mode"] else "☀️ Toggle Light Mode", on_click=toggle_theme)

# App Title
st.title("🚀 Growth Mindset Challenge")

# Sidebar Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📊 Progress Tracker", "📝 Daily Challenge", "💡 Tips for Growth",
    "📖 Success Stories", "🎯 Goal Setting", "🤔 Self-Reflection", "🧠 Brain Exercises"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to the Growth Mindset Challenge! 🎯")
    st.markdown("""
    ### Why Adopt a Growth Mindset?
    ✅ **Embrace Challenges**  
    ✅ **Learn from Mistakes**  
    ✅ **Persist Through Difficulties**  
    ✅ **Celebrate Effort**  
    ✅ **Stay Curious**  
    """)
    st.image("https://media.istockphoto.com/id/1973623637/photo/mindset-loading-bar-concept.webp", use_container_width=True)

# Progress Tracker
elif page == "📊 Progress Tracker":
    st.header("📊 Your Growth Progress")
    days = st.slider("Days Practiced", 1, 30, 5)
    effort = st.slider("Effort Level (1-10)", 1, 10, 7)
    
    fig, ax = plt.subplots()
    ax.bar(["Days", "Effort"], [days, effort], color=["blue", "green"])
    ax.set_ylabel("Level")
    st.pyplot(fig)

# Daily Challenge
elif page == "📝 Daily Challenge":
    st.header("📝 Today's Challenge")
    challenges = [
        "🔹 Identify one mistake you made today and what you learned.",
        "🔹 Try something new and challenging.",
        "🔹 Replace a negative thought with a positive one.",
        "🔹 Teach a skill to a friend.",
        "🔹 Write three things you're grateful for.",
        "🔹 Solve a puzzle or riddle."
    ]
    selected_challenge = random.choice(challenges)
    st.write("💡 **Challenge for Today:**", selected_challenge)
    answer = st.text_input("Write your response here:")
    if st.button("Submit"):
        st.success("Response Saved! Keep Growing! ✅")

# Tips for Growth
elif page == "💡 Tips for Growth":
    st.header("💡 Growth Tips")
    tips = [
        "🔥 Learn from Feedback",
        "🔥 Be Persistent",
        "🔥 Surround Yourself with Positive People",
        "🔥 Stay Curious",
        "🔥 Break Goals into Small Steps",
        "🔥 Celebrate Small Wins",
        "🔥 Develop a Learning Habit"
    ]
    st.markdown(f"💡 **Tip for Today:** {random.choice(tips)}")

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Inspirational Stories")
    stories = {
        "💪 Thomas Edison": "Failed 1,000+ times before inventing the light bulb.",
        "🌍 Oprah Winfrey": "Fired from her first TV job but never gave up.",
        "🎶 Eminem": "Rejected multiple times before becoming a rap legend.",
        "🏀 Michael Jordan": "Cut from his school team but became a legend.",
        "📚 J.K. Rowling": "Rejected by 12 publishers before success."
    }
    selected_story = random.choice(list(stories.items()))
    st.subheader(selected_story[0])
    st.write(selected_story[1])

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Goal")
    goal = st.text_input("Write your goal:")
    deadline = st.date_input("Set a deadline:")
    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")
        st.balloons()

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 Daily Reflection")
    journal = st.text_area("Write about your challenges and learnings:")
    if st.button("Save Reflection"):
        st.success("Reflection saved! Keep growing. ✅")

# Brain Exercises
elif page == "🧠 Brain Exercises":
    st.header("🧠 Brain Challenge")
    riddles = {
        "🤔 I speak without a mouth and hear without ears. Who am I?": "An echo",
        "🔍 The more you take, the more you leave behind. What am I?": "Footsteps",
        "🎭 I have keys but open no locks. What am I?": "A piano",
        "💡 What has to be broken before you can use it?": "An egg"
    }
    riddle, answer = random.choice(list(riddles.items()))
    st.write(riddle)
    if st.button("Show Answer"):
        st.write(f"✅ **Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("🌱 *Built with ❤️ using Streamlit. Keep Growing!*")
