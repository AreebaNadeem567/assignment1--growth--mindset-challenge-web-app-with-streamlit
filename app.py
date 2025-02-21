import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.title("🚀 Mindset Mastery Challenge")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📊 Progress Dashboard", "📝 Daily Challenge", "💡 Growth Tips",
    "📖 Success Stories", "🎯 Goal Setting", "🤔 Self-Reflection", "🧠 Brain Boosters"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to the Mindset Mastery Challenge! 🎯")
    st.markdown("""
    ### Why Cultivate a Strong Mindset?
    ✅ **Overcome Obstacles**: Turn setbacks into stepping stones.  
    ✅ **Embrace Learning**: Growth comes from continuous effort.  
    ✅ **Stay Resilient**: Keep pushing forward, no matter what.  
    ✅ **Celebrate Progress**: Small wins lead to big successes.  
    ✅ **Stay Open-Minded**: Every day is an opportunity to grow.  
    """)
    st.image("https://media.istockphoto.com/id/1973623637/photo/mindset-loading-bar-concept.webp?a=1&b=1&s=612x612&w=0&k=20&c=_IrFcWJW6qoDNKpKgSNT4rY78RxoQYJo9kkPPXh7cFc=", use_container_width=True)

# Progress Dashboard
elif page == "📊 Progress Dashboard":
    st.header("📊 Track Your Growth")
    
    days = st.slider("How many days have you been working on your mindset?", 1, 30, 5)
    effort = st.slider("How much effort are you putting in (1-10)?", 1, 10, 7)

    st.session_state["days"] = days  
    
    fig, ax = plt.subplots()
    x = np.arange(1, days + 1)
    y = np.sin(x / 3) * 5 + effort
    ax.plot(x, y, marker='o', linestyle='-', color='blue', label='Effort Trend')
    ax.fill_between(x, y, alpha=0.3, color='skyblue')
    ax.set_xlabel("Days")
    ax.set_ylabel("Effort Level")
    ax.legend()
    st.pyplot(fig)

# Daily Challenge
elif page == "📝 Daily Challenge":
    st.header("📝 Unlock Today's Challenge")
    
    days = st.session_state.get("days", 1)

    challenges = [
        "🔹 Write a letter to your future self and read it in a month.",
        "🔹 Find one way to turn a setback into a lesson.",
        "🔹 Perform one act of kindness today.",
        "🔹 Learn a new skill for at least 10 minutes.",
        "🔹 Meditate or practice mindfulness for 5 minutes.",
        "🔹 Step out of your comfort zone and try something new."
    ]

    st.write("🎯 **Challenge for Today:**", challenges[days % len(challenges)])

# Growth Tips
elif page == "💡 Growth Tips":
    st.header("💡 Powerful Growth Insights")
    
    tips = [
        "🚀 **Turn Failures into Lessons** – Every setback is a setup for a comeback.",
        "🔥 **Master Self-Discipline** – Small habits shape your future.",
        "🎯 **Surround Yourself with Achievers** – Energy is contagious.",
        "📚 **Never Stop Learning** – Knowledge is the best investment.",
        "💪 **Resilience is Key** – The strongest minds push through hardships.",
        "✨ **Take Risks** – Growth happens outside the comfort zone.",
        "🌎 **Be Curious About Everything** – Curiosity leads to mastery."
    ]
    
    days = st.session_state.get("days", 1)
    st.markdown(f"💡 **Tip for Today:** {tips[days % len(tips)]}")

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Stories of Unbreakable Mindsets")
    
    stories = [
        ("🛠 **Elon Musk**", "Faced multiple failures but revolutionized tech and space exploration."),
        ("🎭 **Jim Carrey**", "Started with nothing, wrote himself a $10M check, and made it happen."),
        ("📖 **Stephen King**", "His first novel was rejected 30 times before success."),
        ("🎤 **Jay-Z**", "Rejected by labels but built his own empire."),
        ("⚽ **Cristiano Ronaldo**", "Worked relentlessly to become one of the best athletes in history.")
    ]
    
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Define & Achieve Your Goals")

    goal = st.text_input("🚀 Write down a goal that excites you:")
    deadline = st.date_input("📅 Set your target date:")
    
    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}! Keep pushing forward!")
        st.balloons()

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 Your Personal Growth Journal")
    
    journal = st.text_area("📖 Write down today’s insights, struggles, and wins:")
    
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Every step counts on your journey.")
        st.balloons()

# Brain Boosters
elif page == "🧠 Brain Boosters":
    st.header("🧠 Sharpen Your Mind with Fun Challenges")

    riddles = [
        ("💡 **What has hands but can't clap?**", "A clock"),
        ("🔑 **I have keys but open no locks. What am I?**", "A keyboard"),
        ("🎭 **The more you take, the more you leave behind. What am I?**", "Footsteps"),
        ("🕵️ **What gets wetter as it dries?**", "A towel")
    ]
    
    days = st.session_state.get("days", 1)
    question, answer = riddles[days % len(riddles)]
    
    st.write(question)
    if st.button("Reveal Answer"):
        st.write(f"✅ **Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("🌱 *Developed with ❤️ using Streamlit. Keep Growing!*")
