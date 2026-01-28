import streamlit as st
import subprocess
import pandas as pd
import os
import time

st.set_page_config(
    page_title="Smile for Attendance",
    page_icon="👀",
    layout="centered"
)


st.markdown("""
<style>
.title { text-align:center; font-size:48px; font-weight:800; }
.subtitle { text-align:center; font-size:16px; color:#666; margin-bottom:40px; }

.button-hover button {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color:white; border-radius:18px;
    padding:16px 26px; font-size:18px;
    transition:0.3s;
}
.button-hover button:hover {
    transform: translateY(-6px);
    box-shadow:0px 10px 25px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="title">😊 Smile for Attendance 👀</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Even though it’s painful… a peaceful smile helps 😌✨</div>',
    unsafe_allow_html=True
)

st.divider()


st.subheader("👤 Register a New Student")

uid = st.text_input("Student UID")
name = st.text_input("Student Name")

with st.container():
    st.markdown('<div class="button-hover">', unsafe_allow_html=True)
    if st.button("✨ Register Face"):
        st.info("Smile softly for the camera 📸")
        subprocess.run(
            ["python", "face_registration.py"],
            input=f"{uid}\n{name}\n",
            text=True
        )
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()


st.subheader("🕒 Attendance")

col1, col2 = st.columns(2)


with col1:
    st.markdown('<div class="button-hover">', unsafe_allow_html=True)
    if st.button("🌸 Punch In"):
        st.info("Hurry up! Don’t be late ⏰✨")
        subprocess.run(
            ["python", "face_recognition.py"],
            env={**os.environ, "PUNCH_MODE": "IN"}
        )
        st.success("Signed in successfully 💖")
        st.balloons()  # 🎈 HAPPY EFFECT
    st.markdown('</div>', unsafe_allow_html=True)


with col2:
    st.markdown('<div class="button-hover">', unsafe_allow_html=True)
    if st.button("☁️ Punch Out"):
        subprocess.run(
            ["python", "face_recognition.py"],
            env={**os.environ, "PUNCH_MODE": "OUT"}
        )

        # 😢 SAD VISUAL FEEL (NO WHITE BOX)
        st.error("We will miss you… take care 😢💔")
        st.toast("😢 😭 😔", icon="💭")
        time.sleep(0.3)
        st.toast("☁️ ☁️ ☁️", icon="☁️")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()


st.subheader("👀 Who all are present today? ✨")

if os.path.exists("attendance.csv"):
    df = pd.read_csv("attendance.csv")

    df["Date"] = df["Date"].astype(str).str.strip()
    df["PunchIn"] = df["PunchIn"].astype(str).str.strip()
    df["PunchOut"] = df["PunchOut"].astype(str).str.strip()

    df["PunchOut"] = df["PunchOut"].replace(
        ["", "nan", "NaN", "None"], "---"
    )

    st.dataframe(df, use_container_width=True)
else:
    st.info("No attendance yet… waiting for smiles 😊")
