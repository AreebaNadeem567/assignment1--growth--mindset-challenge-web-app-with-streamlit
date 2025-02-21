
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

    # Motivational Quote of the Day
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    st.info(f"💡 **Quote of the Day:** {random.choice(quotes)}")

# Habit Tracker
elif page == "📅 Habit Tracker":
    st.header("📅 Habit Tracker")
    habits = ["Exercise", "Read", "Meditate", "Drink Water", "Healthy Eating"]
    
    progress = {habit: st.slider(f"{habit}", 0, 100, 50) for habit in habits}
    
    if st.button("Save Progress"):
        st.success("Great job! Keep up the good work!")
        st.balloons()
    
    # Streak Counter
    if 'streak' not in st.session_state:
        st.session_state['streak'] = 0
    
    st.write(f"🔥 Current Streak: {st.session_state['streak']} days")
    if st.button("Increment Streak"):
        st.session_state['streak'] += 1
        st.success(f"New streak: {st.session_state['streak']} days!")
    
    # Progress Visualization
    st.subheader("Your Habit Progress")
    fig, ax = plt.subplots()
    ax.bar(progress.keys(), progress.values(), color=['blue', 'green', 'orange', 'red', 'purple'])
    ax.set_ylabel("Completion Percentage")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

# Daily Motivation
elif page == "💭 Daily Motivation":
    st.header("💭 Your Daily Dose of Motivation")
    motivation_quotes = [
        "🌟 *Believe in yourself and all that you are!*", 
        "🚀 *Small daily improvements lead to stunning results!*", 
        "🔥 *Your potential is endless. Keep going!*", 
        "💡 *Work hard in silence, let success make the noise.*"
    ]
    st.success(f"💡 **Today's Motivation:** {random.choice(motivation_quotes)}")

    priorities = [st.text_input(f"📌 Priority {i+1}:") for i in range(3)]
    if any(priorities):
        st.write("Your priorities for today:")
        for i, priority in enumerate(priorities, 1):
            if priority:
                st.write(f"{i}. {priority}")

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Goals")
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

# Growth Mindset
elif page == "🧠 Growth Mindset":
    st.header("🧠 Develop a Growth Mindset")
    st.markdown("""
    ### What is a Growth Mindset?
    A growth mindset is the belief that abilities and intelligence can be developed with effort, learning, and persistence.
    
    ### Key Principles:
    1. Embrace challenges
    2. Persist in the face of setbacks
    3. See effort as the path to mastery
    4. Learn from criticism
    5. Find lessons and inspiration in the success of others
    """)

    # Growth Mindset Quiz
    questions = [
        "I believe I can always improve my skills.",
        "I see challenges as opportunities to grow.",
        "I learn from my mistakes and try again.",
        "I'm inspired by the success of others.",
        "I believe effort is the key to mastery."
    ]
    score = sum([1 for q in questions if st.radio(q, ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]) in ["Agree", "Strongly Agree"]])
    
    if st.button("Calculate Growth Mindset Score"):
        st.write(f"Your Growth Mindset Score: {score}/5")
        if score == 5:
            st.success("Excellent! You have a strong growth mindset!")
        elif score >= 3:
            st.info("Good job! You're on your way to developing a strong growth mindset.")
        else:
            st.warning("There's room for improvement. Keep working on developing your growth mindset!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | © 2025 Daily Motivation & Productivity Hub")


