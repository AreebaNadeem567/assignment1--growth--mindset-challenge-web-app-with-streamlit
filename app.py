# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
# import time
# from datetime import date
# import random

# # App Title
# st.set_page_config(page_title="Daily Motivation & Productivity Hub", page_icon="🌟")
# st.title("🌟 Daily Motivation & Productivity Hub")

# # Sidebar for Navigation
# st.sidebar.header("📌 Quick Navigation")
# page = st.sidebar.radio("Go to:", [
#     "🏡 Home", "📅 Habit Tracker", "💭 Daily Motivation", "📖 Inspirational Stories",
#     "🎯 Goal Setting", "📝 Productivity Tips", "🤔 Self-Reflection", "🧠 Brain Teasers", "🧠 Growth Mindset"
# ])

# # Home Page
# if page == "🏡 Home":
#     st.header("Welcome to Your Daily Motivation & Productivity Hub! 🚀")
#     st.markdown("""
#     ### Why Focus on Productivity & Motivation?
#     ✅ **Stay Inspired**: Start each day with positive energy.  
#     ✅ **Build Consistent Habits**: Small steps lead to big success.  
#     ✅ **Set and Achieve Goals**: Turn your dreams into reality.  
#     ✅ **Develop a Growth Mindset**: Keep learning and improving!  
#     """)
#     st.image("https://media.istockphoto.com/id/1183245141/photo/inspiration-motivation-message-on-a-road.webp", use_container_width=True)
#     st.success("Today is a new beginning! Make the most of it! 🚀")
    
#     # Add a motivational quote of the day
#     quotes = [
#         "The only way to do great work is to love what you do. - Steve Jobs",
#         "Believe you can and you're halfway there. - Theodore Roosevelt",
#         "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
#         "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
#     ]
#     st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# # Habit Tracker
# elif page == "📅 Habit Tracker":
#     st.header("📅 Habit Tracker")
#     habits = ["Exercise", "Read", "Meditate", "Drink Water", "Healthy Eating"]
    
#     for habit in habits:
#         st.checkbox(f"Did you {habit.lower()} today?")
    
#     if st.button("Save Progress"):
#         st.success("Great job! Keep up the good work!")
#         st.balloons()
    
#     # Add a streak counter
#     streak = st.session_state.get('streak', 0)
#     st.write(f"🔥 Current Streak: {streak} days")
#     if st.button("Increment Streak"):
#         streak += 1
#         st.session_state.streak = streak
#         st.success(f"New streak: {streak} days!")

# # Daily Motivation
# elif page == "💭 Daily Motivation":
#     st.header("💭 Your Daily Dose of Motivation")
#     quotes = [
#         "🌟 *Believe in yourself and all that you are!*", 
#         "🚀 *Small daily improvements lead to stunning results!*", 
#         "🔥 *Your potential is endless. Keep going!*", 
#         "💡 *Work hard in silence, let success make the noise.*",
#         "🌱 *Your only limit is the one you set yourself!*",
#         "💪 *Success is the sum of small efforts, repeated daily.*"
#     ]
#     st.success(f"💡 **Today's Motivation:** {quotes[date.today().day % len(quotes)]}")
#     st.info("Tip: Write down your top 3 priorities for today!")
#     priorities = []
#     for i in range(3):
#         priority = st.text_input(f"📌 Priority {i+1}:")
#         if priority:
#             priorities.append(priority)
    
#     if priorities:
#         st.write("Your priorities for today:")
#         for i, priority in enumerate(priorities, 1):
#             st.write(f"{i}. {priority}")
    
#     # Motivation Level
#     motivation_level = st.slider("Rate your motivation level today:", 0, 100, 50)
#     fig, ax = plt.subplots()
#     ax.bar(["Motivation Level"], [motivation_level], color='orange')
#     ax.set_ylabel("Percentage")
#     ax.set_ylim(0, 100)
#     st.pyplot(fig)

# # Inspirational Stories
# elif page == "📖 Inspirational Stories":
#     st.header("📖 Real-Life Success Stories")
#     stories = [
#         ("💡 **Elon Musk**", "Started multiple companies and transformed industries."),
#         ("📚 **J.K. Rowling**", "Rejected 12 times before publishing Harry Potter."),
#         ("🏀 **Michael Jordan**", "Was cut from his high school team but became an icon."),
#         ("🌍 **Nelson Mandela**", "Spent 27 years in prison and changed a nation."),
#         ("🎶 **Ed Sheeran**", "Slept on sofas while pursuing music, now a global icon.")
#     ]
#     for name, story in stories:
#         st.subheader(name)
#         st.write(story)
#         if st.button(f"Learn more about {name.split()[1]}", key=name):
#             st.write(f"Showing more details about {name}...")
#             # Here you can add more detailed information about each person
    
#     # Add a feature for users to submit their own inspirational stories
#     st.subheader("Share Your Own Inspirational Story")
#     user_story = st.text_area("Your story:")
#     if st.button("Submit Story"):
#         st.success("Thank you for sharing your story!")
#         # Here you can add logic to save the story

# # Goal Setting
# elif page == "🎯 Goal Setting":
#     st.header("🎯 Set Your Goals")
#     st.write("Setting clear goals is the first step towards achieving them.")
    
#     goal_types = ["Short-term", "Medium-term", "Long-term"]
#     for goal_type in goal_types:
#         st.subheader(f"{goal_type} Goals")
#         goal = st.text_input(f"Enter a {goal_type.lower()} goal:")
#         if goal:
#             st.write(f"Your {goal_type.lower()} goal: {goal}")
#             steps = st.text_area(f"Steps to achieve this {goal_type.lower()} goal:")
#             if steps:
#                 st.write("Your action plan:")
#                 for step in steps.split('\n'):
#                     st.write(f"- {step}")
    
#     if st.button("Save Goals"):
#         st.success("Goals saved successfully!")
#         st.balloons()

# # Productivity Tips
# elif page == "📝 Productivity Tips":
#     st.header("📝 Boost Your Productivity")
#     tips = [
#         "🕒 **Time Blocking** – Schedule time for tasks to improve focus.",
#         "📋 **Prioritize Tasks** – Use the Eisenhower Matrix for efficiency.",
#         "💤 **Get Enough Sleep** – Rested minds perform better.",
#         "📖 **Learn Something New** – Growth fuels productivity.",
#         "📵 **Reduce Distractions** – Limit social media to stay focused."
#     ]
#     st.write(f"💡 **Tip for Today:** {tips[date.today().day % len(tips)]}")
    
#     # Productivity Pie Chart
#     fig, ax = plt.subplots()
#     sizes = [60, 25, 15]
#     labels = ["Focused Work", "Breaks", "Distractions"]
#     colors = ["green", "yellow", "red"]
#     ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
#     ax.axis('equal')
#     st.pyplot(fig)
    
#     # Productivity Timer
#     st.subheader("Pomodoro Timer")
#     minutes = st.number_input("Set timer (minutes):", min_value=1, max_value=60, value=25)
#     if st.button("Start Timer"):
#         with st.empty():
#             for secs in range(minutes * 60, 0, -1):
#                 mm, ss = secs // 60, secs % 60
#                 st.metric("Time Remaining", f"{mm:02d}:{ss:02d}")
#                 time.sleep(1)
#             st.success("Time's up! Take a break.")
#             st.balloons()

# # Self-Reflection
# elif page == "🤔 Self-Reflection":
#     st.header("🤔 End-of-Day Reflection")
#     st.write("Reflect on your day to gain insights and improve.")
    
#     # Mood Tracker
#     mood = st.select_slider("How was your mood today?", options=["😔", "😐", "🙂", "😊", "😃"])
#     st.write(f"You felt {mood} today.")
    
#     # Accomplishments
#     accomplishments = st.text_area("What did you accomplish today?")
    
#     # Challenges
#     challenges = st.text_area("What challenges did you face?")
    
#     # Lessons Learned
#     lessons = st.text_area("What did you learn today?")
    
#     # Gratitude
#     gratitude = st.text_area("What are you grateful for today?")
    
#     if st.button("Save Reflection"):
#         st.success("✅ Reflection saved! Keep growing!")
#         st.balloons()
#         # Here you can add logic to save the reflection data

# # Brain Teasers
# elif page == "🧠 Brain Teasers":
#     st.header("🧠 Sharpen Your Mind")
#     riddles = [
#         ("🤔 **What has keys but can't open locks?**", "A piano"),
#         ("🔍 **What has to be broken before you can use it?**", "An egg"),
#         ("🎭 **The more you take, the more you leave behind. What is it?**", "Footsteps"),
#         ("❓ **I speak without a mouth and hear without ears. What am I?**", "An echo")
#     ]
    
#     question, answer = riddles[date.today().day % len(riddles)]
#     st.write(question)
#     user_answer = st.text_input("Your answer:")
#     if st.button("Check Answer"):
#         if user_answer.lower() == answer.lower():
#             st.success("Correct! Well done!")
#             st.balloons()
#         else:
#             st.error(f"Not quite. The correct answer is: {answer}")
    
#     # Add a new brain teaser game
#     st.subheader("Number Sequence Game")
#     sequence = [1, 3, 6, 10, 15]
#     st.write(f"What's the next number in this sequence? {sequence}")
#     next_number = st.number_input("Your answer:", min_value=1, step=1)
#     if st.button("Check Sequence"):
#         if next_number == 21:
#             st.success("Correct! The sequence is the sum of consecutive integers.")
#         else:
#             st.error("Not quite. Try again!")

# # Growth Mindset
# elif page == "🧠 Growth Mindset":
#     st.header("🧠 Develop a Growth Mindset")
#     st.markdown("""
#     ### What is a Growth Mindset?
#     A growth mindset is the belief that abilities and intelligence can be developed with effort, learning, and persistence.
    
#     ### Key Principles:
#     1. Embrace challenges
#     2. Persist in the face of setbacks
#     3. See effort as the path to mastery
#     4. Learn from criticism
#     5. Find lessons and inspiration in the success of others
#     """)
    
#     # Growth Mindset Quiz
#     st.subheader("Growth Mindset Quiz")
#     questions = [
#         "I believe I can always improve my skills.",
#         "I see challenges as opportunities to grow.",
#         "I learn from my mistakes and try again.",
#         "I'm inspired by the success of others.",
#         "I believe effort is the key to mastery."
#     ]
#     score = 0
#     for q in questions:
#         answer = st.radio(q, ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"])
#         if answer in ["Agree", "Strongly Agree"]:
#             score += 1
    
#     if st.button("Calculate Growth Mindset Score"):
#         st.write(f"Your Growth Mindset Score: {score}/5")
#         if score == 5:
#             st.success("Excellent! You have a strong growth mindset!")
#         elif score >= 3:
#             st.info("Good job! You're on your way to developing a strong growth mindset.")
#         else:
#             st.warning("There's room for improvement. Keep working on developing your growth mindset!")
    
#     # Growth Mindset Challenge
#     st.subheader("Daily Growth Mindset Challenge")
#     challenges = [
#         "Try something new today and reflect on what you learned.",
#         "Reframe a recent failure as a learning opportunity.",
#         "Ask for feedback on a recent project and act on it.",
#         "Set a challenging goal and create a plan to achieve it.",
#         "Practice positive self-talk when facing a difficult task."
#     ]
#     st.write(f"Today's Challenge: {random.choice(challenges)}")
    
#     if st.button("I Accept the Challenge"):
#         st.success("Great! Embrace the challenge and grow!")
#         st.balloons()

# # Add a footer
# st.markdown("---")
# st.markdown("Built with ❤️ using Streamlit | © 2023 Daily Motivation & Productivity Hub")



import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import date
import random

# App Title
st.set_page_config(page_title="Daily Motivation & Productivity Hub", page_icon="🌟")
st.title("🌟 Daily Motivation & Productivity Hub")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "🗓 Habit Tracker", "💭 Daily Motivation", "📚 Inspirational Stories",
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
    
    # Add a motivational quote of the day
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Habit Tracker
elif page == "🗓 Habit Tracker":
    st.header("🗓 Habit Tracker")
    habits = ["Exercise", "Read", "Meditate", "Drink Water", "Healthy Eating"]
    habit_status = {}
    
    for habit in habits:
        habit_status[habit] = st.checkbox(f"Did you {habit.lower()} today?")
    
    if st.button("Save Progress"):
        st.success("Great job! Keep up the good work!")
        st.balloons()
    
    # Add a streak counter
    streak = st.session_state.get('streak', 0)
    st.write(f"🔥 Current Streak: {streak} days")
    if st.button("Increment Streak"):
        streak += 1
        st.session_state.streak = streak
        st.success(f"New streak: {streak} days!")
    
    # Bar Chart Visualization
    completed_habits = sum(habit_status.values())
    fig, ax = plt.subplots()
    ax.bar(habits, [1 if habit_status[h] else 0 for h in habits], color=['green' if habit_status[h] else 'red' for h in habits])
    ax.set_ylabel("Completed (1) / Not Completed (0)")
    ax.set_title("Habit Completion Status")
    st.pyplot(fig)
    
    # Pie Chart Visualization
    labels = ["Completed", "Not Completed"]
    sizes = [completed_habits, len(habits) - completed_habits]
    colors = ['green', 'red']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

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
    priorities = []
    for i in range(3):
        priority = st.text_input(f"📌 Priority {i+1}:")
        if priority:
            priorities.append(priority)
    
    if priorities:
        st.write("Your priorities for today:")
        for i, priority in enumerate(priorities, 1):
            st.write(f"{i}. {priority}")
    
    # Motivation Level
    motivation_level = st.slider("Rate your motivation level today:", 0, 100, 50)
    fig, ax = plt.subplots()
    ax.bar(["Motivation Level"], [motivation_level], color='orange')
    ax.set_ylabel("Percentage")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2053 Daily Motivation & Productivity Hub")

