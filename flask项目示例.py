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




本地部署 使用   termux

尝试更改 Termux 的主目录。为了确保你能够成功将 Termux 的主目录更改为 /storage/emulated/0/termux_files，请按照以下步骤仔细操作。
1. 创建目标目录首先，确保你在内置存储中创建了一个新的目录：mkdir -p /storage/emulated/0/termux_files
2. 复制文件到新目录将现有的 Termux 目录内容复制到新的目录中：cp -r /data/data/com.termux/files/home/* /storage/emulated/0/termux_files/

3.将 HTML 文件放在 Flask 的静态文件夹中创建一个名为 static 的文件夹，并将 index.html 文件放入其中。然后在 Flask 应用中添加一条路由来提供这个文件。# 修改后的 app.py


在你的项目目录中创建一个名为 static 的文件夹非常简单。
可以用在/storage/emulated/0/termux_files直接创建名为 static 的文件夹

你也可以使用命令行或图形界面来创建这个文件夹。使用命令行创建 static 文件夹打开终端或命令提示符。导航到你的项目目录。
例如，如果你的项目在 termux_files 文件夹中，
可以使用以下命令：cd/storage/emulated/0/termux_files

可以用mt直接创建static 文件夹，也可以使用命令来创建

创建名为 static 的文件夹：mkdir static

将你的 index.html 文件放到 static 文件夹中。
例如，如果你的 index.html 文件在当前目录下，可以使用以下命令：mv index.html static/

使用图形界面创建 static 文件夹打开你的文件管理器。导航到你的项目目录。创建一个新文件夹并命名为 static。将 index.html 文件拖放到 static 文件夹中。更新后的项目结构你的项目目录结构应该类似于以下内容：
termux_files/
├── app.py
└── static/
    └── index.html这样，当你运行 Flask 应用时，Flask 将能够找到并提供 static 文件夹中的 index.html 文件





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


