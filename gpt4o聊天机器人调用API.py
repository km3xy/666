工具termux

import openai

# 替换为你的 OpenAI API 密钥
openai.api_key = 'sk-proj-你的api密钥'

def chat_with_gpt4(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # 使用合适的模型
        messages=messages
    )
    return response['choices'][0]['message']['content']

# 初始系统消息
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You:用户    ")
    if user_input.lower() in ['exit', 'quit']:
        print("Chatbot: Goodbye!")
        break
    messages.append({"role": "user", "content": user_input})
    bot_response = chat_with_gpt4(messages)
    print(f"Chatbot: {bot_response}")
    messages.append({"role": "assistant", "content": bot_response})
