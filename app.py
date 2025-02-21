import streamlit as st
import pandas as pd
import os
import json
import random
from io import BytesIO
import matplotlib.pyplot as plt

# Load or initialize data
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {"challenges": [], "journal": []}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

# Streamlit App Configuration
st.set_page_config(page_title="Success Mindset Hub", layout="wide")
st.title("🎈 Success Mindset Hub 🚀")
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Motivation Insights", "Quiz", "Journal & Reflection", "Data Visualization"])

# Home Page
if page == "Home":
    st.header("Welcome to the Success Mindset Hub! 🌟")
    st.write("Develop the mindset of successful people and achieve your dreams!")
    st.image("https://blog.iawomen.com/wp-content/uploads/2024/01/Depositphotos_682225278_S.jpg")
    st.balloons()
    st.subheader("Core Principles for Success")
    st.markdown("""
    - 🚀 **Take Initiative**: Don't wait for opportunities, create them.
    - 📚 **Keep Learning**: Knowledge is the key to success.
    - 💪 **Resilience Matters**: Every setback is a setup for a comeback.
    - 🎯 **Stay Focused**: Work consistently towards your goals.
    """)
    st.success("💡 *Success is not final, failure is not fatal: it is the courage to continue that counts.*")

# Motivation Insights
elif page == "Motivation Insights":
    st.header("📊 Motivation & Growth Insights")
    motivation_data = {
        "Factors": ["Hard Work", "Consistency", "Learning", "Risk-Taking", "Networking"],
        "Importance": [90, 80, 85, 70, 75]
    }
    df = pd.DataFrame(motivation_data)
    st.write("### Key Factors for Success")
    st.bar_chart(df.set_index("Factors"))

# Quiz Section
elif page == "Quiz":
    st.header("🧠 Success Mindset Quiz")
    questions = [
        {"q": "What is the most important trait for success?", "opts": ["Luck", "Hard Work", "Giving Up"], "a": "Hard Work"},
        {"q": "How should failures be viewed?", "opts": ["As lessons", "As final outcomes", "As setbacks"], "a": "As lessons"},
    ]
    score = sum(st.radio(q["q"], q["opts"], key=q["q"]) == q["a"] for q in questions)
    if st.button("Submit Quiz"):
        st.success(f"🎯 Your score: {score}/{len(questions)}")

# Journal & Reflection
elif page == "Journal & Reflection":
    st.header("📖 Journal & Reflection")
    journal_entry = st.text_area("Reflect on your success journey today:")
    if st.button("Save Entry"):
        if journal_entry.strip():
            data["journal"].append(journal_entry)
            save_data(data)
            st.success("✅ Entry saved!")
        else:
            st.error("Please write something before saving.")
    if data["journal"]:
        st.subheader("📜 Past Entries")
        for i, entry in enumerate(reversed(data["journal"])):
            st.write(f"🔹 *Entry {len(data['journal']) - i}:* {entry}")
    else:
        st.info("No journal entries yet. Start today!")

# Data Visualization
elif page == "Data Visualization":
    st.header("📊 Success Trends")
    df = pd.DataFrame({
        "Year": [2018, 2019, 2020, 2021, 2022, 2023],
        "Success Rate (%)": [50, 55, 65, 70, 80, 85]
    })
    fig, ax = plt.subplots()
    ax.plot(df["Year"], df["Success Rate (%)"], marker="o", linestyle="-", color="blue")
    ax.set_xlabel("Year")
    ax.set_ylabel("Success Rate (%)")
    ax.set_title("Success Rate Over the Years")
    st.pyplot(fig)
    st.balloons()

st.success("🎉 Keep striving for success! 🚀")
