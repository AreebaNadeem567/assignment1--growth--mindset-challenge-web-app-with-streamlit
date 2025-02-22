import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Title and Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌟")
st.title("🌟 Growth Mindset Challenge")

# Sidebar: Quick Navigation (listing all pages)
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", 
    "📅 Habit Tracker", 
    "💭 Daily Motivation", 
    "📖 Inspirational Stories",
    "🎯 Goal Setting", 
    "📝 Productivity Tips", 
    "🤔 Self-Reflection", 
    "🧠 Brain Teasers", 
    "🧠 Growth Mindset"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to Your Home Page")
    st.markdown("""
    ### Why Focus on Productivity & Motivation?
    ✅ **Stay Inspired:** Start each day with positive energy.  
    ✅ **Build Consistent Habits:** Small steps lead to big success.  
    ✅ **Set and Achieve Goals:** Turn your dreams into reality.  
    ✅ **Develop a Growth Mindset:** Keep learning and improving!
    """)
    st.image("https://m.media-amazon.com/images/I/51JYYBZTjaL._SL500_.jpg", use_container_width=True)
    st.success("Today is a new beginning! Make the most of it! 🚀")
    
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")
    
    # Weekly Motivation Trend Graph
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    motivation_levels = np.random.randint(60, 100, size=7)
    fig, ax = plt.subplots()
    ax.plot(days, motivation_levels, marker='o', linestyle='-', color='blue')
    ax.set_title("Weekly Motivation Trend")
    ax.set_ylabel("Motivation Level (%)")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Habit Tracker Page
elif page == "📅 Habit Tracker":
    st.header("📅 Habit Tracker")
    habits = ["Exercise", "Read", "Meditate", "Drink Water", "Healthy Eating"]
    for habit in habits:
        st.checkbox(f"Did you {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Keep up the good work!")
        st.balloons()
    
    weekly_progress = {habit: random.randint(0, 7) for habit in habits}
    fig, ax = plt.subplots()
    ax.bar(weekly_progress.keys(), weekly_progress.values(), color='green')
    ax.set_title("Weekly Habit Progress")
    ax.set_ylabel("Days Completed")
    ax.set_ylim(0, 7)
    st.pyplot(fig)
    
    streak = st.session_state.get('streak', 0)
    st.write(f"🔥 Current Streak: {streak} days")
    if st.button("Increment Streak"):
        streak += 1
        st.session_state.streak = streak
        st.success(f"New streak: {streak} days!")

# Daily Motivation Page
elif page == "💭 Daily Motivation":
    st.header("💭 Daily Dose of Motivation")
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
    priorities = []
    for i in range(3):
        priority = st.text_input(f"📌 Priority {i+1}:")
        if priority:
            priorities.append(priority)
    
    if priorities:
        st.write("Your priorities for today:")
        for i, priority in enumerate(priorities, 1):
            st.write(f"{i}. {priority}")
    
    motivation_level = st.slider("Rate your motivation level today:", 0, 100, 50)
    fig, ax = plt.subplots()
    ax.bar(["Motivation Level"], [motivation_level], color='orange')
    ax.set_ylabel("Percentage")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Inspirational Stories Page
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
        if st.button(f"Learn more about {name.split()[1]}", key=name):
            st.write(f"Showing more details about {name}...")
    
    st.subheader("Share Your Own Inspirational Story")
    user_story = st.text_area("Your story:")
    if st.button("Submit Story"):
        st.success("Thank you for sharing your story!")

# Goal Setting Page
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Goals")
    st.write("Setting clear goals is the first step towards achieving them.")
    
    goal_types = ["Short-term", "Medium-term", "Long-term"]
    for goal_type in goal_types:
        st.subheader(f"{goal_type} Goals")
        goal = st.text_input(f"Enter a {goal_type.lower()} goal:")
        if goal:
            st.write(f"Your {goal_type.lower()} goal: {goal}")
            steps = st.text_area(f"Steps to achieve this {goal_type.lower()} goal:")
            if steps:
                st.write("Your action plan:")
                for step in steps.split('\n'):
                    st.write(f"- {step}")
    
    if st.button("Save Goals"):
        st.success("Goals saved successfully!")
        st.balloons()

# Productivity Tips Page
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
    sizes = [60, 25, 15]
    labels = ["Focused Work", "Breaks", "Distractions"]
    colors = ["green", "yellow", "red"]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    
    st.subheader("Pomodoro Timer")
    minutes = st.number_input("Set timer (minutes):", min_value=1, max_value=60, value=25)
    if st.button("Start Timer"):
        with st.empty():
            for secs in range(minutes * 60, 0, -1):
                mm, ss = secs // 60, secs % 60
                st.metric("Time Remaining", f"{mm:02d}:{ss:02d}")
                time.sleep(1)
            st.success("Time's up! Take a break.")
            st.balloons()

# Self-Reflection Page
elif page == "🤔 Self-Reflection":
    st.header("🤔 End-of-Day Reflection")
    st.write("Reflect on your day to gain insights and improve.")
    
    mood = st.select_slider("How was your mood today?", options=["😔", "😐", "🙂", "😊", "😃"])
    st.write(f"You felt {mood} today.")
    
    accomplishments = st.text_area("What did you accomplish today?")
    challenges = st.text_area("What challenges did you face?")
    lessons = st.text_area("What did you learn today?")
    gratitude = st.text_area("What are you grateful for today?")
    
    if st.button("Save Reflection"):
        st.success("✅ Reflection saved! Keep growing!")
        st.balloons()

# Brain Teasers Page
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
    user_answer = st.text_input("Your answer:")
    if st.button("Check Answer"):
        if user_answer.lower() == answer.lower():
            st.success("Correct! Well done!")
            st.balloons()
        else:
            st.error(f"Not quite. The correct answer is: {answer}")
    
    st.subheader("Number Sequence Game")
    sequence = [1, 3, 6, 10, 15]
    st.write(f"What's the next number in this sequence? {sequence}")
    next_number = st.number_input("Your answer:", min_value=1, step=1)
    if st.button("Check Sequence"):
        if next_number == 21:
            st.success("Correct! The sequence is the sum of consecutive integers.")
        else:
            st.error("Not quite. Try again!")

# Growth Mindset Page
elif page == "🧠 Growth Mindset":
    st.header("🧠 Growth Mindset Challenge")
    
    # Quick Navigation List inside the page for clarity
    st.markdown("### Quick Navigation")
    st.markdown("""
    - 🏡 Home  
    - 📅 Habit Tracker  
    - 💭 Daily Motivation  
    - 📖 Inspirational Stories  
    - 🎯 Goal Setting  
    - 📝 Productivity Tips  
    - 🤔 Self-Reflection  
    - 🧠 Brain Teasers  
    - **🧠 Growth Mindset**
    """)
    
    st.markdown("""
    ### What is a Growth Mindset?
    A growth mindset is the belief that abilities and intelligence can be developed with effort, learning, and persistence.
    
    **Key Principles:**
    1. Embrace challenges  
    2. Persist in the face of setbacks  
    3. See effort as the path to mastery  
    4. Learn from criticism  
    5. Find lessons and inspiration in the success of others  
    """)
    
    st.subheader("Growth Mindset Quiz")
    questions = [
        "I believe I can always improve my skills.",
        "I see challenges as opportunities to grow.",
        "I learn from my mistakes and try again.",
        "I'm inspired by the success of others.",
        "I believe effort is the key to mastery."
    ]
    score = 0
    for q in questions:
        answer = st.radio(q, ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"])
        if answer in ["Agree", "Strongly Agree"]:
            score += 1
    
    if st.button("Calculate Growth Mindset Score"):
        st.write(f"Your Growth Mindset Score: {score}/5")
        if score == 5:
            st.success("Excellent! You have a strong growth mindset!")
        elif score >= 3:
            st.info("Good job! You're on your way to developing a strong growth mindset.")
        else:
            st.warning("There's room for improvement. Keep working on developing your growth mindset!")
    
    st.subheader("Daily Growth Mindset Challenge")
    challenges = [
        "Try something new today and reflect on what you learned.",
        "Reframe a recent failure as a learning opportunity.",
        "Ask for feedback on a recent project and act on it.",
        "Set a challenging goal and create a plan to achieve it.",
        "Practice positive self-talk when facing a difficult task.",
        "Step out of your comfort zone by starting a conversation with someone new.",
        "Spend 15 minutes reading about a subject you know nothing about.",
        "Write down one thing you're grateful for and one challenge you overcame."
    ]
    selected_challenge = random.choice(challenges)
    st.write(f"**Today's Challenge:** {selected_challenge}")
    
    plan = st.text_area("What's your plan to tackle this challenge?")
    if st.button("I Accept the Challenge"):
        if plan.strip() == "":
            st.warning("Please share your plan for the challenge!")
        else:
            st.success("Great! Embrace the challenge and grow!")
            st.write("Your plan:", plan)
            st.balloons()

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Growth Mindset Challenge")
