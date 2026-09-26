# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一个专业心理咨询师"},
        {"role": "user", "content": "有没有什么推荐的,释放压力的方式"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "disabled"}}
)

print(response.choices[0].message.content)