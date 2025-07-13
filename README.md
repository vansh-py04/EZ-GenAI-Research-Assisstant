# EZ Smart Research Assisstant

# Deployed Link

https://ez-genai-research-assisstant.onrender.com

---

An intelligent document-aware assistant built with Google Gemini and Streamlit that:

 Accepts PDF or TXT document uploads

 Summarizes the content (≤150 words)

 Answers user questions based on document content with justification

 Generates logic-based comprehension questions

 Evaluates user responses with document-grounded feedback

 Maintains memory of all interactions

 # Features
## ✅ Upload and Auto-Summary

Upload .pdf or .txt documents

Get a concise summary immediately on upload

## 💬 Ask Anything Mode

Ask any question based on the uploaded document

Gemini answers with context and references paragraph numbers

## 🎯 Challenge Me Mode

App generates 3 reasoning/comprehension-based questions

Users type their answers

Gemini evaluates and justifies correctness

## 🧠 Memory Support

All user interactions are tracked

Questions and answers persist across refreshes

# Tech Stack
✅ Streamlit (frontend/UI)

✅ Google Gemini (Generative AI API)

✅ PyPDF2 for PDF parsing

✅ dotenv for managing API keys

# Clone the repo
    git clone https://github.com/yourusername/genai-doc-assistant.git
    cd genai-doc-assistant

# Install dependencies 
    pip install -r requirements.txt

# Run the app
    python -m streamlit run app.py


# Author
 Yuganter Pratap
