import openai

def generate_answer(question, chunks):
    content = "\n".join([f"{c['text']} (Source: {c['source']})" for c in chunks])
    prompt = f"Question: {question}\n\nContent:\n{content}\n\nAnswer with citations and summarize key themes."
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return res.choices[0].message.content, extract_themes(res) # type: ignore


# llm.py
def generate_theme_summary(responses):
    """
    Accepts a list of raw document answers and returns a mock theme summary.
    Replace this with your LLM logic (e.g., OpenAI call).
    """
    theme_names = ["Policy Changes", "Tech Trends", "Government Initiatives"]
    summary = "Based on the documents, major themes include policy shifts and recent technological developments. (Mock summary)"
    return summary, theme_names

