# Please install OpenAI SDK first: `pip3 install openai`
#chat or reasoner

from openai import OpenAI

client = OpenAI(api_key="sk-856013722bfd421f96ac47ed9199a777>", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你好！"},
    ],
    stream=True
)

print(response.choices[0].message.content) # type: ignore