from flask import Flask, request, jsonify, send_from_directory
import openai


app = Flask(__name__)

# 替换为你的 OpenAI API 密钥
openai.api_key = '你的api密钥'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",  # 使用合适的模型
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    ) 


assistant_message = response.choices[0].message['content'].strip()
    return jsonify({"message": assistant_message})

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)  # 使用不同的端口以避免冲突





对应的html    index.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat with GPT-4</title>
</head>
<body>
    <h1>Chat with GPT-4</h1>
    <input type="text" id="user-input" placeholder="Enter your message here">
    <button id="send-button">Send</button>
    <div id="response"></div>

    <script>
        document.getElementById('send-button').addEventListener('click', function() {
            const userMessage = document.getElementById('user-input').value;
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({message: userMessage})
            })
            .then(response => response.json())
            .then(data => {
                const responseDiv = document.getElementById('response');
                if (data.error) {
                    responseDiv.textContent = `Error: ${data.error}`;
                } else {
                    responseDiv.textContent = `Assistant: ${data.message}`;
                }
            })
            .catch(error => console.error('Error:', error));
        });
    </script>
</body>
</html>





    
    assistant_message = response.choices[0].message['content'].strip()
    return jsonify({"message": assistant_message})

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)  # 使用不同的端口以避免冲突



项目目录结构应该类似于以下内容：
termux_files/
├── app.py
└── static/
    └── index.html这样，当你运行 Flask 应用时，Flask 将能够找到并提供 static 文件夹中的 index.html 文件




    启动 Flask 应用在终端中导航到你的项目目录并运行 Flask 应用：python app.py

首先进入项目目录
cd /storage/emulated/0/termux_files

然后输入命令 python app.py


.../0/termux_files $ python  app.pyServing Flask app 'app'Debug mode: on WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.Running on http://127.0.0.1:5000 Press CTRL+C to quit


看来你已经成功将 Flask 应用程序运行在端口 5000 上。现在你可以测试一下应用程序，确保它能够正常工作。测试步骤访问应用程序：在浏览器中访问 http://127.0.0.1:5000  输入消息并点击 "Send" 按钮：在文本框中输入消息，然后点击 "Send" 按钮。



然后在浏览器中访问 http://127.0.0.1:5000/，你应该会看到你的聊天界面，并且可以与 OpenAI 助手进行交互。


以此类推可以创建更多的flask项目

创建其他项目时端口和文件名称不能重复，
可以依次类加   app.py     index.html        
端口  5000

app2.py    index2.html   端口 5001
或者创建新的项目目录

termux_files/
├── app2.py
└── static2/
index.html

端口5001

或者创建新的项目目录

termux_files/
├── app3.py
└── static3/
index2.html

端口5002


工具termux


