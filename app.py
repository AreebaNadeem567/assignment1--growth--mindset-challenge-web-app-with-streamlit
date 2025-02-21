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
    st.header("📝 Today's Mindset Challenge")
    
    days = st.session_state.get("days", 1)

    challenges = [
        "🔹 Reflect on a challenge you faced and how you handled it.",
        "🔹 Do something outside your comfort zone.",
        "🔹 Replace a limiting belief with an empowering one.",
        "🔹 Teach someone something valuable.",
        "🔹 Read about a person who overcame great odds.",
        "🔹 Write down three things you're grateful for today."
    ]

    st.write("💡 **Challenge for Today:**", challenges[days % len(challenges)])

# Growth Tips
elif page == "💡 Growth Tips":
    st.header("💡 Daily Growth Insights")
    
    tips = [
        "🔥 **Learn from Feedback** – Growth comes from reflection.",
        "🔥 **Stay Consistent** – Small steps make a big impact.",
        "🔥 **Surround Yourself with Positivity** – Mindset is contagious.",
        "🔥 **Ask More Questions** – Curiosity fuels growth.",
        "🔥 **Set Micro-Goals** – Achieve one step at a time.",
        "🔥 **Celebrate Every Win** – Progress is worth acknowledging.",
        "🔥 **Commit to Lifelong Learning** – Knowledge is power."
    ]

    days = st.session_state.get("days", 1)
    st.markdown(f"💡 **Tip for Today:** {tips[days % len(tips)]}")

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Inspiring Growth Stories")
    
    stories = [
        ("💪 **Thomas Edison**", "Failed 1,000 times before inventing the light bulb."),
        ("🌍 **Oprah Winfrey**", "Was fired from her first TV job but kept pushing forward."),
        ("🎶 **Eminem**", "Rejected multiple times before making it big."),
        ("🏀 **Michael Jordan**", "Was cut from his high school basketball team but kept training."),
        ("📚 **J.K. Rowling**", "Her book was rejected by 12 publishers before becoming a hit.")
    ]
    
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Define Your Goals")

    goal = st.text_input("📝 Write down your goal:")
    deadline = st.date_input("📅 Set a deadline:")

    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")
        st.balloons()

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 Reflect on Your Journey")

    journal = st.text_area("📖 Write about your experiences, challenges, and lessons learned:")
    
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep growing.")
        st.balloons()

# Brain Boosters
elif page == "🧠 Brain Boosters":
    st.header("🧠 Strengthen Your Mind")

    riddles = [
        ("🤔 **I speak without a mouth and hear without ears. Who am I?**", "An echo"),
        ("🔍 **The more you take, the more you leave behind. What am I?**", "Footsteps"),
        ("🎭 **I have keys but open no locks. What am I?**", "A piano"),
        ("💡 **What has to be broken before you can use it?**", "An egg")
    ]
    
    days = st.session_state.get("days", 1)
    question, answer = riddles[days % len(riddles)]
    
    st.write(question)
    if st.button("Show Answer"):
        st.write(f"✅ **Answer:** {answer}")

# Footer
st.markdown("---")
st.markdown("🌱 *Developed with ❤️ using Streamlit. Keep Growing!*")
