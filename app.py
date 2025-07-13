# app.py
import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils import extract_text
from prompts import SUMMARY_PROMPT, QA_PROMPT, CHALLENGE_PROMPT, EVAL_PROMPT

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="GenAI Document Assistant")
st.title("📄 Smart Research Assistant")

# Initialize chat history memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_file = st.file_uploader("Upload a PDF or TXT document", type=["pdf", "txt"])

if uploaded_file:
    doc_text = extract_text(uploaded_file)
    st.subheader("🔎 Auto Summary")
    summary = model.generate_content([SUMMARY_PROMPT, doc_text]).text
    st.write(summary)

    st.subheader("💬 Ask Anything")
    user_q = st.text_input("Ask a question about the document:")
    if st.button("Get Answer") and user_q:
        history = st.session_state.chat_history
        history.append({"role": "user", "content": user_q})
        response = model.generate_content([QA_PROMPT.format(question=user_q), doc_text])
        history.append({"role": "assistant", "content": response.text})
        st.session_state.chat_history = history
        st.write(response.text)

    # Show memory history below
    if st.session_state.chat_history:
        st.markdown("---")
        st.subheader("🧠 Chat Memory")
        for idx, msg in enumerate(st.session_state.chat_history[::-1]):
            st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")

    st.subheader("🎯 Challenge Me")

    if "challenge_questions" not in st.session_state:
        st.session_state.challenge_questions = []

    if st.button("Generate Questions"):
        challenge = model.generate_content([CHALLENGE_PROMPT, doc_text]).text
        st.session_state.challenge_questions = [q.strip() for q in challenge.split("\n") if q.strip()][:3]

    if st.session_state.challenge_questions:
        st.subheader("Your Challenge Questions")
        for idx, q in enumerate(st.session_state.challenge_questions):
            st.markdown(f"**Q{idx+1}: {q}**")
            user_ans = st.text_input(f"Your answer to Q{idx+1}", key=f"qa_{idx}")
            if user_ans:
                feedback = model.generate_content([
                EVAL_PROMPT.format(question=q, answer=user_ans), doc_text
                ]).text
                st.write(f"📝 Feedback: {feedback}")
