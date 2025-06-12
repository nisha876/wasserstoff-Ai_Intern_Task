import openai

def generate_answer(question, chunks):
    content = "\n".join([f"{c['text']} (Source: {c['source']})" for c in chunks])
    prompt = f"Question: {question}\n\nContent:\n{content}\n\nAnswer with citations and summarize key themes."
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return res.choices[0].message.content, extract_themes(res) # type: ignore
