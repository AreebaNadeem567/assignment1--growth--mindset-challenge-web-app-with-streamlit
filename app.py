import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# App Title
st.title("🌟 Ultimate Productivity Challenge")
st.balloons()

# Sidebar Navigation
st.sidebar.header("🚀 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📈 Productivity Tracker", "📅 Daily Task", "📚 Learning Hub",
    "💡 Productivity Hacks", "📖 Inspiring Journeys", "🎯 Set Goals", "📝 Self-Reflection"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to the Ultimate Productivity Challenge! 🚀")
    st.markdown("""
    ### Why Focus on Productivity?
    ✅ **Manage Time Efficiently**: Work smarter, not harder.  
    ✅ **Stay Consistent**: Small steps lead to big achievements.  
    ✅ **Minimize Procrastination**: Stay on track with goals.  
    ✅ **Maximize Learning**: Make time for self-improvement.  
    ✅ **Boost Creativity**: A clear mind leads to innovative ideas.  
    """)
    st.image("https://media.istockphoto.com/id/1178414294/photo/time-management-and-productivity-concept.jpg?s=612x612&w=0&k=20&c=xjNEKH7-5V1YOi_s9pXAJMjEayIGuXUmJSk4ZxG-gDI=", use_container_width=True)

# Productivity Tracker
elif page == "📈 Productivity Tracker":
    st.header("📊 Your Productivity Progress")
    
    days = st.slider("How many days have you been tracking productivity?", 1, 30, 5)
    focus_hours = st.slider("How many hours do you focus daily? (1-10)", 1, 10, 6)
    breaks = st.slider("How many breaks do you take? (1-5)", 1, 5, 2)
    
    fig, ax = plt.subplots()
    ax.bar(["Days Tracked", "Focus Hours", "Breaks Taken"], [days, focus_hours, breaks], color=["blue", "green", "red"])
    ax.set_ylabel("Level")
    st.pyplot(fig)

# Daily Task
elif page == "📅 Daily Task":
    st.header("📅 Today's Productivity Task")
    
    tasks = [
        "📝 Plan your day using the Eisenhower Matrix.",
        "⏳ Use the Pomodoro technique for focused work.",
        "📖 Read 10 pages of a book on personal development.",
        "🧘 Meditate for 5 minutes to enhance focus.",
        "🚶 Take a 10-minute walk for mental clarity.",
        "📅 Schedule your most important task for the next day."
    ]
    st.write("✅ **Task for Today:**", tasks[days % len(tasks)])

# Learning Hub
elif page == "📚 Learning Hub":
    st.header("📚 Daily Learning Insight")
    
    insights = [
        "📖 Learning a new skill improves brain function.",
        "⏳ Time-blocking increases efficiency.",
        "🌱 Growth mindset leads to higher success.",
        "📊 Tracking habits enhances productivity.",
        "📵 Reducing screen time boosts focus.",
        "💡 Creative thinking comes from mental breaks."
    ]
    st.markdown(f"💡 **Insight for Today:** {insights[days % len(insights)]}")

# Productivity Hacks
elif page == "💡 Productivity Hacks":
    st.header("💡 Daily Productivity Tip")
    
    tips = [
        "🔥 **Use the 80/20 Rule** – Focus on 20% of tasks that bring 80% results.",
        "🔥 **Batch Similar Tasks** – Reduce mental load by grouping similar tasks.",
        "🔥 **Eliminate Distractions** – Turn off notifications while working.",
        "🔥 **Take Smart Breaks** – Short breaks keep you refreshed.",
        "🔥 **Prioritize Tasks** – Do the hardest task first.",
        "🔥 **Review & Reflect** – Track progress to stay accountable."
    ]
    st.markdown(f"💡 **Tip for Today:** {tips[days % len(tips)]}")

# Inspiring Journeys
elif page == "📖 Inspiring Journeys":
    st.header("📖 Productivity Success Stories")
    
    stories = [
        ("💡 **Elon Musk**", "Manages multiple companies by extreme time-blocking."),
        ("📚 **Bill Gates**", "Reads one book per week to maintain knowledge."),
        ("🎤 **Oprah Winfrey**", "Balances multiple projects with focus strategies."),
        ("💻 **Steve Jobs**", "Focused on simplicity to drive innovation.")
    ]
    
    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Setting
elif page == "🎯 Set Goals":
    st.header("🎯 Set Your Productivity Goals")
    
    goal = st.text_input("📝 Write your goal:")
    deadline = st.date_input("📅 Set a deadline:")
    
    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")
        st.balloons()

# Self-Reflection
elif page == "📝 Self-Reflection":
    st.header("📝 Daily Reflection Journal")
    
    journal = st.text_area("📖 Write about your day, your achievements, and challenges:")
    
    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep improving.")

# Footer
st.markdown("---")
st.markdown("🌟 *Developed with ❤️ using Streamlit. Stay Productive!*")
