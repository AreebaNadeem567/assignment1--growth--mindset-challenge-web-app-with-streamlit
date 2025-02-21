import streamlit as st
import pandas as pd
import os
import json
import random
from io import BytesIO

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
st.set_page_config(page_title="Growth Mindset Hub", layout="wide")
st.title("🚀 Growth Mindset Hub")
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Daily Challenge", "Quiz", "Journal & Reflection", "File Converter"])

# Home Page
if page == "Home":
    st.header("Welcome to the Growth Mindset Hub! 🌱")
    st.write("A growth mindset means believing in continuous learning and improvement.")
    st.image("https://blog.iawomen.com/wp-content/uploads/2024/01/Depositphotos_682225278_S.jpg")
    st.subheader("Why Cultivate a Growth Mindset?")
    st.markdown("""
    - 🌟 **Embrace Challenges**: See obstacles as opportunities.
    - 🧠 **Learn from Mistakes**: Use setbacks as stepping stones.
    - 🔥 **Develop Resilience**: Stay persistent in tough times.
    - 🎨 **Enhance Creativity**: Think outside the box.
    """)
    st.success("💡 *Mindset Shift: Hard work beats talent when talent doesn’t work hard.*")

# Daily Challenge
elif page == "Daily Challenge":
    st.header("🌟 Daily Growth Challenge")
    challenges = [
        "Write down three things you learned today.",
        "Share a mistake you made recently and the lesson learned.",
        "Set a new goal and outline steps to achieve it.",
        "Encourage someone by sharing an inspiring story.",
        "Reflect on a tough situation and how you overcame it.",
        "Read about a successful growth mindset leader and summarize.",
        "Step out of your comfort zone and document your experience."
    ]
    challenge = random.choice(challenges)
    st.subheader("✨ Your Challenge Today:")
    st.write(f"📝 {challenge}")
    response = st.text_area("How will you complete this challenge?")
    if st.button("Submit Response"):
        data["challenges"].append({"challenge": challenge, "response": response})
        save_data(data)
        st.success("🎉 Response saved! Keep growing!")

# Quiz Section
elif page == "Quiz":
    st.header("🧠 Growth Mindset Quiz")
    questions = [
        {"q": "What is a key trait of a growth mindset?", "opts": ["Avoiding challenges", "Embracing challenges", "Giving up easily"], "a": "Embracing challenges"},
        {"q": "How should you view mistakes?", "opts": ["As failures", "As learning opportunities", "As things to avoid"], "a": "As learning opportunities"},
    ]
    score = sum(st.radio(q["q"], q["opts"], key=q["q"]) == q["a"] for q in questions)
    if st.button("Submit Quiz"):
        st.success(f"🎯 Your score: {score}/{len(questions)}")

# Journal & Reflection
elif page == "Journal & Reflection":
    st.header("📖 Journal & Reflection")
    journal_entry = st.text_area("Reflect on today's growth journey:")
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

# File Converter
elif page == "File Converter":
    st.header("📂 File Converter (CSV ↔ Excel)")
    uploaded_files = st.file_uploader("Upload CSV or Excel files:", type=["csv", "xlsx"], accept_multiple_files=True)
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        df = pd.read_csv(file) if file_ext == ".csv" else pd.read_excel(file)
        st.write(f"📌 *{file.name}* ({file.size / 1024:.2f} KB)")
        st.dataframe(df.head())
        if st.checkbox(f"📊 Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            df.to_csv(buffer, index=False) if conversion_type == "CSV" else df.to_excel(buffer, index=False, engine='openpyxl')
            buffer.seek(0)
            st.download_button(label=f"⬇ Download {file.name} as {conversion_type}", data=buffer, file_name=file.name.replace(file_ext, f".{conversion_type.lower()}"), mime=f"text/{conversion_type.lower()}" if conversion_type == "CSV" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

st.success("🎉 All features are ready! Keep learning and growing! 🚀")
