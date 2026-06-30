from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

with open("marketing.txt", "r") as file:
    context = file.read()

question = input("Ask a marketing question: ")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": f"You are a marketing assistant.\n\n{context}"},
        {"role": "user", "content": question}
    ]
)

print(response.choices[0].message.content)
