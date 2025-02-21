import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set dark theme
st.set_page_config(page_title="Mindset Mastery Challenge", layout="wide")
st.markdown("""
    <style>
        body { background-color: #121212; color: #e0e0e0; }
        .stTextInput>div>div>input { background-color: #333; color: #fff; }
        .stButton>button { background-color: #6200ea; color: white; }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🚀 Mindset Mastery Challenge")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📊 Mindset Tracker", "📝 Daily Mindset Challenge", "💡 Success Strategies",
    "📖 Inspiring Stories", "🎯 Goal Planning", "🤔 Reflection & Insights", "🧠 Brain Boosters"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to the Mindset Mastery Challenge! 🧠")
    st.markdown("""
    ### Why Strengthen Your Mindset?
    ✅ **Develop Resilience**: Overcome challenges with confidence.  
    ✅ **Cultivate Positivity**: Focus on growth and self-improvement.  
    ✅ **Enhance Problem-Solving Skills**: Learn to navigate obstacles effectively.  
    ✅ **Stay Motivated**: Build habits that drive long-term success.  
    """)
    st.image("https://media.istockphoto.com/id/1257468735/photo/creative-idea-bulb-lighting-on-colorful-background.webp", use_container_width=True)

# Mindset Tracker
elif page == "📊 Mindset Tracker":
    st.header("📊 Track Your Mindset Progress")
    days = st.slider("How many days have you been practicing a growth mindset?", 1, 30, 5)
    focus = st.slider("How focused were you today? (1-10)", 1, 10, 7)
    fig, ax = plt.subplots()
    x = np.arange(1, days + 1)
    y = np.sin(x / 3) * 5 + focus
    ax.plot(x, y, marker='o', linestyle='-', color='cyan', label='Mindset Growth')
    ax.fill_between(x, y, alpha=0.3, color='lightblue')
    ax.set_xlabel("Days")
    ax.set_ylabel("Mindset Level")
    ax.legend()
    st.pyplot(fig)
    st.button("🚀 Boost Your Mindset!")

# Daily Mindset Challenge
elif page == "📝 Daily Mindset Challenge":
    st.header("📝 Strengthen Your Mindset Today")
    challenges = [
        "💡 Identify one limiting belief and reframe it positively.",
        "📖 Read a motivational quote and reflect on its meaning.",
        "🧘 Practice 5 minutes of mindfulness or deep breathing.",
        "📓 Write down three things you learned from a recent challenge.",
        "🔄 Try something outside your comfort zone today."
    ]
    challenge = np.random.choice(challenges)
    st.write("🎯 **Today's Challenge:**", challenge)
    response = st.text_area("How did you complete the challenge?")
    if st.button("Submit Challenge"):
        st.success("🎉 Great job! Keep building a strong mindset.")
        st.balloons()

# Success Strategies
elif page == "💡 Success Strategies":
    st.header("💡 Strategies for a Powerful Mindset")
    strategies = [
        "🔥 Embrace failures as learning opportunities.",
        "🚀 Set clear, achievable goals and stay committed.",
        "💪 Practice self-discipline and eliminate distractions.",
        "📚 Keep learning – Knowledge fuels growth.",
        "💬 Surround yourself with positive, growth-oriented individuals."
    ]
    tip = np.random.choice(strategies)
    st.markdown(f"💡 **Today's Strategy:** {tip}")
    st.button("🔄 Refresh Strategy")

# Inspiring Stories
elif page == "📖 Inspiring Stories":
    st.header("📖 Stories of Mindset Transformation")
    stories = [
        ("🏀 **Michael Jordan**", "Was cut from his high school basketball team but became a legend."),
        ("📚 **J.K. Rowling**", "Faced multiple rejections before Harry Potter became a global success."),
        ("💡 **Elon Musk**", "Overcame failures and setbacks to revolutionize multiple industries."),
        ("🎶 **Eminem**", "Was rejected multiple times but persisted to become a rap icon."),
        ("🎬 **Walt Disney**", "Was told he lacked creativity but built an empire.")
    ]
    name, story = np.random.choice(stories)
    st.subheader(name)
    st.write(story)
    st.button("🔄 Another Story")

# Goal Planning
elif page == "🎯 Goal Planning":
    st.header("🎯 Define and Achieve Your Goals")
    goal = st.text_input("🚀 What mindset goal do you want to achieve?")
    deadline = st.date_input("📅 Set a deadline:")
    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}! Stay focused!")
        st.balloons()

# Reflection & Insights
elif page == "🤔 Reflection & Insights":
    st.header("🤔 Capture Your Mindset Journey")
    journal = st.text_area("📝 What progress have you made today? What mindset shifts have you noticed?")
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep growing mentally.")
        st.balloons()

# Brain Boosters
elif page == "🧠 Brain Boosters":
    st.header("🧠 Boost Your Mental Agility")
    riddles = [
        ("🧩 **I speak without a mouth and hear without ears. Who am I?**", "An echo"),
        ("💭 **The more you take, the more you leave behind. What am I?**", "Footsteps"),
        ("🔑 **I have keys but open no locks. What am I?**", "A piano"),
        ("🥚 **What has to be broken before you can use it?**", "An egg")
    ]
    question, answer = np.random.choice(riddles)
    st.write(question)
    if st.button("Reveal Answer"):
        st.write(f"✅ **Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("🧠 *Designed to help you master your mindset. Keep growing!*")
