# prompts.py

SUMMARY_PROMPT = """
You are an AI research assistant. Summarize the following document in under 150 words, focusing on the core objective, methodology, and findings.
"""

QA_PROMPT = """
You are a document comprehension assistant. Based on the following document, answer the user's question accurately. Use a direct quote from the text in your answer.


Question: {question}
"""

CHALLENGE_PROMPT = """
From the document below, generate exactly three unique logic-based or comprehension questions that test understanding of the content. 

Only return the questions — do NOT include explanations, rationales, answers, or introductory text. Each question should be standalone and phrased clearly on a new line.

Do not number the questions with '1.', 'Q1:', etc. Just write each question on its own line.
"""

EVAL_PROMPT = """
Evaluate the following user's answer to the given question based on the document. Mention if the answer is correct, partially correct, or incorrect and justify with a source from the text.

Question: {question}
Answer: {answer}
"""
